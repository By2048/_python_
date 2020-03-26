import time

import paho.mqtt.client as mqtt

from mqtt.test_base import HOST, PORT
from mqtt.test_base import MAC, TOPIC, DEVICE


def on_connect(client, userdata, flags, rc):
    print("on_connect", str(rc))


def on_message(client, userdata, msg):
    print('on_message', msg.topic, str(msg.payload))


def on_disconnect(client, userdata, rc):
    print("on_disconnect", str(rc))


client = mqtt.Client(client_id=f"{MAC}")
client.connect(HOST, PORT)
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.loop_start()

client.publish(TOPIC, DEVICE)

time.sleep(900)
# client.loop_stop()
# client.disconnect()
