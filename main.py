from discord.ext import commands, tasks
import os, discord, time

print("'m'")
client = commands.Bot(command_prefix='!', intents=discord.Intents.default())


@client.command()
async def ping(ctx):
    await ctx.send('Pong')


@client.event
async def on_ready():
    await sendFromConsole()


@client.event
async def on_message(message):
    print(message.author)
    print(f">{message.author.id} said {message.content}")


@client.event
async def sendFromConsole():
    await client.wait_until_ready()
    channel = client.get_channel(892469076067221567)
    run = True
    while run:
        await client.wait_until_ready()
        message = input('Enter message: ')
        try:
            await channel.send(message)
        except:
            print("bad message")


client.run(os.environ['TOKEN'])
