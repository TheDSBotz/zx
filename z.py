import requests
from bs4 import BeautifulSoup

proxies = {
    "http": "http://RpQQ6Q:bRapWN@168.81.251.135:8000",
    "https": "http://RpQQ6Q:bRapWN@168.81.251.135:8000"
}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url = "https://httpbin.org/ip"

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
