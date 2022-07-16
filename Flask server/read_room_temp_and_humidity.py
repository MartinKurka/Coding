import matplotlib.pyplot as plt
import numpy as np
import mysql.connector

def read_room_temps():
    x_timeline = []
    y_temp = []
    y_humidity = []
    connection = mysql.connector.connect(host='',
                                         database='',
                                         user='',
                                         password='')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pokoj ORDER BY date DESC LIMIT 200")
    rows = cursor.fetchall()
    for i in rows:
        # print(i)
        x_timeline.append(i[1].strftime("%d/%m/%Y %H:%M"))
        y_temp.append(i[2])
        y_humidity.append(i[3])

    x_timeline = x_timeline[::-1]
    y_temp = y_temp[::-1]
    y_humidity = y_humidity[::-1]

    # print(x_timeline)
    fig, ax1 = plt.subplots()
    fig.set_size_inches(12, 5, forward=True)
    color = 'tab:red'
    ax1.set_xticks(np.arange(1, len(x_timeline), 15))
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.30, left=0.07, right=0.970)
    ax1.set_ylabel('Teplota [°C]', color=color)
    ax1.plot(x_timeline, y_temp, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_xticks(np.arange(1, len(x_timeline), 15))
    ax2.set_ylabel('Vlhkost [%]', color=color)  # we already handled the x-label with ax1
    ax2.plot(x_timeline, y_humidity, color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    title = "Aktuálně " + str(x_timeline[len(x_timeline) - 1]) + " |    " + str(y_temp[len(y_temp)-1])+ " °C   " + str(y_humidity[len(y_humidity)-1])+ " %"
    plt.title(title, fontsize = 20)
    plt.grid()
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.savefig("static/images/teplota_pokoj.png")
    # plt.show()

if __name__ == "__main__":
    read_room_temps()
