import discord
import os
from game_logic import Logic
from render import Render
import numpy as np

client = discord.Client()

games = []
r = Render()


class Game():
    def __init__(self, player1, player2, id_game):
        self.player1 = player1
        self.player2 = player2
        self.id_game = id_game
        self.won = False
        self.logic = Logic()

        self.next_to_move = 1

    def get_image(self):
        return r.render_matrix(np.flip(self.logic.board, 0))

    def move(self, column):
        print(f'Moved in column ${column}')

        self.logic.insert_jeton(self.logic.empty_row(column), column, self.next_to_move)

        if (self.logic.isDraw()):
            self.won = True
            return (r.render_matrix(np.flip(self.logic.board, 0), -1), -1)
        if (self.logic.win(self.next_to_move)):
            self.won = True
            return (r.render_matrix(np.flip(self.logic.board, 0), self.next_to_move), self.next_to_move)
        else:
            if self.next_to_move == 1:
                self.next_to_move = 2
            else:
                self.next_to_move = 1
            return (r.render_matrix(np.flip(self.logic.board, 0)), 0)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$start'):
        player1 = message.author.mention
        player2 = message.content.split(" ")[1].replace('!', '')
        id_game = len(games)

        game = Game(player1, player2, id_game)
        games.append(game)

        image = game.get_image()
        image.save("./image.png")

        await message.channel.send(f'{player1} started a game with {player2}. Game ID: {id_game}')
        await message.channel.send(f'{games[id_game].player1}, you\'re first to move!', file=discord.File('image.png'))
        
        os.remove("./image.png")

    if message.content.startswith('$move'):
        id_game = int(message.content.split(" ")[1])
        move_column = int(message.content.split(" ")[2])

        if ((message.author.mention == games[id_game].player1 and games[id_game].next_to_move == 1) \
            or (message.author.mention == games[id_game].player2 and games[id_game].next_to_move == 2)) \
            and games[id_game].won == False:
            
            (image, winner) = games[id_game].move(move_column)

            image.save("./image.png")

            tag_player = games[id_game].player1 if games[id_game].next_to_move == 1 else games[id_game].player2
            
            if winner == -1:
                await message.channel.send(f'It\'s a draw!', file=discord.File('image.png'))
            elif winner == 0:
                await message.channel.send(f'{tag_player}, you\'re next to move in game {id_game}!', file=discord.File('image.png'))
            else:
                await message.channel.send(f'{tag_player}, you\'ve won game {id_game}! Congrats!', file=discord.File('image.png'))

            os.remove("./image.png")

    if message.content.startswith('$help'):
        await message.channel.send("I'm here to help you! How to use me:\nType `$start <tag someone>` to begin a game. Keep a note of the game ID!\nType `$move <game id> <column>` to make a move in one of your current games.\nType `$stop <game id>` to surrender a game.")  

    if message.content.startswith('$py101'):
        await message.channel.send("Why do Python programmers have low self esteem?\n.\n.\n.\nThey're constantly comparing their self to other.")

    if message.content.startswith('$stop'):
        id_game = int(message.content.split(" ")[1])

        tag_player = games[id_game].player1 if message.author.mention == games[id_game].player2 else games[id_game].player2
        games[id_game].won = True
        await message.channel.send(f'{tag_player}, you\'ve won game {id_game} by surrender!')

client.run(os.getenv('TOKEN'))
