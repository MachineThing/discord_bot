from bot.messages import (
    help, specs, fan, unknown
)

async def get_msg(msg):
    if msg.content.lower().startswith(':help'):
        await help.msg(msg)
    elif msg.content.lower().startswith(':specs'):
        await specs.msg(msg)
    elif msg.content.lower().startswith(':fan'):
        await fan.msg(msg)
    elif msg.content.startswith(':'):
        await unknown.msg(msg)
