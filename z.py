import requests
from bs4 import BeautifulSoup
proxies = {
    "http": "http://customer-rcodewithharry:ActcitXccR8xbxs@pr.oxylabs.io:7777",
    "https": "http://customer-rcodewithharry:ActcitXccR8xbxs@pr.oxylabs.io:7777"
}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url = "https://www.amazon.com/OnePlus-Unlocked-Android-Smartphone-Charging/dp/B07XWGWPH5/?_encoding=UTF8&pf_rd_p=fd98176f-b79c-4a77-8259-f0fae864b0d6&pd_rd_wg=L7Wki&pf_rd_r=6VHW0KN3CD6RZ0191H0T&content-id=amzn1.sym.fd98176f-b79c-4a77-8259-f0fae864b0d6&pd_rd_w=pAdjg&pd_rd_r=d40bb4c4-5aba-448c-b46b-2899a48ebe3d&ref_=exports-popular-this-season-with-similar-asins"

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
