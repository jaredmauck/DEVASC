import json

j = """[
  {
    "version": "25.05.1",
    "rommon": "IOS-XE",
    "hostname": "SW-001",
    "uptime": "5 years, 5 weeks, 3 days, 11 hours, 05 minutes",
    "uptime_years": "5",
    "uptime_weeks": "5",
    "uptime_days": "3",
    "uptime_hours": "11",
    "uptime_minutes": "05",
    "reload_reason": "PowerOn",
    "running_image": "packages.conf",
    "hardware": [
      "C9300-48P",
      "C9300-48A"
    ],
    "serial": [
      "SER0001",
      "SER0002"
    ],
    "config_register": "0x102",
    "mac": [
      "00:00:00:00:00:01",
      "00:00:00:00:00:02"
    ],
    "restarted": "12:00:00 PDT Thu Jun 1 2021"
  }
]"""[1:-1] 

jdict = json.loads(j)
hostname = jdict["hostname"]    
for hardwareItems, serialItems in zip(jdict["hardware"], jdict["serial"]):
    print(f'model: {hardwareItems}, serial: {serialItems}')
#if you have backslashes you can use normal print with pluses between
    print('model: ' + hardwareItems + ', serial: ' + serialItems)
