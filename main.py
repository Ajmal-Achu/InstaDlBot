import telebot
from telebot import types

bot = telebot.TeleBot('5910218382:AAHqe2wBnNX6ET0xqoiiniqzwuQwrrUPaZY')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello! I am an Instagram downloader bot made by Ajmal-X0. Please enter the URL of the Instagram post you would like to download.')

    @bot.message_handler(content_types=['text'])
    def get_url(message):

        # Get the URL from the user's message 
        url = message.text

        # Create a keyboard with two buttons 
        keyboard = types.InlineKeyboardMarkup()

        # Create two buttons 
        button1 = types.InlineKeyboardButton('Download Image', callback_data='image') 
        button2 = types.InlineKeyboardButton('Download Video', callback_data='video')

        # Add buttons to the keyboard 
        keyboard.add(button1, button2)

        # Send a message with the keyboard 
        bot.send_message(message.chat.id, 'Please select what you would like to download:', reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: True) 
    def callback_query(call): 

      if call.data == 'image': 

          # Download image from URL and send it to user  
          bot.send_photo(call.message.chat.id, url)  

      elif call.data == 'video':  

          # Download video from URL and send it to user  
          bot
