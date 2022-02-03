import requests
from bs4 import BeautifulSoup
url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

soup = BeautifulSoup(response.text, 'html.parser')
heading = soup("p", {"class": "paywall"})

print(heading)