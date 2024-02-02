from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler
import re
import firebase_admin
from firebase_admin import credentials, initialize_app

# Инициализируем Firebase (предполагается, что вы уже настроили Firebase)
cred = credentials.Certificate("path/to/your/firebase-adminsdk.json")  # Укажите путь к вашему файлу сертификата
initialize_app(cred)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Привет, привет, что-то я тебя не помню. Пройди на стол регистрации и введите свою электронную почту и пароль через пробел."
    )

def validate_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if not re.search("[a-zA-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*()_+]", password):
        return False
    return True

def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    try:
        email, password = text.split(' ', 1)
        if validate_password(password):
            # Здесь добавьте логику для аутентификации через Firebase
            update.message.reply_text("Регистрация прошла успешно!")
        else:
            update.message.reply_text("Пароль не соответствует требованиям.")
    except ValueError:
        update.message.reply_text("Введите электронную почту и пароль, разделенные пробелом.")

def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data == "about_bot":
        query.edit_message_text(text="Я бот-повар, подскажу рецепт крабсбургера.")
    elif query.data == "evening_with_loved_one":
        query.edit_message_text(text="Если вы хотите провести вечер с любимой, то есть много вариантов...")

def show_buttons(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("О боте", callback_data='about_bot')],
        [InlineKeyboardButton("Как провести вечер с любимой?", callback_data='evening_with_loved_one')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)

def main():
    updater = Updater("6773274562:AAH0H40gQ-_K2NTRSzJDr8th0pYSlNKx2qQ", use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.dispatcher.add_handler(CallbackQueryHandler(button_handler))

    updater.start_polling()
    updater.idle()

if _name_ == '_main_':
    main()