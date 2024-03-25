from AnnayanX import app
from config import OWNER_ID

from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AnnayanX.utils.annayanx_ban import admin_filter
BOT_ID="6456164805"

@app.on_message(filters.command("banall") & admin_filter)
async def ban_all(_, msg):
    chat_id = msg.chat.id
    x = 0
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members == True
    if bot_permission:
        members = []
        async for m in app.iter_chat_members(chat_id):
            members.append(m.user.id)
            try:
                await app.ban_chat_member(chat_id, members[x])
                print(f"Banning user: {m.user.mention}")
                x += 1
            except Exception:
                pass
    else:
        await msg.reply_text("Either I don't have the right to restrict users or you are not in sudo users")

@app.on_callback_query(filters.regex("^stop$"))
async def stop_callback(_, query):
    await query.message.delete()
