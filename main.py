import telebot
from telebot import types


bot = telebot.TeleBot('BOT_API')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет👋\nЯ InfoAboutUserBot🤖 - помогу дать тебе информацию о твоих данных.\nНапиши /creators - чтобы узнать о создателях бота!',)
    bot.send_message(message.chat.id, 'Напишите что-угодно, для получения информации.')


@bot.message_handler(commands=['creators'])
def creators(message):
    bot.reply_to(message, 'Создатели:\nzzsxd')
    bot.send_message(message.chat.id, 'Напишите что-угодно, для получения информации.')

@bot.message_handler(content_types=['photo', 'video', 'audio', 'voice', 'stickers', 'text'])
def info(message):
    bot.reply_to(message, f"\nПользовательское имя: @{message.from_user.username}\nИмя: {message.from_user.first_name}\nФамилия: {message.from_user.last_name}\nID Пользователя: {message.from_user.id}\nTG Premium: {message.from_user.is_premium}")


bot.polling(none_stop=True)