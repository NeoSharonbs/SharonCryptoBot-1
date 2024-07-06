import os
import psycopg2
import telebot

TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

conn = psycopg2.connect(
    dbname='mydb',
    user='user',
    password='password',
    host='postgres'
)
cursor = conn.cursor()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Crypto Alert Bot!")

@bot.message_handler(commands=['price'])
def send_price(message):
    cursor.execute("SELECT price FROM prices ORDER BY timestamp DESC LIMIT 1")
    price = cursor.fetchone()[0]
    bot.reply_to(message, f"The current price of Bitcoin is ${price}")

bot.polling()