import mysql.connector
from mysql.connector import Error
from req import get_room_temp
from datetime import datetime
from telegram_bot.bot_message import send_me_message
import time

# Backup database
import sqlite3

# read time in minutes
t = 5

cursor = None
connection = None

def main():
    global cursor, connection
    while True:
        try:
            connection = mysql.connector.connect(host='192.168.0.30',
                                                database='teploty',
                                                user='martin',
                                                password='hafling')
            if connection.is_connected():
                global temp, humidity
                db_Info = connection.get_server_info()
                temp, humidity = get_room_temp()
                # print(date, temp, humidity)
                cursor = connection.cursor()
                cursor.execute(f"INSERT INTO pokoj (date, temp, humidity) VALUES (NOW(), {temp}, {humidity});")
                connection.commit()
        except Error as e:
            print(datetime.now()," --  Error while connecting to MySQL", e)
            temp, humidity = get_room_temp()
            backup(temp, humidity)
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


def backup(temperature, humidity):
    conn = sqlite3.connect('backup_database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pokoj(date, temp, humidity) VALUES (datetime('now','localtime'),"+str(temperature)+","+str(humidity)+");")
    conn.commit()
    conn.close()

def read_backup():
    conn = sqlite3.connect('backup_database.db')
    cursor = conn.cursor()
    rows = cursor.execute("SELECT * FROM pokoj ORDER BY date DESC")
    x_timeline = []
    y_price = []

    for i in rows:
        x_timeline.append(i[1])
        y_price.append(float(i[2]))

if __name__ == "__main__":
    main()