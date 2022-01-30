import requests
import json
import xmltojson

url = "http://njrusmc.net/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

xml_2_json = xmltojson.parse(response.text)

output = json.dumps(xml_2_json)

output2 = json.loads(output)

output_dict = json.loads(output2)

print(output_dict["html"]["body"]["h1"])