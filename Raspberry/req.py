import requests
from html.parser import HTMLParser
from datetime import datetime
all_data = []


class Parser(HTMLParser):
    def handle_data(self, data):
        global all_data
        all_data.append(data)


def get_room_temp():
    global all_data
    try:
        r = requests.get('http://192.168.0.20/')
        # print(r.text)
        parser = Parser()
        parser.feed(r.text)
        # print("data:", all_data)
        temp = 0
        humidity = 0
        for item in all_data:
            if item == "Temperature":
                if float(all_data[all_data.index(item) + 1]) >= 0 and float(all_data[all_data.index(item) + 1]) <= 100:
                    temp = float(all_data[all_data.index(item) + 1])
            elif item == "Humidity":
                # print(all_data[all_data.index(item) - 1])
                if float(all_data[all_data.index(item) + 1]) >= 0 and float(all_data[all_data.index(item) + 1]) <= 100:
                    humidity = float(all_data[all_data.index(item) + 1])
        date = datetime.now().strftime("%d/%m/%Y %H:%M")
        # print(date)
        # print(price_usd, price_czk)
        all_data = []
        return str(date), temp, humidity
    except:
        pass


if __name__ == "__main__":
    get_room_temp()