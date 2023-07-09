import requests
from bs4 import BeautifulSoup
proxies = {
    "http": "http://customer-rcodewithharry:ActcitXccR8xbxs@pr.oxylabs.io:7777",
    "https": "http://customer-rcodewithharry:ActcitXccR8xbxs@pr.oxylabs.io:7777"
}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url = "https://apis-jiovoot.voot.com/recapi/voot/v1/voot-web/watchnow?id=3703198&responseType=common"

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
