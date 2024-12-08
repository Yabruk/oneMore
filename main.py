import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Список передбачень
PREDICTIONS = [
    "Сьогодні тобі пощастить у неочікуваних справах!",
    "Не бійся ризикувати – удача на твоєму боці!",
    "Старий друг принесе гарні новини.",
    "Зосередься на своєму здоров'ї – воно найважливіше.",
    "Успіх вже поруч – будь готовий його зустріти!",
    "Час відпустити минуле і рухатися вперед.",
    "Твоя наполегливість принесе плоди вже цього тижня!",
    "Несподіваний подарунок чекає на тебе найближчим часом."
]

# Обробник команди /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привіт! Натисни /predict, щоб отримати своє передбачення!')

# Обробник команди /predict
def predict(update: Update, context: CallbackContext) -> None:
    prediction = random.choice(PREDICTIONS)
    update.message.reply_text(f"🔮 {prediction}")

# Основна функція для запуску бота
def main() -> None:
    # Встав свій токен бота сюди
    TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("predict", predict))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
