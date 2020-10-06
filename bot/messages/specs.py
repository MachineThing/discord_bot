async def msg(msg):
    commands = [
    ['!help', 'No'],
    ['!specs', 'Gives you my pc specs'],
    ['!fan on|off', 'Control Mason\'s fan']
    ]
    helptext = 'Find help yourself you poop. Anyways here is my commands.\n\n'
    for command in commands:
        helptext = helptext+command[0]+' - '+command[1]+'\n'
    helptext = helptext+'\nHappy now?'
    await msg.channel.send(helptext)
