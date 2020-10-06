import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        commands = [
        ['!help', 'No'],
        ['!specs', 'Gives you my pc specs'],
        ['!Fan on|off', 'Control Mason\'s fan']
        ]
        helptext = 'Find help yourself you poop. Anyways here is my commands.\n\n'
        for command in commands:
            helptext = helptext+command[0]+' - '+command[1]+'\n'
        helptext = helptext+'\nHappy now?'
        await message.channel.send(helptext)

token = open("token", "r")
tokenstr = token.readline()
token.close()
print('Running.')
client.run(tokenstr)
