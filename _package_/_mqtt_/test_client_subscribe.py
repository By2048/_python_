import json
import time

import paho.mqtt.client as mqtt
from mqtt.test_base import HOST, PORT

from mqtt.test_base import MAC, TOPIC

unack = []


def on_connect(client, userdata, flags, rc):
    print("on_connect", str(rc))


def on_message(client, userdata, msg):
    print("on_message", msg.topic, str(msg.payload))


def on_disconnect(client, userdata, rc):
    print("on_disconnect", str(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    print('on_subscribe', mid)
    unack.remove(mid)


client = mqtt.Client(client_id=f"sub-{MAC}")
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.connect(HOST, PORT)

client.connect(HOST, PORT)

client.loop_start()

result, ids = client.subscribe(TOPIC)
unack.append(ids)

while len(unack) != 0:
    time.sleep(1)

time.sleep(9)
client.loop_stop()
client.disconnect()
