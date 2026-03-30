import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8176985726:AAEcoXx0R-wpX1_LnSlZzl07f-mNdBGVr2s"

# ПЕРША СИЛКА (КАЗИНО)
CASINO_URL = "https://norvio.fun/Prsp2djM"
# ДРУГА СИЛКА (БОНУС)
BONUS_URL = "https://gguapromo.com/l/6928436812a9aed053072b62"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("🎰 ВЕРИФІКАЦІЯ", web_app=WebAppInfo(url=CASINO_URL))],
        [InlineKeyboardButton("🎁 КАЗИНО", web_app=WebAppInfo(url=BONUS_URL))],
        [InlineKeyboardButton("👤 ПРОФІЛЬ", callback_data="profile")]
    ]
    
    await update.message.reply_text(
        f"🔥 Вітаю, {user.first_name}! 🔥\n\n"
        f"Обери дію нижче:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "profile":
        user = query.from_user
        await query.edit_message_text(
            f"👤 ТВІЙ ПРОФІЛЬ\n\n"
            f"🆔 ID: {user.id}\n"
            f"📝 Ім'я: {user.first_name}\n"
            f"🔗 Юзернейм: @{user.username if user.username else 'немає'}",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("◀️ НАЗАД", callback_data="back_to_menu")
            ]])
        )
    
    elif query.data == "back_to_menu":
        user = query.from_user
        keyboard = [
            [InlineKeyboardButton("🎰 КАЗИНО", web_app=WebAppInfo(url=CASINO_URL))],
            [InlineKeyboardButton("🎁 БОНУС", web_app=WebAppInfo(url=BONUS_URL))],
            [InlineKeyboardButton("👤 ПРОФІЛЬ", callback_data="profile")]
        ]
        await query.edit_message_text(
            f"🔥 Вітаю, {user.first_name}! 🔥\n\nОбери дію нижче:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    logger.info("✅ Бот успішно запущено!")
    app.run_polling()

if __name__ == "__main__":
    main()