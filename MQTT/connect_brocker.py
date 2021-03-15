from umqtt import MQTTClient
from machine import unique_id
import time

id_machine = unique_id()


# Publish test messages e.g. with:
# mosquitto_pub -t foo_topic -m hello

# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    print((topic, msg))

def main(server="185.216.25.143"):
    id_machine = unique_id()
    c = MQTTClient(id_machine, server)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"#")
    while True:
        if True:
            # Blocking wait for message
            c.wait_msg()
        else:
            # Non-blocking wait for message
            c.check_msg()
            # Then need to sleep to avoid 100% CPU usage (in a real
            # app other useful actions would be performed instead)
            time.sleep(1)

    c.disconnect()

if __name__ == "__main__":
    main()
