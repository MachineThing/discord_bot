from bot.messages import (
    help, specs, fan
)

async def get_msg(msg):
    if msg.content.lower().startswith('!help'):
        await help.msg(msg)
    if msg.content.lower().startswith('!specs'):
        await specs.msg(msg)
    if msg.content.lower().startswith('!fan'):
        await fan.msg(msg)
