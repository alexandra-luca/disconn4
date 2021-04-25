import discord
import os

client = discord.Client()

games = []


class Game():
    def __init__(self, player1, player2, id_game):
        self.player1 = player1
        self.player2 = player2
        self.id_game = id_game

        self.next_to_move = 1

    def move(self, column):
        print(f'Moved in column ${column}')
        if self.next_to_move == 1:
            self.next_to_move = 2
        else:
            self.next_to_move = 1

        # TODO


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

        await message.channel.send(f'{player1} started a game with {player2}. Game ID: {id_game}')
        await message.channel.send(f'{games[id_game].player1}, you\'re first to move!')

    if message.content.startswith('$move'):
        id_game = int(message.content.split(" ")[1])
        move_column = int(message.content.split(" ")[2])

        if message.author.mention == games[id_game].player1 and games[id_game].next_to_move == 1:
            games[id_game].move(move_column)
            await message.channel.send(f'{games[id_game].player2}, you\'re next to move!')
        elif message.author.mention == games[id_game].player2 and games[id_game].next_to_move == 2:
            games[id_game].move(move_column)
            await message.channel.send(f'{games[id_game].player1}, you\'re next to move!')

client.run(os.getenv('TOKEN'))
