import requests
from bs4 import BeautifulSoup as bs


r = requests.get("https://auto.ria.com/uk/legkovie/lamborghini/?page=1")
html = bs(r.text, "html.parser")
data = html.find_all('span', class_='bold size22 green')
data1 = html.find_all('span', class_='blue bold')
names = []
for i in data:
    print(i.text)

grn = int(input('Enter grn: '))

r = requests.get("https://privatbank.ua/rates-archive")

html = bs(r.text, "html.parser")

data = html.find_all('div', class_='purchase')

cur = []

for i in data:
    cur.append(float(i.span.text))

print(f'EUR: {grn / cur[0]}\nUSD: {grn / cur[1]}\nPLN: {grn / cur[2]}')