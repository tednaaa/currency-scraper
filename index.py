import requests
from bs4 import BeautifulSoup

def get_bitcoin(currency):
	url = f'https://alpari.com/ru/markets/crypto/bitcoin/{currency}'

	res = requests.get(url)

	soup = BeautifulSoup(res.text, 'html.parser')

	bitcoin = soup.find('div', {'class': 'analytics-crypto-item__instrument-price-left'}).text

	return bitcoin

print(get_bitcoin('usd'))