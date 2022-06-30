import mysql.connector
from mysql.connector import Error
from req import get_room_temp
from datetime import datetime
from telegram_bot.bot_message import send_me_message
import time

# read time in minutes
t = 5

cursor = None
connection = None

def main():
    global cursor, connection
    while True:
        try:
           connection = mysql.connector.connect(host='',
                                                database='teploty',
                                                user='martin',
                                                password='hafling')
           if connection.is_connected():
               db_Info = connection.get_server_info()
               temp, humidity = get_room_temp()
               # print(date, temp, humidity)
               cursor = connection.cursor()
               cursor.execute(f"INSERT INTO pokoj (date, temp, humidity) VALUES (NOW(), {temp}, {humidity});")
               connection.commit()
        except Error as e:
           print(datetime.now()," --  Error while connecting to MySQL", e)
           try:
               send_me_message("Raspberry mysql_example.py failed")
           except:
               pass
           pass
        finally:
           if connection.is_connected():
               # cursor = connection.cursor()
               # cursor.execute("SELECT * FROM pokoj")
               # myresult = cursor.fetchall()
               # for x in myresult:
               #     print(x)
               cursor.close()
               connection.close()
               # print("MySQL connection is closed")
        time.sleep(t*60)
        cursor = None
        connection = None

if __name__ == "__main__":
    main()