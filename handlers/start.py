import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, CHANNEL_UPDATES, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEOnLVj0FZObesyqVy3VqJJfaqkTm0JGwAC2wgAAo5DAVb47Sdbc1PSei0E")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f""" ** Hey {message.from_user.mention()} , ⚔️\n\n
๏ This is [{bn}](https://t.me/MT_GROUPMUSIC_BOT) ,  !
➻ 👑Official Account🖤
💟Wish Me On 15 August 🎂
⚡My Life My Rules💪
🎶Music ka Diwana💥
🕉️Mahadev Bhakt🕉️
♍I’m not Rich ßut I’m Royal 👑
༒︎Iɴsᴛᴀɢʀᴀᴍ ɪᴅ ༒︎ ☠︎︎ mt_legend_xd ☠︎︎.

──────────────────
๏  All of my command can be used with My command handle : ( / . • $ ^ ~ + * ? )
➻ Made 🫶🏻 by : [𝐇𝐀𝐂𝐊𝐄𝐑❤️‍🔥](https://t.me/MT_LEXTUS_XD) ** """,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✚ group me add kar re ", url=f"https://t.me/MT_GROUPMUSIC_BOT?startgroup=true"
                       ),
                 ],[
                    InlineKeyboardButton(
                        "⚔️ Chal Channel ko support kar  ", url=f"https://t.me/AASHIYANA_MERA"
                    ),
                    InlineKeyboardButton(
                        "⚔️ Group Support ", url=f"https://t.me/COOKIE_WORLD"
                    )
                  ],[
                    InlineKeyboardButton(
                        "👤 King owner ", url=f"https://t.me/MT_LEXTUS_XD"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 Developer ", url=f"https://t.me/MT_LEXTUS_XD"
                    ),
                  ],[
                    InlineKeyboardButton(
                        "✅ Inline ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "💡 Git repo", url="https://telegra.ph/file/089864f9401b686c645cb.mp4"
                    )]
            ]
       ),
    )

