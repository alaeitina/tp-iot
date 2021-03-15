from umqtt import MQTTClient

id_machine = unique_id()
BROKER_ADDRESS="185.216.25.143"

c = MQTTClient(id_machine, BROKER_ADDRESS)
c.connect()
c.publish(b"Mimoun", b"Mimoun est vraiment tres fort en informatique")
c.disconnect()

