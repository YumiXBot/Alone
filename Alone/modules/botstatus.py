from pyrogram import filters
from Alone.database.users_db import *
from Alone.helpers.status import *
from Alone import app, COMMAND_HANDLER, OWNER


@app.on_message(filters.command("stats", COMMAND_HANDLER) & filters.user(OWNER))
async def botstats(_, message):
    NUM_CHATS = await chats.count_documents({})
    NUM_USERS = await users.count_documents({})
    await message.reply_text(f"""
**ALONE STATS:**

**TOTAL USERS:** {NUM_USERS}
**TOTAL CHATS:** {NUM_CHATS}
""")