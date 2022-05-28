from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://te.legra.ph/file/075499337227f2b0630ae.jpg",
                caption=(f"""**Salam {message.from_user.mention} 🎵\nMən {bot}!\nSəsli söhbətlərdə musiqi botuyam. Səs yetkisi verib, Asistanı qrupa əlavə edin.\n\n[Qrup 🎙️](https://t.me/Gencler_Mekani).**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Qrupuna Sal ❱ ➕", url=f"https://t.me/Rahid_Music_Bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/Rahid_Music"
                    ),
                    InlineKeyboardButton(
                        "💬 Support", url="https://t.me/Gencler_Mekani"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧩 Komutlar", callback_data= "cbbilgi"
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
      await message.reply_text(" ❗ Not:\n Botun aktiv işləməsi üçün üç yetkiye ehtiyac var:\n- Mesaj silme yetkisi,\n- Bağlantı ile davet etme yetkisi,\n- Sesli sohbeti yönetme yetkisi.", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🔴 Hərkəs üçün komutlar", callback_data="hərkəs")
                 ],[                     
                     InlineKeyboardButton(
                         "⚫ Adminlər üçün komutlar", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "Ana menü🏠", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "⚙ Geliştirici", url="https://t.me/Rahid_2003")
                 ]
             ]
         )
    )


@Client.on_message(command(["bilgi", f"bilgi@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text(" ❗ Not:\n Botun aktiv işləməsi üçün üç yetkiye ehtiyac var:\n- Mesaj silme yetkisi,\n- Bağlantı ile davet etme yetkisi,\n- Sesli sohbeti yönetme yetkisi.", 
      reply_markup=InlineKeyboardMarkup(
             [
        [
          InlineKeyboardButton(
            "✨Hərkəs üçün Komutlar", callback_data ="hərkəs")
        ],
        [
          InlineKeyboardButton(
            "👑Yönetici Komutları",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "🏠Ana Menü", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "⚙ Geliştirici", url="https://t.me/Rahid_2003")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("hərkəs"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun hərkəs üçün komut menüsü 😉\n\n ▶️ /oynat - Mahnı oxutmaq üçün youtube url'sinə vəya mahnı dosyasına yanıt verin
 ▶️ /oynat  - istədiyiniz mahnı tap
 🔴 
 🎵 /bul  - istədiyiniz mahnıları sürətli bir şəkildə tapın
 🎵 /vbul istədiyiniz videoları sürətli bir şəkildə tapın
 🔍 /ara  - youtube'da olan videoları axtarın\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Geliştirici", url="https://t.me/Rahid_2003")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botu adminlər üçün komut menüsü 🤩\n\n ▶️ /devam - Mahnı oxutmağa davam et
 ⏸️ /durdur - Mahnını dayandırmaq
 🔄 /atla- Sıraya alınmış musiqi parçasını atlat.
 ⏹ /son - musiqini dayandır
 🔼 /ver botu istifadə etmək üçün istifadəçiyə yetki ver
 🔽 /al Bot üçün istifadəçinin yetkisini al

 ⚪ /asistan - Musiqi asistanı qrupuna qoşulur.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Geliştirici", url="https://t.me/Rahid_2003")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://te.legra.ph/file/075499337227f2b0630ae.jpg",
                caption=(f"""**Salam {message.from_user.mention} 🎵\nMən {bot}!\nSəsli söhbətlərdə musiqi botuyam. Səs yetkisi verib, Asistanı qrupa əlavə edin.\n\n[Qrup 🎙️](https://t.me/Gencler_Mekani).**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Qrupuna Sal ❱ ➕", url=f"https://t.me/Rahid_Music_Bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/Rahid_Music"
                    ),
                    InlineKeyboardButton(
                        "💬 Support", url="https://t.me/Gencler_Mekani"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌀 Komutlar" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Rəsmi Kanal 🇦🇿", url=f"https://t.me/Rahid_44"
                    )
                ]
                
           ]
        ),
    )