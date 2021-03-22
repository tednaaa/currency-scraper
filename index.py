import requests
from bs4 import BeautifulSoup

url = 'https://www.rbc.ru/crypto/currency/btcusd'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
bitcoin_text = soup.find('div', {'class': 'chart__subtitle'}).text
bitcoin = ''.join(bitcoin_text.split()).split('-')[0]
print(bitcoin)