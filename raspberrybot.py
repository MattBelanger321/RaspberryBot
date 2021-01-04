import discord
import random
import time
from time import sleep
client = discord.Client()
insult=["Youre a potatoe hah!","Took alot of confidence to get out of bed today","Its not even haloween why are you wearing a mask"]


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
            'How silly are you i literally insult people it ain\'t rocket science\n\nbut fr type ?acchelp for help')

    if message.content.lower() == ('?acchelp'):
        await message.channel.send('Click this for more help' + link)

    if message.content.lower() == ('?hello'):
        await message.channel.send('Sup Bro')

    if message.content.lower() == ('?adam'):
        await message.channel.send('Ah my Glorious Creator has arrived')

    if message.content.lower() == ('?nick'):
        await message.channel.send('The Asian Man has Arrived')

    if message.content.lower() == ('?goodwin'):
        await message.channel.send('https://imgur.com/eTrlD2K')

    if message.content.lower() == ('?justin'):
        await message.channel.send('https://imgur.com/yq8W8Tt')

    if message.content.upper() == ("?MATT"):
        await message.channel.send('The elder has arrived')

    if message.content.lower() == ("?devin"):
        await message.channel.send('My favourite man child arrived everyone say hi ;)')

    if message.content.lower() == ("?tomato"):
        await message.channel.send('Yes, this is indeed a tomato :tomato:')

    if message.content.lower() == ("?insult"):
        ranNum = random.randint(0,len(insult)-1)  #If you want to add insult, refer to line 4 and add new insult to list
        await message.channel.send(insult[ranNum])

    if message.content.lower() == ("?timer"):
        await message.channel.send("How long for the timer?(in minutes)")
        msg = await client.wait_for('message')
        timechosen = msg.content
        time1=timechosen
        while 1:
            if time1.isdigit()==False:
                await message.channel.send("Invalid Entry Please Enter Again!")
                msg = await client.wait_for('message')
                timechosen = msg.content
                time1 = timechosen
                continue
            elif time1.isdigit()==True:
                time1 = int(timechosen)
                break
        print(timechosen)
        print(time1)
        counter2 = int(0)
        while counter2<time1:
            counter=0
            while 1:
                counter+=1
                time.sleep(1)
                print(counter)
                if counter==60:
                    counter2=counter2+1
                    break
        print("Timer Done")
        await message.channel.send('<@753250163216220172>'+" Timer has pinged you, Time to get to WORK!")
file = open('config.txt')
client.run(file.read())