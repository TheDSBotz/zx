import requests

url = "https://www.zee5.com/tvshows/details/kar-k>

r = requests.get(url)
print(r.text)
