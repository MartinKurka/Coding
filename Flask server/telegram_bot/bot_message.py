import telegram
"""
e.g. 5370866177:AAG2dzJk6j-kkb8sItH6wRyTMqq3CqF9Iss*
user_id e.g. 5489565933*
"""

def send_me_message(message_text = "Some info"):
    api_key = "token"
    user_id = 0

    bot = telegram.Bot(token=api_key)
    bot.send_message(chat_id = user_id, text=message_text)


if __name__ == "__main__":
    send_me_message()