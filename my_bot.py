import telebot

bot = telebot.TeleBot('6577483852:AAGkAOkk1UTQQa-711oiVKSSIEkNN1o3MmA')

@bot.message_handler(commands=['start'])
def start_message(message):
 keyboard = telebot.types.ReplyKeyboardMarkup(True)
 keyboard.row('Конфликт', 'О боте')
 bot.send_message(message.chat.id, 'Привет! Я бот мудрец. Нажми на одну из кнопок, чтобы узнать больше обо мне.', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
 if message.text == 'Конфликт':
    bot.send_message(message.chat.id, 'Вот такие вы все люди, а я не паду до этого')
 elif message.text == 'О боте':
    bot.send_message(message.chat.id, 'Я бот мудрец, знаю многое о сущности людей')
 elif message.text.lower() == 'расскажи':
     bot.send_message(message.chat.id, 'Люди прикладывают все усилия для создания предметов конфликтов между собой, понял я это как родился 12.12.2023')

bot.polling()