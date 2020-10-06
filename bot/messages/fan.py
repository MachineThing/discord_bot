import requests

def fan(state):
    req = requests.get('http://10.0.0.87/cm?cmnd=status')
    if state == 1 and req.json()['Status']['Power'] == 1:
        return 'It\'s already on stupid'
    elif state == 0 and req.json()['Status']['Power'] == 0:
        return 'It\'s already off stupid'
    else:
        req = requests.get('http://10.0.0.87/cm?cmnd=Power%20Toggle')
        return '👍'

async def msg(msg):
    if 'on' in msg.content.lower() and 'off' in msg.content.lower():
        # The user caused the planet to explode
        await msg.channel.send('IT CAN\'T DO BOTH BRO! In other news:\nhttps://www.theonion.com/earth-explodes-1819564021')
    elif 'on' in msg.content.lower():
        await msg.channel.send(fan(1))
    elif 'off' in msg.content.lower():
        await msg.channel.send(fan(0))
    else:
        await msg.channel.send('The fan can\'t do that you fool!')
