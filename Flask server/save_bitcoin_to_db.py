import sqlite3
from bitcoin import CurrentBtcPrice
from read_bitcoin_db import read_btc
import time

# Check time in minutes
check_time = 5

def main():
    while True:
        try:
            current_price, date = CurrentBtcPrice().getusd()
            # print(current_price, date)
            conn = sqlite3.connect('bitcoin_database.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO bitcoin (date, price) VALUES (datetime('now','localtime')," + str(current_price)+");")
            conn.commit()
            conn.close()
            read_btc()
            time.sleep(check_time * 60)
        except:
            print("Failed script")

    # conn = sqlite3.connect('bitcoin_database.db')
    # cursor = conn.cursor()
    # rows = cursor.execute("SELECT * FROM bitcoin")
    # for i in rows:
    #     print(i, type(i))

if __name__ == "__main__":
    main()