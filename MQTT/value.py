"""
Ce script permet de faire changer la couleur de la LED à l'aide du potentiomètre
"""

import pycom
import machine
import math
import time
from umqtt import MQTTClient

n=40

id_machine = machine.unique_id()
BROKER_ADDRESS = '185.216.25.143'
client = MQTTClient(id_machine, BROKER_ADDRESS, 1883)

colors = [8388736,8257680,7864480,7209136,6291647,5112015,3670239,1966319,255,8447,16639,24831,32767,40959,49151,57343,65535,61393,57255,53122,48992,45122,41000,36882,32768,1216512,2662400,4370432,6340352,8572672,11001600,13758208,16776960,16768768,16760576,16752384,16744192,16736256,16728064,16719872,16711680]

n_colors = len(colors)
print("Nombre de couleurs dans le gradient: ", n_colors)

def which_value(val):
    """
    Fonction permettant d'associer la valeur renvoyée par le potentiomètre à une couleur
    """
    where = math.floor(val/(4096/n))
    return where


adc = machine.ADC()             # Création de l'objet ADC
apin = adc.channel(pin='P13', attn=machine.ADC.ATTN_11DB)
while True:
    pycom.heartbeat(False)  # Extinction de la lED
    val = apin()                    # Lecture de la valeur de tension du potentiomètre
    pycom.rgbled(which_color(val))    # Changement de la couleur de la LED

    client.connect()
    a = str(which_value(val))
    client.publish(b"temp", bytes(a, 'utf-8'))
    client.disconnect()
