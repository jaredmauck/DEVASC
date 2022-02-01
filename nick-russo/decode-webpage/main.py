import requests
from bs4 import BeautifulSoup

# url = "https://nytimes.com/"
url = "https://artofnetworkengineering.com/category/podcast/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)


soup = BeautifulSoup(response.text, "html.parser")
header = soup("h2", {"class": "entry-title"})

for h in header:
    print(h.a.string)