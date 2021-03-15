import network
import time


# setup as a station
wlan = network.WLAN(mode=network.WLAN.STA)
wlan.connect('IloveIoT', auth=(network.WLAN.WPA2, 'PycharmCestMieux13!'))
while not wlan.isconnected():
    time.sleep_ms(50)
print(wlan.ifconfig())