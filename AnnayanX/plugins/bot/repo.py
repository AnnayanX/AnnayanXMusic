from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnnayanX import app
from config import BOT_USERNAME

start_txt = """**
(っ◔◡◔)っ ♥ ✪ Welcome For AnnayanX Repos
𝙱𝚑𝚊𝚒 𝚁𝚎𝚙𝚘 𝚔𝚎 𝙻𝚒𝚢𝚎 𝚂𝚑𝚊𝚔𝚊𝚕 𝙳𝚎𝚔𝚑𝚒 𝙷𝚊𝚒 𝙺𝚑𝚞𝚍𝚔𝚒 𝙳𝚊𝚏𝚊 𝚑𝚘𝚓𝚊 @𝙰𝚗𝚗𝚊𝚢𝚊𝚗𝚇
**"""





@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/Vrindavaneeko16008"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/AnnayanX"),
          ],
             
[
InlineKeyboardButton("𝖧𝗎𝗋𝗍𝖾𝖽", url=f"https://github.com/AnnayanX/Hurted"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/cb6486633fe8d630a6070.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
