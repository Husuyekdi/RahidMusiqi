from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://te.legra.ph/file/075499337227f2b0630ae.jpg",
                caption=(f"""**Salam {message.from_user.mention} 🎵\nMən {bot}!\nSəsli sohbetlerde musiqi çalabilən botam. Ban yetkisiz, Səs yönetimi yetkisi verib, Asistanı qruba əlavə edin.\n\nSahib  [Sahibim 🎙️](https://t.me/Rahid_2003).**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Məni Qrupa Əlavə Et ❱ ➕", url=f"https://t.me/BTO_Music_Bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/Rahid_Music"
                    ),
                    InlineKeyboardButton(
                        "😍 Sahibim", url="https://t.me/Rahid_2003"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧩 Əmrlər" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Rəsmi Kanal🇦🇿", url=f"https://t.me/Rahid_44"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["bilgi", f"bilgi@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text(" ❗ Not:\n Botun aktif çalışması üçün bu üç yetgi lazimdir:\n- Mesaj silmə yetgisi,\n- Bağlantı ilə dəvət etmə yetgisi,\n- Sesli sohbeti yönetme yetgisi.", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🔴 İstifatəçi Əmrləri", callback_data="herkes")
                 ],[                     
                     InlineKeyboardButton(
                         "⚫ Admin  Əmrləri", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "Geri 🔄", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "🇦🇿 Sahib", url="https://t.me/Rahid_2003")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text(" ❗ Not:\nBotun aktif çalışması üçün bu üç yetgi  lazımdır:\n- Mesaj silmə yetgisi,\n- Bağlantı ilə dəvət etmə yetgisi,\n- Səsli sohbəti yönetme yetgisi.", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "✨İstifadəçi Əmrləri, callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "👑Admin Əmrləri",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "🔄 Geri", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "🇦🇿 Sahib", url="https://t.me/Rahid_2003")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun hərkəs üçün komut menüsü 😉\n\n ▶️ /play - musiqi oxutmaq üçün youtube url'sine vəya musiqi dosyasına yanıt vermə\n ▶️ /play <song name> - istədiyiniz musiqi oxut\n 🔴 \n 🎵 /song <song name> - istədiyiniz musiqi hızlı bir şekildə axtarin\n 🎵 /vbul istədiyiniz videoları hızlı bir şekildə axtarın\n 🔍 /video <query> - youtube'da ayrıntıları içeren videoları axtarma\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🇦🇿 Sahib", url="https://t.me/Rahid_2003")
                 ],
                 [
                     InlineKeyboardButton(
                         "️🔄 Geri", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun adminlər üçün komut menüsü 🤩\n\n ▶️ /resume - musiqi oxutmaqa davam et\n ⏸️ /durdur - oxuyan musiqini dayandirmaq üçün\n 🔄 /atla- Sıraya alınmış musiqiyə kecir.\n ⏹ /skip- musiqi oxumanı dayandırır\n 🔼 /promote botun sadəcə yönətici üçün  olan komutlarını isdifadə üçün kullanıcıya yetgi ver\n 🔽 /demote botun yönətici komutlarını isdifadə edən kullanıcının yetgisini al\n\n ⚪ /asistan - Musiqi asistanı qrubunuza qatılır.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🇦🇿 Sahib", url="https://t.me/Rahid_44")
                 ],
                 [
                     InlineKeyboardButton(
                         "️🔄 Geri", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**Salam {query.from_user.mention} 🎵\nMən {bot}!\nSəsli sohbətlərdə musiqi oxuyan botam. Ban yetgisiz, Ses yönetimi yetgisi verib, Asistanı qruba əlavə edin.\n\n😍Sahibim [️Sahibim](https://t.me/Rahid_2003).**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Məni Qrupa əlavə Et ❱ ➕", url=f"https://t.me/BTO_Music_Bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/Rahid_Music"
                    ),
                    InlineKeyboardButton(
                        "🇦🇿 Sahib", url="https://t.me/Rahid_2003"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌀 Əmrlər (Help)" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Rəsmi Kanal 🇦🇿", url=f"https://t.me/Rahid_Music"
                    )
                ]
                
           ]
        ),
    )
