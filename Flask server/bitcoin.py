import requests

api = 'https://api.coindesk.com/v1/bpi/currentprice.json'


class CurrentBtcPrice:
    def __init__(self):
        self.api = api

    def getusd(self):
        response = requests.get(self.api)
        data = response.json()
        update_time = data["time"]["updatedISO"]
        dollar = float(data["bpi"]["USD"]["rate_float"])
        return dollar, update_time

    def geteur(self):
        response = requests.get(self.api)
        data = response.json()
        update_time = data["time"]["updatedISO"]
        euro = float(data["bpi"]["EUR"]["rate_float"])
        return euro, update_time


# usd = CurrentBtcPrice(api).getusd()
# print(usd)
# eur = CurrentBtcPrice(api).geteur()
# print(eur)


"""
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
print()
price_USD = float(data["bpi"]["USD"]["rate"].replace(",",""))
price_EUR = float(data["bpi"]["EUR"]["rate"].replace(",",""))
print("USD: ",price_USD)
print("EUR: ",price_EUR)
# for item in data["bpi"]:
#     for i in item:
#         print(i)
# os.system("pause")
# while True:
#     print("USD: ", data["bpi"]["USD"]["rate"])
#     time.sleep(1)
"""