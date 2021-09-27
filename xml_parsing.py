import xmltodict

with open ("XML_Interface_Config.xml") as data:
    xml_file = data.read()

xml_to_python = xmltodict.parse(xml_file)

print(xml_to_python)
