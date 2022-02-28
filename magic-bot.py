import discord
import random

client = discord.Client()

magic_on = False
step = 1
correct_number = random.randint(0, 10)
special_number = correct_number * 2


@client.event
async def on_ready():
    print('Bot is now online and ready to roll')


@client.event
async def on_message(message):
    global magic_on, step, correct_number, special_number

    if(message.author == client.user):
        return

    if(message.content == '!Magic'):
        if(step == 1):
            await message.channel.send('Welcome to the World of Magic🪄')
            await message.channel.send('Think of any amount of money in your mind.💰')
            await message.channel.send('If you are ready with the money in your mind then send a "yo" in this channel.')
            correct_number = random.randint(0, 10) * 100
            special_number = correct_number * 2
            step += 1
            magic_on = True
        else:
            await message.channel.send('Oops!😔 looks like I am busy  with another show. Please wait for it to end')

    if(magic_on):

        if(step == 2):
            if(message.content == 'yo'):
                await message.channel.send('Now, borrow the same amount of money from your friend in your mind.💰')
                await message.channel.send('If you are done with calculations  in your mind then send a "yup" in this channel.')
                step += 1
        if(step == 3):
            if(message.content == 'yup'):
                await message.channel.send(f'Now add {special_number} amount of money to the money which you have in your  mind.💰')
                await message.channel.send('If you are done with calculation in your mind then send a "yo" in this channel.')
                step += 1
        if(step == 4):
            if(message.content == 'yo'):
                await message.channel.send('Divide whatever amount of money you have by 2.💰')
                await message.channel.send('If you are done with calculation in your mind then send a "yup" in this channel.')
                step += 1
        if(step == 5):
            if(message.content == 'yup'):
                await message.channel.send('Now give back the money you took from your friend in the earlier step.💰')
                await message.channel.send('If you are done with calculation in your mind then send  "magic magic !" in this channel.')
                step += 1
        if(step == 6):
            if(message.content == 'magic magic !'):

                await message.channel.send('Abara ka dabara 🪄🪄')
                await message.channel.send('Abara ka dabara 🪄🪄')
                await message.channel.send(f'The amount of money that is left in your mind is {correct_number}.🥳🥳')
                step = 1
                magic_on = False


client.run('YOUR_TOKEN')