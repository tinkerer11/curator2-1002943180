import telebot

bot = telebot.TeleBot('6519714621:AAGCTwQGkXpWS2IMd8cI7oojXIDw3UX1b7Q')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}! ✋')
    bot.send_message(message.chat.id, '*Как дела?*', parse_mode='MarkdownV2')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '/start - запускает бота\n/hi - приветствие\n/morequote - сайт с цитатами\n/quote - цитата\n/joke - шутка\n/morejokes - сайт с шутками\n/bot - вызов бота\n/bye - увидимся 😉')


@bot.message_handler(commands=['hi'])
def main(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}')
    bot.send_message(message.chat.id, f'Это твой id - {message.from_user.id}')
    bot.send_message(message.chat.id, 'и я его знаю 🤫')


@bot.message_handler(commands=['quote', 'Quote'])
def main(message):
    bot.send_message(message.chat.id, 'Вот пару цитат:')
    bot.send_message(message.chat.id, 'Трудности существуют для того, чтобы преодолевать их.©')
    bot.send_message(message.chat.id, 'Только тот, кто делает, чему—то научится.©')


@bot.message_handler(commands=['joke', 'Joke'])
def main(message):
    bot.send_message(message.chat.id, '😄 Вот шутка:')
    bot.send_message(message.chat.id, 'В ресторане:\n— Официант, скажите, почему это блюдо называется "Разбойничье рагу"?\n— Вы это поймёте, когда я принесу счёт. 😉')


@bot.message_handler(commands=['morequote', 'MoreQuote'])
def main(message):
    bot.send_message(message.chat.id, '[||*ТЫКНИ*||](https://citaty.ru/motiviruyusshie/)', parse_mode='MarkdownV2')


@bot.message_handler(commands=['morejokes', 'MoreJokes'])
def main(message):
    bot.send_message(message.chat.id, '[||*ТЫКНИ*||](https://nekdo.ru/random/)', parse_mode='MarkdownV2')


@bot.message_handler(commands=['bot', 'Bot'])
def main(message):
    bot.send_message(message.chat.id, 'я тут!')


@bot.message_handler(commands=['bye', 'Bye'])
def main(message):
    bot.send_message(message.chat.id, f'Пока {message.from_user.first_name}! 👋')
    bot.send_message(message.chat.id, 'Заходи ещё\!', parse_mode='MarkdownV2')


bot.infinity_polling()

