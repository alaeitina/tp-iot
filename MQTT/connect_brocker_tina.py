from umqtt import MQTTClient
from machine import unique_id

id_machine = unique_id()
BROKER_ADDRESS = '185.216.25.143'
client = MQTTClient(id_machine, BROKER_ADDRESS, 1883)
client.connect()
client.publish(b"Mimoun", b"Mimoun est vraiment pas sympa")
client.disconnect()