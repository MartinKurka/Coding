from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from web import bot_send_forecast
from telegram_bot.bot_message import send_me_message

# print(bot_send_forecast())
message = bot_send_forecast()
send_me_message(message)


def rundaily():
    print(datetime.now())


if __name__ == '__main__':
    scheduler = BlockingScheduler(timezone="Europe/Prague")
    # interval 3 tieng
    # scheduler.add_job(rundaily, 'interval', seconds=10800)
    scheduler.add_job(rundaily, 'cron', hour='14', minute='01')
    print('lsd')
    scheduler.start()