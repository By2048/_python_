import time

import paho.mqtt.client as mqtt

unacked_sub = []  # 未获得服务器响应的订阅消息 id 列表


def on_connect(client, userdata, flags, rc):
    print("Connection returned with result code:" + str(rc))


def on_message(client, userdata, msg):
    print("Received message, topic:" + msg.topic + "payload:" + str(msg.payload))


def on_disconnect(client, userdata, rc):
    print("Disconnection returned result:" + str(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    unacked_sub.remove(mid)


client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.connect("s50.53iq.com", 1883, 60)
client.loop_start()

# 订阅单个主题
result, mid = client.subscribe("hello", 0)
unacked_sub.append(mid)
# 订阅多个主题
result, mid = client.subscribe([("temperature", 0), ("humidity", 0)])
unacked_sub.append(mid)

while len(unacked_sub) != 0:
    time.sleep(1)

client.publish("hello", payload="Hello world!")
client.publish("temperature", payload="24.0")
client.publish("humidity", payload="65%")

# 断开连接
time.sleep(5)  # 等待消息处理结束

client.loop_stop()
client.disconnect()
