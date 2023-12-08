import requests
from bs4 import BeautifulSoup as bs
import sqlite3

connection = sqlite3.connect('task1.db')
cur = connection.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS User (name VARCHAR(100) NOT NULL,
                                                link VARCHAR(100) NOT NULL)
                                                ''')
cur.execute('''INSERT INTO User (name, link) 
                    VALUES('autoria', 'https://auto.ria.com/uk/legkovie/lamborghini/?page=1'),
                    ('privat-bank', 'http://privatbank.ua/rates-archive')''')
connection.commit()

sqlstr = 'SELECT name, link FROM User'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()

r = requests.get("https://auto.ria.com/uk/legkovie/lamborghini/?page=1")
html = bs(r.text, "html.parser")
data = html.findall('span', class='bold size22 green')
data1 = html.findall('span', class='blue bold')
names = []
for i in data:
    print(i.text)

grn = int(input('Enter grn: '))

r = requests.get("https://privatbank.ua/rates-archive")

html = bs(r.text, "html.parser")

data = html.findall('div', class='purchase')

cur = []

for i in data:
    cur.append(float(i.span.text))
