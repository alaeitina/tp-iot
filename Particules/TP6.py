"""
Ce script permet de faire changer la couleur de la LED à l'aide du potentiomètre
"""

import pycom
import machine
import math
import time

def potentio_to_particule(val):
    """
    Fonction permettant d'associer la valeur renvoyée par le potentiomètre à une couleur
    """
    where = math.floor(val*/(4096/n))
    return colors[where]


adc = machine.ADC()             # Création de l'objet ADC
apin = adc.channel(pin='P13', attn=machine.ADC.ATTN_11DB)
while True:
    pycom.heartbeat(False)  # Extinction de la lED
    val = apin()                    # Lecture de la valeur de tension du potentiomètre
    pycom.rgbled(which_color(val))    # Changement de la couleur de la LED