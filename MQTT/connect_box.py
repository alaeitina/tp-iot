import network
import time
import env


# setup as a station
wlan = network.WLAN(mode=network.WLAN.STA)
wlan.connect(env.NET_SSID, auth=(network.WLAN.WPA2, env.NET_PASS))
while not wlan.isconnected():
    time.sleep_ms(50)
print(wlan.ifconfig())