from AnnayanX import app
from config import BOT_ID, OWNER_ID
from pyrogram import filters
from pyrogram.types import ChatPermissions

# SUDOERS list should be defined in AnnayanX.misc or elsewhere
SUDOERS = [7099470799]  # Example list of sudo users

@app.on_message(filters.command("banall") & filters.user(SUDOERS))
async def ban_all(_, msg):
    chat_id = msg.chat.id    
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.can_restrict_members
    
    if bot_permission:
        async for member in app.iter_chat_members(chat_id):
            try:
                if member.user.is_bot:
                    continue  # Skip banning bots
                await app.kick_chat_member(chat_id, member.user.id)
                await msg.reply_text(f"‣ One more user banned.\n\n➻ {member.user.mention if member.user.username else 'User ID: ' + str(member.user.id)}")
            except Exception as e:
                print(f"Error banning user: {e}")
                continue
    else:
        await msg.reply_text("Either I don't have the right to restrict users or you are not a sudo user.")
