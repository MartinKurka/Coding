import requests
from html.parser import HTMLParser

all_data = []
class Parser(HTMLParser):
    def handle_data(self, data):
        global all_data
        all_data.append(data)

r = requests.get('http://192.168.0.1/webpages/login.html')
print(r.text)
parser = Parser()
parser.feed(r.text)
# print("data:", all_data)
price_usd = 0
price_czk = 0
for item in all_data:
    print(item)