import discord, asyncio
from bot import messages as msg

client = discord.Client()

@client.event
async def on_ready():
    print('Online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        pass
    else:
        await msg.get_msg(message)

token = open("token", "r")
tokenstr = token.readline()
token.close()
print('Running.')
client.run(tokenstr)
