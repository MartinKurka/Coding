import sqlite3
import matplotlib.pyplot as plt
import numpy as np

def read_btc():
    conn = sqlite3.connect('bitcoin_database.db')
    cursor = conn.cursor()
    rows = cursor.execute("SELECT * FROM bitcoin ORDER BY date DESC LIMIT 300")

    x_timeline = []
    y_price = []

    for i in rows:
        x_timeline.append(i[1])
        y_price.append(float(i[2]))

    x_timeline = x_timeline[::-1]
    y_price = y_price[::-1]

    fig, ax= plt.subplots()
    fig.set_size_inches(12, 5, forward=True)
    ax.plot(x_timeline, y_price, linewidth=2.0, color="red")
    ax.set_xticks(np.arange(1, len(x_timeline), 20))
    plt.xticks(rotation=45)
    # plt.figure(figsize=(16, 4))
    plt.subplots_adjust(bottom=0.30, left=0.07, right=0.970)

    max_y_lim = max(y_price) + 500
    min_y_lim = min(y_price) - 500
    if min_y_lim < 0:
        min_y_lim = 0

    plt.ylim(min_y_lim, max_y_lim)
    plt.ylabel('Cena v USD')
    plt.title('Bitcoin')
    plt.grid()
    # plt.figure(figsize=(16, 4))
    # plt.show()
    # fig.set_size_inches(18.5, 10.5)
    plt.savefig("static/images/btc_export.png")


if __name__ == "__main__":
    read_btc()