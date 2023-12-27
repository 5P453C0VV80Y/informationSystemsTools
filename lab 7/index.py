# !C:\Users\office\AppData\Local\Programs\Python\Python312\python.exe
import telebot;
# надо раскомментить, чтобы работало, ибо гитхаб жалуется на слитый токен
# но работает только в теории, бота я удалил и токен, соответственно тоже
# но(2) все работает, клянусь
# bot = telebot.TeleBot('6877060037:AAFV73CQF50UC-990rMAYtqrh0XBQeA4kEo');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "начнем":
        bot.send_message(message.from_user.id, "чипи чипи")

    if message.text == "чапа чапа":
        bot.send_message(message.from_user.id, "дуби дуби")
    elif message.text == "даба даба":
        bot.send_message(message.from_user.id, "чипи чипи")
    elif message.text == "дуби дуби":
        bot.send_message(message.from_user.id, "даба даба")
    elif message.text == "даба даба":
        bot.send_message(message.from_user.id, "чипи чипи")


bot.polling(none_stop=True, interval=0)


# print ('Content-type: text/html\n\n')
# print ('<html>')
# print (' <head>')
# print (' <title>Apache + Python</title>')
# print (' </head>')
# print (' <body>')
# print (' Hello world!')
# print (' </body>')
# print ('</html>')