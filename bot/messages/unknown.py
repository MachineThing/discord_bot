import random
async def msg(msg):
    texts = [
    'If you keep that up I will say a bad word in this Christian server!',
    'I don\'t know what that means nor I care.',
    ':Shut '+str(msg.author)[:-5]
    ]
    await msg.channel.send(random.choice(texts))
