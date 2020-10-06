from bot.messages import (
    help
)

async def get_msg(msg):
    if msg.content.lower() == '!help':
        await help_msg(msg)
