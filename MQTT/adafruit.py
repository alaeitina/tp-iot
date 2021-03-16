from umqtt import MQTTClient
from machine import unique_id
import time
import socket

id_machine = unique_id()
BROKER_ADDRESS="https://io.adafruit.com/"

print(socket.dnsserver())


id_machine = unique_id()
c = MQTTClient(id_machine, BROKER_ADDRESS, user="talaei", password="aio_gqKQ78A0bhAETrixvkH7T6LIzxH9")
c.connect()
c.publish(b"temp", b"1")
c.disconnect()