import telegram
"""
e.g. 5370866177:AAG2dzJk6j-kkb8sItH6wRyTMqq3CqF9Iss*
user_id e.g. 5489565933*
"""
api_key = "Token"
user_id = 0

bot = telegram.Bot(token=api_key)
bot.send_message(chat_id = user_id, text="pokus message")