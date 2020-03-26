import json

MAC = 'AABBCCDDEEFF'

TOPIC = f"/device/type/key/{MAC}"

DEVICE = json.dumps({"mac": "0C8C24A6A891", "key": "VTgJDqeX"})

HOST, PORT = "s50.53iq.com", 1883
