import requests
from bs4 import BeautifulSoup

# url = "https://nytimes.com/"
url = "https://artofnetworkengineering.com/category/podcast/"

payload={}
headers = {
  'Cookie': 'nyt-a=_T1sbp6kZesZuFCI48EK4D; nyt-purr=cfshcfhssckf'
}

response = requests.request("GET", url, headers=headers, data=payload)


soup = BeautifulSoup(response.text, "html.parser")
header = soup("h2", {"class": "entry-title"})

for h in header:
    print(h.a.string)