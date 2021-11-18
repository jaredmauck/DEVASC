import json

with open ('js.json') as json_file:
    data = json.load(json_file)
    

    nobrackets = str(data)[1:-1]
    print(type(nobrackets))
    print(nobrackets)

    dicts = eval(nobrackets)

    print(type(dicts))
    print("Hostname: ", dicts["hostname"])
    print("Version: ", dicts["version"])
    print("Model: ", dicts["hardware"][0])
    print("Vendor: Cisco")


    print('"{\\"records\\":[{\\"hostname\\": \\"' + dicts["hostname"] + '\\", \\"serialnumber\\": \\"' + dicts["serial"][0] + '\\", \\"model\\": \\"' + dicts["hardware"][0] + '"},{\\"vendor\\": \\"Cisco\\"},')
    
    print('{\\"hostname\\": \\"' + dicts["hostname"] + '\\", \\"serialnumber\\": \\"' + dicts["serial"][1] + '\\", \\"model\\": \\"' + dicts["hardware"][1] + '"},{\\"vendor\\": \\"Cisco\\"}]}"')

