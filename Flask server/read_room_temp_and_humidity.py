import matplotlib.pyplot as plt
import numpy as np
import mysql.connector

def read_room_temps():
    x_timeline = []
    y_temp = []
    y_humidity = []
    connection = mysql.connector.connect(host='',
                                         database='teploty',
                                         user='martin',
                                         password='hafling')
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

    fig, axs = plt.subplots(2, 1)
    fig.set_size_inches(12, 10, forward=True)

    title = "Aktuálně " + str(x_timeline[len(x_timeline) - 1]) + " |    " + str(
        y_temp[len(y_temp) - 1]) + " °C   " + str(y_humidity[len(y_humidity) - 1]) + " %"
    fig.suptitle(title, fontsize=20)

    axs[0].plot(x_timeline, y_temp, 'r')
    axs[0].set_xticks(np.arange(1, len(x_timeline), 15))
    axs[0].set_ylabel('Teplota [°C]')
    axs[0].tick_params(axis='x', rotation=45)
    axs[0].grid(True)

    axs[1].plot(x_timeline, y_humidity, 'b')
    axs[1].set_xticks(np.arange(1, len(x_timeline), 15))
    axs[1].set_ylabel('Vlhkost [%]')
    axs[1].grid(True)
    axs[1].tick_params(axis='x', rotation=45)


    plt.subplots_adjust(hspace=0.415)
    fig.tight_layout()
    plt.savefig("static/images/teplota_pokoj.png")
    # plt.show()

if __name__ == "__main__":
    read_room_temps()
