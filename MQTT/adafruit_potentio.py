from umqtt import MQTTClient
import machine
import time
import math
import pycom
import env

id_machine = machine.unique_id()
BROKER_ADDRESS="io.adafruit.com"
user = env.ADA_USER
password = env.ADA_PASSWORD
topic_temp = user +"/f/temp"
topic_switch = user + "/f/switch"
topic_potentio = user + "/f/potentio"


print(socket.dnsserver())

n=40
def which_value(val):
    """
    Fonction permettant d'associer la valeur renvoyée par le potentiomètre à une couleur
    """
    where = math.floor(val/(4096/n))
    return where

def sub_cb(topic, msg):

    pycom.heartbeat(False)

    #Renvoie la couleur vert si "ON"
    if msg == b"ON":
        pycom.rgbled(0x00ff00)
    
    #Renvoie la couleur rouge si "OFF"
    if msg == b"OFF":
        pycom.rgbled(0xff0000)

    print((topic, msg))


client = MQTTClient(id_machine, BROKER_ADDRESS, 1883, user, password)

#Extinction de la led de pycom
pycom.heartbeat(False)

#Connexion au pin pour la recuperation de la valeur du potentio
adc = machine.ADC()
apin = adc.channel(pin='P13', attn=machine.ADC.ATTN_11DB)

client.set_callback(sub_cb)
client.connect()

#Souscrit au topic switch
client.subscribe(topic_switch)

while True:
    #Verifie si il y a un message en attente si oui -> callback
    client.check_msg()

    #Recup et publication de la valeur du potentio
    val = apin()
    a = str(which_value(val))

    #publication de la valeur du potentio
    client.publish(topic_potentio, bytes(a, 'utf-8'))

    time.sleep(3)

client.disconnect()