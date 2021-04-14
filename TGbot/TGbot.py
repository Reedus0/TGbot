import telebot
import config
from dbworker import set_state, get_current_state

client = telebot.TeleBot(config.config["token"])

gotToken = False

@client.message_handler(commands=["start"])
def login(message):
    set_state(message.chat.id, config.States.S_LOGIN)
    client.send_message(message.chat.id, 'Write your message')

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_LOGIN)
def messageToUser(message):
    client.send_message(message.chat.id, 'Thank you for contacting us!')
    set_state(message.chat.id, config.States.S_END)

@client.message_handler(func=lambda message: get_current_state(message.chat.id) == config.States.S_END)
def passing(message):
    pass

client.polling(none_stop=True, interval=0)
