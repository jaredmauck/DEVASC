import yaml

with open("YAML_Interface_Config.yml") as data:
    yaml_python = yaml.load(data.read(), Loader=yaml.FullLoader)
    print(yaml_python)

print(yaml_python["interface"]["ConfigIf-Configuration"]["ip"]["address"]["IPAddress"])

yaml_python["interface"]["ConfigIf-Configuration"]["ip"]["address"]["IPAddress"] = "172.16.0.2"

print(yaml_python["interface"]["ConfigIf-Configuration"]["ip"]["address"]["IPAddress"])

print(yaml_python)

with open("YAML_Interface_Config.yml", "w") as file:
    yaml_edit = file.write(yaml.dump(yaml_python, default_flow_style = False))
    print(yaml_edit)
