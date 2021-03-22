import usocket
import _thread
import time
from network import WLAN
import pycom
import network
from TP6 import get_density, get_potentio

# Thread for handling a client
def client_thread(clientsocket):
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
        clientsocket.send(http + "<html><body><h1> Coucou </h1><br> Clique sur le lien pour accéder à la carte <br><a href='/map'>Carte</a><br></body></html>")

    elif "GET /dust" in str(r):
        # Envoie de la page web contenant la carte
        clientsocket.send(http + """<!DOCTYPE html>
<html>
	<head>
		<title>Particules</title>
		<link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/morris.js/0.5.1/morris.css">
	</head>
	<body>
		<div id="particules" style="height: 250px;"></div>

		<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js"></script>
		<script src="http://cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js"></script>
		<script src="http://cdnjs.cloudflare.com/ajax/libs/morris.js/0.5.1/morris.min.js"></script>
		<script type="text/javascript">

			memory = [
			]



			var linechart = new Morris.Line({
			  element: 'particules',
			  data: memory,
			  xkey: 'time',
			  ykeys: ['value'],
			  labels: ['Value']
			});

			$(document).ready(function(){
			function update_graph(){
				$.ajax({
					url:'/get_value',
					method:'GET',
					dataType:'text',
					async: true,
					success: function(data_txt){
						data = JSON.parse(data_txt.replaceAll("'", '"'))
						memory.push(data)
						if (memory.length > 180) {
							memory = memory.slice(1, memory.length)
						}
						linechart.setData(memory)
					},
				})
				setTimeout(() => { update_graph() }, 1000); // MAJ en temps réel du graph
			}
			update_graph()

			});

		</script>
		
	</body>
</html>""")

    elif "GET /get_value" in str(r):
        clientsocket.send("HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nAccess-Control-Allow-Origin: *\r\nConnection:close \r\n\r\n" + str({"time": time.time(), "value": get_density()}))

    elif "GET /test" in str(r):
        clientsocket.send(http + "<html><body><h1> Coucou </h1><br> Clique sur le lien pour accéder à la carte <br><a href='/map'>Carte</a><br></body></html>")

    elif "GET /TP6" in str(r):
        clientsocket.send(http + "<html><body><h1> Densité de particule </h1><br> Valeur :  " + str(get_density()))

    # Close the socket and terminate the thread
    clientsocket.close()
    time.sleep_ms(500)

time.sleep(1)

# setup as a station
wlan = network.WLAN(mode=network.WLAN.STA)
wlan.connect('IloveIoT', auth=(network.WLAN.WPA2, 'PycharmCestMieux13!'))
print("Connecting", end="")
while not wlan.isconnected():
    print(".", end="")
    time.sleep_ms(50)
print()
ip, *_ = wlan.ifconfig()
print(ip)

print("WiFi is up!")

# Set up server socket
serversocket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
serversocket.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
serversocket.bind((ip, 80))

# Accept maximum of 5 connections at the same time
serversocket.listen(5)
print("Webserver is up!")

# Unique data to send back
while True:
    # Accept the connection of the clients
    (clientsocket, address) = serversocket.accept()
    # Start a new thread to handle the client
    _thread.start_new_thread(client_thread, (clientsocket,))
serversocket.close()