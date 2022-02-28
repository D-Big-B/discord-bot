import discord
import time

client = discord.Client()

game_on = False
step = 0
player1 = ''
player2 = ''
player1_marker = ''
player2_marker = ''
the_board = ['   ']*10
turn = ''
initial_time = time.time()


async def display_board(board, message):

    await message.channel.send('----------')
    await message.channel.send(f'|{board[1]}|{board[2]}|{board[3]}|')
    # await message.channel.send('  |  |  ')
    await message.channel.send('----------')
    await message.channel.send(f'|{board[4]}|{board[5]}|{board[6]}|')
    await message.channel.send('----------')
    # await message.channel.send('  |  |  ')
    await message.channel.send(f'|{board[7]}|{board[8]}|{board[9]}|')
    await message.channel.send('----------')


def space_check(board, position):

    return board[int(position)] == '   '


def win_check(board, mark):
    # Win tic toe game?

    # All rows, and check to see if they all share the same marker?
   # All columns, check to see if marker matches
    # 2 diagonalss , check to see match
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


def place_marker(board, marker, position):
    board[int(position)] = marker


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    # Board is full if we return true

    return True


@client.event
async def on_ready():
    print('Bot is now online and ready to roll')


@client.event
async def on_message(message):
    global game_on, step, player1_marker, player2_marker, the_board, turn, display_board, space_check, place_marker, win_check, full_board_check, player1, player2, initial_time
    if(message.author == client.user):
        return

    if(time.time() - initial_time > 240):
        game_on = False
        step = 0

    if(not game_on):
        if(step == 0):
            if(message.content == '!Play'):
                initial_time = time.time()
                await message.channel.send('Welcome to Tic Tac Toe Game! \n\nThis game will continue for a period of 4 minutes. \nFor marking your input in the board you will have to choose a Position (1-9) in the board.')
                await message.channel.send('Player 1, reply with "yo" in this channel ')

            if(message.content == 'yo'):
                player1 = message.author.id
                await message.channel.send('Player 2, reply with "hey" in this channel')
                step += 1
        elif(step == 1):
            if(message.content == 'hey'):
                player2 = message.author.id
                game_on = True
                step += 1

    if(game_on):
        if(step > 2):
            if(message.content == '!Play'):
                await message.channel.send('Looks like there is an unfinished game\nSo, Please wait till it is completed')

        if(step == 2):
            await message.channel.send(f'<@{player1}>, choose X or O: ')
            step += 1

        if(step == 3):
            if(message.content == 'X'):
                player1_marker = 'X'
                player2_marker = 'O'
                await message.channel.send(f'<@{player1}> will go first')
                step += 1
                turn = 'Player 1'
                await display_board(the_board, message)
                await message.channel.send('Choose a Position (1-9)')

            if(message.content == 'O'):
                player1_marker = 'O'
                player2_marker = 'X'
                await message.channel.send(f'<@{player2}> will go first')
                step += 1
                turn = 'Player 2'
                await display_board(the_board, message)
                await message.channel.send('Choose a Position (1-9)')

        if(step == 4):
            if(turn == 'Player 1' and message.author.id == player1):

                if(message.content in range(1, 9) or space_check(the_board,  message.content)):
                    postion = message.content
                    place_marker(the_board, player1_marker, postion)

                    if(win_check(the_board, player1_marker)):
                        game_on = False
                        initial_time = time.time()
                        step = 0
                        await display_board(the_board, message)
                        await message.channel.send(f'<@{player1}> has WON !!🥳🥳')
                    else:
                        if full_board_check(the_board):
                            initial_time = time.time()
                            game_on = False
                            step = 0
                            await display_board(the_board, message)
                            await message.channel.send('Tie GAME !!')

                        else:
                            turn = 'Player 2'
                            await display_board(the_board, message)
                            await message.channel.send(f'<@{player2}> Choose a Position (1-9) : ')

            if(turn == 'Player 2' and message.author.id == player2):

                if(message.content in range(1, 9) or space_check(the_board,  message.content)):
                    postion = message.content
                    place_marker(the_board, player2_marker, postion)

                    if(win_check(the_board, player2_marker)):
                        game_on = False
                        step = 0
                        initial_time = time.time()
                        await display_board(the_board, message)
                        await message.channel.send(f'<@{player2}> has WON !!🥳🥳')
                    else:
                        if full_board_check(the_board):
                            game_on = False
                            step = 0
                            initial_time = time.time()
                            await display_board(the_board, message)
                            await message.channel.send('Tie GAME !!')

                        else:
                            turn = 'Player 1'
                            await display_board(the_board, message)
                            await message.channel.send(f'<@{player1}> Choose a Position (1-9) : ')


client.run('OTM3MjU5MzI3NTkxNDI0MDAw.YfZIxQ.fAKLSV4lfdMg-AdUDnkpaJ7uJo0')
