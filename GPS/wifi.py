import network
import time
import usocket as socket
import ssl
import uselect as select


# setup as a station
wlan = network.WLAN(mode=network.WLAN.STA)
wlan.connect('IloveIoT', auth=(network.WLAN.WPA2, 'PycharmCestMieux13!'))
print("Connexion en cours", end="")
while not wlan.isconnected():
    print(".", end="")
    time.sleep_ms(50)
print()
print("Connexion réussie")
print(wlan.ifconfig())
ip, *_ = wlan.ifconfig()
print(ip)

s = socket.socket()
#s.setblocking(False)
s.bind((ip, 8012))
s.listen()
s.accept()