import requests
from html.parser import HTMLParser
from datetime import datetime
import time

all_data = []
class Parser(HTMLParser):
    def handle_data(self, data):
        global all_data
        all_data.append(data)


def get_btc_current_price():
    global all_data
    r = requests.get('https://www.kurzy.cz/bitcoin/')
    # print(r.text)
    parser = Parser()
    parser.feed(r.text)
    # print("data:", all_data)
    price_usd = 0
    price_czk = 0
    for item in all_data:
        if item == " USD":
            # print(all_data[all_data.index(item) - 1])
            price_usd = float(all_data[all_data.index(item) - 1])
        elif item == " CZK":
            # print(all_data[all_data.index(item) - 1])
            price_czk = float(all_data[all_data.index(item) - 1])
    date = datetime.now().strftime("%d/%m/%Y %H:%M")
    print(date)
    # print(price_usd, price_czk)
    all_data = []
    return str(date), price_usd, price_czk
# r = 0
# for i in all_data:
#     print(r, "-", i)
#     r+=1


if __name__ == "__main__":
    get_btc_current_price()