import json
import requests
from bs4 import BeautifulSoup


mystocks = ['NKE', 'FB']
stockdata = []

def scrapper(symbol):
    url = f'https://finance.yahoo.com/quote/{symbol}'

    r = requests.get(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    soup = BeautifulSoup(r.text, 'html.parser')
    stock ={
    'company': soup.find('h1', {'class': 'D(ib) Fz(18px)'}).text,
    'price' : soup.find('span', {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
    }
    return stock




for item in mystocks:
    stockdata.append(scrapper(item))
    print('getting and writing stock prices' ,item)
with open ('stock_data.json', 'w') as f:
    json.dump(stockdata, f)
print ('finished')