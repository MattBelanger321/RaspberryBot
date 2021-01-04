import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    link = '<https://www.youtube.com/watch?v=dQw4w9WgXcQ>'

    if message.author == client.user:
        return

    if message.content == ('?helplist'):
        await message.channel.send('Type : ?insult to be insulted')

    if message.content == ('?help') or message.content == ('?HELP'):
        await message.channel.send(
            'How fucking stupid are you i literally insult people it ain\'t rocket science\n\nbut fr type ?acchelp for help')

    if message.content == ('?acchelp'):
        await message.channel.send('Click this for more help' + link)

    if message.content == ('?hello'):
        await message.channel.send('Sup Fuckface')

    if message.content == ('?Adam') or message.content == ('?ADAM') or message.content == ('?adam'):
        await message.channel.send('Ah my Glorious Creator has arrived')

    if message.content.startswith('fuck') or message.content.startswith('FUCK'):
        await message.channel.send('watch your fucking profanity you bitch')
    if message.content == ('?Nick'):
        await message.channel.send('The Asian Man has Arrived')

file = open('config.txt')
client.run(file.read())