from telebot import TeleBot, types

# 🎯 توکن ربات (توکن واقعی شما)
TOKEN = "7227213916:AAEqslEJI7dhdWyLrMTVeUrnK9Sa60WjYnY"
bot = TeleBot(TOKEN)

# 🎬 هندلر شروع /start
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id

    # دکمه باز کردن WebApp (دکمه بالا - آبی)
    webapp_button = types.InlineKeyboardMarkup()
    webapp_button.add(
        types.InlineKeyboardButton(
            text="🚀 اجرای برنامه VIPZEXNET",
            web_app=types.WebAppInfo(url="https://mahdishamiahar.github.io/VIPZEXNETBOT/")
        )
    )
    bot.send_message(
        chat_id,
        "🌟 به ربات VIPZEXNET خوش آمدید!\n\nبرای اجرای برنامه روی دکمه زیر کلیک کنید:",
        reply_markup=webapp_button
    )

    # دکمه‌های کیبورد پایین
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("📩 دریافت نرم‌افزار", "🌐 سایت رسمی ربات")
    keyboard.row("💬 پشتیبانی", "💳 خرید سرویس")
    keyboard.row(
        types.KeyboardButton(
            text="📱 باز کردن برنامه",
            web_app=types.WebAppInfo(url="https://mahdishamiahar.github.io/VIPZEXNETBOT/")
        )
    )
    bot.send_message(chat_id, "از منوی زیر یکی از گزینه‌ها را انتخاب کنید:", reply_markup=keyboard)

# 💡 پاسخ به گزینه‌های منو
@bot.message_handler(func=lambda m: True)
def menu_handler(message):
    if message.text == "📩 دریافت نرم‌افزار":
        bot.send_message(message.chat.id, "📥 لینک نرم‌افزار:\nhttps://github.com/Mahdishamiahar/apVIPZEXNET.git")
    elif message.text == "🌐 سایت رسمی ربات":
        bot.send_message(message.chat.id, "🌍 وب‌سایت:\nhttps://mahdishamiahar.github.io/Web.VIPZEXNET/")
    elif message.text == "💬 پشتیبانی":
        bot.send_message(message.chat.id, "🧑‍💻 پشتیبانی:\n@Supp_ort_VIPZEXNET")
    elif message.text == "💳 خرید سرویس":
        bot.send_message(message.chat.id, "💸 برای خرید سرویس به پشتیبانی پیام بده:\n@Supp_ort_VIPZEXNET")
    else:
        bot.send_message(message.chat.id, "❗ لطفاً یکی از گزینه‌های منو را انتخاب کنید.")

# ♾️ اجرای همیشگی
bot.infinity_polling()