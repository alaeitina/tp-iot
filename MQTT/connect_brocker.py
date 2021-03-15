import flash.umqtt as umqtt
from machine import unique_id

id_machine = unique_id()
client = MQTTClient(id_machine, )
