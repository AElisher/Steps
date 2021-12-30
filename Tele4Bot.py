import telebot
import Config4
from telebot import types

client = telebot.TeleBot(Config4.config['token'])


@client.message_handler(commands=['start', 'help'])
def welcome(message):
    
    ikm = types.ReplyKeyboardMarkup(one_time_keyboard=True ,resize_keyboard=True)
    ikm.add(types.KeyboardButton('Yes'), types.KeyboardButton('No'))
    
    msg = client.send_message(message.chat.id, 'Are you a student of our school?', reply_markup=ikm)
    client.register_next_step_handler(msg, user_answer)

    
def user_answer(message):
    if message.text == "Yes":
        rkm = types.ReplyKeyboardMarkup(resize_keyboard=True)
        rkm.add(types.KeyboardButton('Schedule'), types.KeyboardButton('Events'), types.KeyboardButton('Homework'), types.KeyboardButton('Contacts'), types.KeyboardButton('Go Back'))
        msg = client.send_message(message.chat.id, 'What you want to know??', reply_markup=rkm)
        client.register_next_step_handler(msg, school)
    elif message.text == "No":
        msg = client.send_message(message.chat.id, 'Sorry to hear that. \nBut you can apply to our school any time! \nOur Contacts: \nPhone Number: +1 323-665-4526 \nAddress: 4155 Russell Ave, Los Angeles, CA 90027') 
        client.register_next_step_handler(msg, user_answer)
    else:
        msg = client.send_message(message.chat.id, "Sorry, I didn't quiet understand what you mean 😢 ")
        client.register_next_step_handler(msg, user_answer)

def school(message):
    if message.text == 'Schedule':
        msg = client.send_message(message.chat.id, "Sorry, we don't have that information right now.")
        client.register_next_step_handler(msg, school)
    elif message.text == 'Events':
        msg = client.send_message(message.chat.id, "Sorry, we don't have that information right now.")
        client.register_next_step_handler(msg, school)
    elif message.text == 'Homework':
        msg = client.send_message(message.chat.id, "Sorry, we don't have that information right now.")
        client.register_next_step_handler(msg, school)
    elif message.text == 'Contacts':
        msg = client.send_message(message.chat.id, "Our Contacts: \nPhone Number: +1 323-665-4526 \nAddress: 4155 Russell Ave, Los Angeles, CA 90027")
        client.register_next_step_handler(msg, school)
    elif message.text == 'Go Back':
        msg = client.send_message(message.chat.id, "Going Back")
        client.register_next_step_handler(msg, welcome)    

client.polling()    