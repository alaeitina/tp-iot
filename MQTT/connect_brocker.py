from umqtt import MQTTClient
from machine import unique_id
import time

id_machine = unique_id()
BROKER_ADDRESS="185.216.25.143"

# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    print((topic, msg))


id_machine = unique_id()
c = MQTTClient(id_machine, BROKER_ADDRESS)
c.set_callback(sub_cb)
c.connect()
c.subscribe(b"#")
while True:
    c.wait_msg()

c.disconnect()

