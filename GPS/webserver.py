import usocket
import _thread
import time
from network import WLAN
import pycom
import network
from machine import I2C


availablecolor = 0x001100
connectioncolor = 0x110000

def read_byte():
    i2c = I2C(0, pins=('P22','P21'))
    a16 = i2c.readfrom(16, 255)
    return a16

def read_msg():
    a = read_byte()
    astr = str(a)[2:-1]
    liste = astr.split('\\r\\n$')[1:-1]
    return liste

def loop_read_dec_trame_GPGGA():
    while True:
        msgs = read_msg()
        gpgga = [msg for msg in msgs if 'GPGGA' in msg]
        if gpgga:
            paramsplit = gpgga[0].split(',')
            params = {}
            params['time'] = paramsplit[1][:2]+':'+paramsplit[1][2:4]+':'+paramsplit[1][4:6]
            if paramsplit[2] != '':
                params['latitude'] = float(paramsplit[2][:2])+float(paramsplit[2][2:])/60 * ((-1)*(paramsplit[3] == 'S'))
                params['longitude'] = float(paramsplit[5][:2])+float(paramsplit[5][2:])/60 * ((-1)*(paramsplit[3] == 'W'))
                params['altitude'] = float(paramsplit[9])
            return params

# Thread for handling a client
def client_thread(clientsocket,n):
    # Receive maxium of 12 bytes from the client
    r = clientsocket.recv(4096)

    # If recv() returns with 0 the other end closed the connection
    if len(r) == 0:
        clientsocket.close()
        return
    else:
        # Do something wth the received data...
        print("Received: {}".format(str(r))) #uncomment this line to view the HTTP request

    http = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection:close \r\n\r\n" #HTTP response
    
    if "GET / " in str(r):
        #this is a get response for the page   
        # Sends back some data
        clientsocket.send(http + "<html><body><h1> You are connection "+ str(n) + "</h1><br> Your browser will send multiple requests <br> <a href='/hello'> hello!</a><br><a href='/color'>change led color!</a></body></html>")
    elif "GET /hello "in str(r):
        
        clientsocket.send(http + "<html><body><h1> Hello to you too! </h1><br> <a href='/'> go back </a></body></html>")
    elif "GET /color" in str(r):
        pycom.rgbled(0xFFFFFF)
        clientsocket.send(http + "<html><body><h1> You are connection "+ str(n) + "</h1><br> Your browser will send multiple requests <br> <a href='/hello'> hello!</a><br><a href='/color'>change led color!</a></body></html>")
    elif "GET /map" in str(r):
        params = loop_read_trame_GPGGA()
        if not(params.get('latitude')):
            params['latitude'] = 43.2907194
            params['longitude'] = 5.3620492
        clientsocket.send(http + """
        <!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <!-- Nous chargeons les fichiers CDN de Leaflet. Le CSS AVANT le JS -->
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.3.1/dist/leaflet.css" integrity="sha512-Rksm5RenBEKSKFjgI3a41vrjkw4EVPlJ3+OiI65vTjIdo9brlAacEuKOiQ5OFh7cOI1bkDwLqdLw3Zg0cRJAAQ==" crossorigin="" />
        <style type="text/css">
            #map{ /* la carte DOIT avoir une hauteur sinon elle n'apparaît pas */
                height:1000px;
            }
        </style>
        <title>Carte</title>
    </head>
    <body>
        <div id="map">
	    <!-- Ici s'affichera la carte -->
	</div>

        <!-- Fichiers Javascript -->
        <script src="https://unpkg.com/leaflet@1.3.1/dist/leaflet.js" integrity="sha512-/Nsx9X4HebavoBvEBuyp3I7od5tA0UzAxs+j83KgC8PU0kgB4XiK4Lfe4y4cgBtaRJQEIFCW+oC506aPT2L1zw==" crossorigin=""></script>
	<script type="text/javascript">
            // On initialise la latitude et la longitude de Paris (centre de la carte)
            var lat = """+str(params['latitude'])+""";
            var lon = """+str(params['longitude'])+""";
            var macarte = null;
            // Fonction d'initialisation de la carte
            function initMap() {
                // Créer l'objet "macarte" et l'insèrer dans l'élément HTML qui a l'ID "map"
                macarte = L.map('map').setView([lat, lon], 15);
                // Leaflet ne récupère pas les cartes (tiles) sur un serveur par défaut. Nous devons lui préciser où nous souhaitons les récupérer. Ici, openstreetmap.fr
                L.tileLayer('https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png', {
                    // Il est toujours bien de laisser le lien vers la source des données
                    attribution: 'données © <a href="//osm.org/copyright">OpenStreetMap</a>/ODbL - rendu <a href="//openstreetmap.fr">OSM France</a>',
                    minZoom: 1,
                    maxZoom: 20
                }).addTo(macarte);
                // Nous ajoutons un marqueur
                var marker = L.marker([lat, lon]).addTo(macarte);
            }
            window.onload = function(){
		// Fonction d'initialisation qui s'exécute lorsque le DOM est chargé
		initMap(); 
            };
        </script>
    </body>
</html>""")
    # Close the socket and terminate the thread

    clientsocket.close()
    pycom.rgbled(connectioncolor)
    time.sleep_ms(500)
    pycom.rgbled(availablecolor)  

time.sleep(1)

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

print("WiFi is up!")
time.sleep(1)
pycom.heartbeat(False)
pycom.rgbled(availablecolor)

# Set up server socket
serversocket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
serversocket.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
serversocket.bind((ip, 80))

# Accept maximum of 5 connections at the same time
serversocket.listen(5)

# Unique data to send back
c = 1
while True:
    # Accept the connection of the clients
    (clientsocket, address) = serversocket.accept()
    # Start a new thread to handle the client
    _thread.start_new_thread(client_thread, (clientsocket, c))
    c = c+1
serversocket.close()