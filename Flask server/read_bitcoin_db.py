import sqlite3
import matplotlib.pyplot as plt
import numpy as np
# time = ['18-05 14:00', '18-05 15:00', '18-05 16:00', '18-05 17:00', '18-05 18:00', '18-05 19:00', '18-05 20:00', '18-05 21:00', '18-05 22:00', '18-05 23:00', '19-05 00:00', '19-05 01:00', '19-05 02:00', '19-05 03:00', '19-05 04:00', '19-05 05:00', '19-05 06:00', '19-05 07:00', '19-05 08:00', '19-05 09:00', '19-05 10:00', '19-05 11:00', '19-05 12:00', '19-05 13:00', '19-05 14:00', '19-05 15:00', '19-05 16:00', '19-05 17:00', '19-05 18:00', '19-05 19:00', '19-05 20:00', '19-05 21:00', '19-05 22:00', '19-05 23:00', '20-05 00:00', '20-05 01:00', '20-05 02:00', '20-05 03:00', '20-05 04:00', '20-05 05:00', '20-05 06:00', '20-05 07:00', '20-05 08:00', '20-05 09:00', '20-05 10:00', '20-05 11:00', '20-05 12:00', '20-05 13:00']
# temp = [21.64, 22.01, 21.72, 21.35, 20.62, 18.98, 15.59, 13.53, 12.29, 11.3, 10.69, 9.88, 9.01, 8.25, 7.56, 6.96, 7.06, 9.2, 11.7, 14.12, 16.2, 18.34, 20.38, 21.77, 22.85, 23.57, 23.89, 23.64, 22.32, 20.1, 17.75, 15.9, 15.13, 14.16, 13.53, 13.07, 13.33, 13.57, 13.15, 12.93, 12.87, 14.52, 16.31, 18.39, 20.25, 22.07, 23.29, 24.29]

def read_btc():
    conn = sqlite3.connect('bitcoin_database.db')
    cursor = conn.cursor()
    rows = cursor.execute("SELECT * FROM bitcoin ORDER BY date DESC LIMIT 200")

    x_timeline = []
    y_price = []

    for i in rows:
        x_timeline.append(i[1])
        y_price.append(float(i[2]))

    x_timeline = x_timeline[::-1]
    y_price = y_price[::-1]

    fig, ax = plt.subplots()
    fig.set_size_inches(12, 5, forward=True)
    ax.plot(x_timeline, y_price, linewidth=2.0, color="red")
    # ax.plot(time, temp, linewidth=2.0)
    ax.set_xticks(np.arange(1, len(x_timeline), 8))
    plt.xticks(rotation=45)
    # plt.figure(figsize=(16, 4))
    plt.subplots_adjust(bottom=0.30, left=0.07, right=0.970)
    plt.ylim(min(y_price), max(y_price))
    plt.ylabel('Cena v USD')
    plt.title('Bitcoin')
    plt.grid()
    # plt.figure(figsize=(16, 4))
    # plt.show()
    # fig.set_size_inches(18.5, 10.5)
    plt.savefig("static/images/btc_export.png")


if __name__ == "__main__":
    read_btc()