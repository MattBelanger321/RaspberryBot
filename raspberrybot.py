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

    if message.content.lower() == ('?helplist'):
        await message.channel.send('Type : ?insult to be insulted')

    if message.content.lower() == ('?help'):
        await message.channel.send(
            'How fucking stupid are you i literally insult people it ain\'t rocket science\n\nbut fr type ?acchelp for help')

    if message.content.lower() == ('?acchelp'):
        await message.channel.send('Click this for more help' + link)

    if message.content.lower() == ('?hello'):
        await message.channel.send('Sup Fuckface')

    if message.content.lower() == ('?adam'):
        await message.channel.send('Ah my Glorious Creator has arrived')

    if message.content.lower() == ('fuck'):
        await message.channel.send('watch your fucking profanity you bitch')

    if message.content.lower() == ('?nick'):
        await message.channel.send('The Asian Man has Arrived')

    if message.content.lower() == ('?goodwin'):
        await message.channel.send('https://imgur.com/eTrlD2K')

    if message.content.lower() == ('?justin'):
        await message.channel.send('https://imgur.com/yq8W8Tt')

    if message.content.upper() == ("?MATT"):
        await message.channel.send('The elder has arrived')

file = open('config.txt')
client.run(file.read())