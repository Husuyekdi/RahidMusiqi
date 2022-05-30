from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://te.legra.ph/file/075499337227f2b0630ae.jpg",
                caption=(f"""**Salam {message.from_user.mention} 🎵\nMən {bot}!\nSəsli söhbətlərdə musiqi oxuyan botam. Ban yetkisiz, Səs yetkisi verib, Asistanı qrupa əlavə edin.\n\nSahibim👉  [Rahid](https://t.me/Rahid_2003)**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Məni Qrupa Əlavə Et ❱ ➕", url=f"https://t.me/Rahid_Music_Bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/Rahid_Asistan"
                    ),
                    InlineKeyboardButton(
                        "Support 💬", url="https://t.me/Gencler_Mekani"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧩 Əmrlər" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Rəsmi Kanal 🇦🇿", url=f"https://t.me/Rahid_44"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["bilgi", f"bilgi@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text(" ❗ Not:\n Botun aktiv işləməsi üçün bu üç yetki vermək lazımdır ⬇️:\n- Mesaj silmə yetkisi,\n- Bağlantı ilə dəvət etmə yetkisi,\n- Səsli səhbəti yönətmə yetkisi.", 
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
                         "Support 💬", url="https://t.me/Gencler_Mekani")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text(" ❗ Not:\nBotun aktiv işləməsi üçün bu üç yetki vermək lazımdır ⬇️\n- Mesaj silmə yetkisi.\n- Bağlantı ilə dəvət etmə yetkisi.\n- Səsli sohbəti yönətmə yetkisi.", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "✨Hərkəs üçün əmrlər", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "👑Admin əmrləri",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "🔄 Geri", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "Sahib 🇦🇿", url="https://t.me/Rahid_2003")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun hərkəs üçün əmr menyusu 😉\n\n ▶️ /play - musiqi oxutmaq üçün youtube url'sinə vəya musiqi dosyasına yanıt verin\n ▶️ /play <song name> - istədiyiniz musiqi oxut\n 🔴 \n 🎵 /song <song name> - istədiyiniz musiqi sürətli bir şəkildə axtarın\n 🎵 /vbul - istədiyiniz videoları sürətli bir şəkildə axtarın\n 🔍 /video <query> - youtube'da olan videoları axtarın\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "Sahib 🇦🇿", url="https://t.me/Rahid_2003")
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
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun adminlər üçün əmr menyusu 🤩\n\n ▶️ /resume - musiqi oxutmağa davam et\n ⏸️ /durdur - oxuyan musiqini dayandır\n 🔄 /atla - Sıraya alınmış musiqiyə kecmək\n ⏹ /skip - musiqi oxumanı dayandır\n 🔼 /promote - botun sadəcə yönətici üçün olan Əmrlərini isdifadə üçün istifadəçiyə yetki ver\n 🔽 /demote - botun yönətici Əmrlərini isdifadə edən istifadəçinin yetkisini al\n\n ⚪ /asistan - Musiqi asistanı qrupunuza qoşulur.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "Sahib 🇦🇿", url="https://t.me/Rahid_2003")
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
    await query.edit_message_text(f"""**Salam {query.from_user.mention} 🎵\nMən {bot}!\nSəsli sohbətlərdə musiqi oxuyan botam. Ban yetkisiz, Səs yönətim yetki verib, Asistanı qrupa əlavə edin.\n\nSahibim👉 [Rahid](https://t.me/Rahid_2003)**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Məni Qrupa Əlavə Et ❱ ➕", url=f"https://t.me/Rahid_Music_Bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/Rahid_Asistan"
                    ),
                    InlineKeyboardButton(
                        "Sahib 🇦🇿", url="https://t.me/Rahid_2003"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌀 Əmrlər (Help)" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Rəsmi Kanal 🇦🇿", url=f"https://t.me/Rahid_44"
                    )
                ]
                
           ]
        ),
    )
