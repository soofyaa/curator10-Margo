import telebot
bot = telebot.TeleBot('6848178654:AAFeB5tmv8Z-XV2G8jAiefsc0WHqBaoQZhA')

@bot.message_handler(commands = ['start'])
def otp(message):
    bot.send_message(message.chat.id, '*Приветик*:)',  parse_mode='Markdown')

@bot.message_handler(commands = ['капибара'])
def otp(message):
    bot.send_photo(message.chat.id, 'https://i.pinimg.com/736x/e3/aa/ea/e3aaeabdec02e77300d98f454279b5fa.jpg')

@bot.message_handler(commands = ['большекапибар'])
def otp(message):
    bot.send_message(message.chat.id, 'Еще больше капибар: https://www.istockphoto.com/ru/фотографии/капибара',  parse_mode='Markdown')

bot.infinity_polling()



