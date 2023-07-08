import requests

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w") as f:
    f.write(r.text)
  
url = "https://www.zee5.com/tvshows/details/kar-k>

fetchAndSaveToFile(url, "data/times.html")
