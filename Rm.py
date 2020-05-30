from telethon import events
import random, re
from uniborg.util import admin_cmd
import asyncio
HARAMI_STR = [
    "`Bahut Pelegy Be`"]



@borg.on(admin_cmd("harami ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(HARAMI_STR) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = HARAMI_STR[bro]
    await event.edit(reply_text)
