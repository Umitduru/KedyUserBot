"""
Sakir Bey / HerlockUserBot Modul birleştirmesi
"""
import re
import os
from telethon import events
from userbot import bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("smsg")

# ████████████████████████████████ #
@register(outgoing=True, pattern="^.send ?(.*)")
async def pm(event):
 
    p = event.pattern_match.group(1)
    m = p.split(" ")

    chat_id = m[0]
    try:  
        chat_id = int(chat_id)
    except BaseException:
        
        pass
  
    msg = ""
    mssg = await event.get_reply_message() 
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await event.edit("@HerlockUserBot `Mesajı gönderdi ✔️`")
    for i in m[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await event.client.send_message(chat_id, msg)
        await event.edit("@HerlockUserBot `Mesajı gönderdi ✔️`")
    except BaseException:
        await event.edit("** @HerlockUserBot Mesajınızı Gönderemedi :(**")
        
CmdHelp('sendmsg').add_command('send', LANG['SM1'], LANG['SM2'], LANG['SM3']).add()
