import requests
from bs4 import BeautifulSoup
# from bs4 import SoupStrainer
import re

# url = "https://www.recorderonline.com/"
# url = "https://nytimes.com/"
# url = "https://artofnetworkengineering.com/category/podcast/"
url = "http://njrusmc.net/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
# only_a_tags = SoupStrainer("a")
regex_class = re.compile(r'.*')
regex = re.compile(r'^h[1-9]')
soup = BeautifulSoup(response.text, "html.parser")
heading = soup(regex, {"class": regex_class})
if heading == []:
    heading = soup(regex)

for h in heading:
    try:
        if h.a is None and h is None:
            pass
        elif h.a is not None:
            print(h.a.string)
        elif h is not None:
            print(h.string)
        else:
            print(h)
    except:
        pass
