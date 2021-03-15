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
    
    client.connect()
    a = str(which_value(val))
    client.publish(b"temp", bytes(a, 'utf-8'))
    client.disconnect()
