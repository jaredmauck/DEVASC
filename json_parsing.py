import json

with open('JSON_Interface_Config.json') as data:
#   json_file = data.read()
#   json_python = json.loads(json_file)
    json_python = json.loads(data.read())
    print(json_python)
