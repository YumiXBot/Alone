#MIT License
#Copyright (c) 2023, ©NovaNetworks

import time
from pyrogram import filters

from Alone import app, start, Alone_Ver
from Alone.helpers.readable_time import get_readable_time
from Alone.Config import COMMAND_HANDLER


@app.on_message(filters.command(["ping"], COMMAND_HANDLER))
async def ping(_, message):
    currentTime = get_readable_time(time.time() - start)
    start_t = time.time()
    rm = await message.reply_photo("https://graph.org//file/6ede45ee5dd3ecfc7314e.jpg", caption="Pong..")
    end_t = time.time()
    time_taken_s = round(end_t - start_t, 3)
    await rm.edit_caption(
        f"""
**BOT VERSION:** {Alone_Ver}

**PING:** {time_taken_s} seconds
**UPTIME:** {currentTime}"""
    )

__mod__ = "MISC"
__help__ = """
**» /ping** - Check If The Bot Is Alive
**» /joinreq** - To Turn On Approve And Decline Buttons In The Chat
**» /tgm** - Upload Photo (Under 5mb) To Cloud And Give Link 
**» /upscale** - Reply To A Image To Upscale It (Improve Its Quality)
**» /id** - Get The Id of a User
**» /gstatus** - Get The Group Stats (TRY IT)

**[NOTE: JOIN REQUESTS ONLY WORKS IF APPROVE SETTINGS ARE ENABLED]**
"""