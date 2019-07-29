# coding=utf-8

import paho.mqtt.client as mqtt
import time

HOST = "192.168.0.103"
PORT = 1883

client_id = 'test_id1'
user = ''
pwd = ''



def client_loop():
    # client_id = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    client = mqtt.Client(client_id)
    client.username_pw_set(user, pwd)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 60)
    client.loop_forever()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("test")


def on_message(client, userdata, msg):
    print(msg.topic + " " + msg.payload.decode("utf-8"))


if __name__ == '__main__':
    client_loop()
