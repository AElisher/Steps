import telebot
import config3
from telebot import types

bot = telebot.TeleBot(config3.TOKEN, parse_mode='html')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Howdy, how are you doing? Welcome to International School of Los Angeles!')

    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Yes', callback_data='yes')
    item2 = types.InlineKeyboardButton('No', callback_data='no')
    markup.add(item1, item2)
    
    bot.send_message(message.chat.id, 'Are you a student of our school?', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'no':
                bot.send_message(call.message.chat.id, 'Sorry to hear that. \nBut you can apply to our school any time! \nOur Contacts: \nPhone Number: +1 323-665-4526 \nAddress: 4155 Russell Ave, Los Angeles, CA 90027')
            elif call.data == 'yes':
                
                markup = types.InlineKeyboardMarkup(row_width=4)
                item3 = types.InlineKeyboardButton('Schedule', callback_data='schedule')
                item4 = types.InlineKeyboardButton('Events', callback_data='events')
                item5 = types.InlineKeyboardButton('HomeWork', callback_data='homework')
                item6 = types.InlineKeyboardButton('Contacts', callback_data='contacts')
                markup.add(item3, item4, item5, item6)
                
                bot.send_message(call.message.chat.id, 'Great to hear that! \nWhat do you want?', reply_markup=markup)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Are you a student of our school?",
                reply_markup=None)
               
    except Exception as e:
        print(repr(e))          

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'schedule':
                bot.send_message(call.message.chat.id, "Sorry, we don't have that information right now.")
            elif call.data == 'events':
                bot.send_message(call.message.chat.id, "Sorry, we don't have that information right now.")
            elif call.data == 'homework':
                bot.send_message(call.message.chat.id, "Sorry, we don't have that information right now.")
            elif call.data == 'contacts':
                bot.send_message(call.message.chat.id, "Phone Number: +1 323-665-4526 \nAddress: 4155 Russell Ave, Los Angeles, CA 90027")
            
    except Exception as e:
        print(repr(e))    


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)          


bot.infinity_polling()