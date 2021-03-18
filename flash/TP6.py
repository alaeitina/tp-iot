"""
Ce script permet de récupérer la valeur de la densité de poussière
"""

import machine
import time

DENSITY_CHARACTERISTICS = {
    'density' : [0, 0.5, 0.52, 0.8],
    'voltage' : [0.6, 3.5, 3.6, 3.8]
}


def potentio_to_particule(val):
    """
    Fonction permettant de simuler le détecteur de particules
    """
    output_min_particule = 0.61
    output_max_particule = 3.7
    output_max_potentio = 4096
    return val * (output_max_particule - output_min_particule) / output_max_potentio + output_min_particule


def get_indices_of_neighbour(value, liste):
    """
    Cette fonction retourne les indices des valeurs qui encadrent la valeur choisie.
    """
    for item_id, item in enumerate(liste):
        if value <= item:
            return item_id - 1, item_id


def interpolation(x, x1, x2, y1, y2):
    """
    Cette fonction renvoie la valeur associée à x grâce à l'interpolation linéaire entre les points (x1, y1) et (x2, y2)
    """
    return y1 + ((x - x1) / (x2 - x1)) * (y2 - y1)


def get_density():
    adc = machine.ADC()             # Création de l'objet ADC
    apin = adc.channel(pin='P13', attn=machine.ADC.ATTN_11DB)
    val_potentio = apin()                      # Lecture de la valeur de tension du potentiomètre à changer plus tard par celle du filtre à particule
    voltage = potentio_to_particule(val_potentio)

    #Récupération des indices correspondant à l'intervalle dans lequel est contenu la tension du capteur
    indinf, indsup = get_indices_of_neighbour(voltage, DENSITY_CHARACTERISTICS['voltage'])
    
    #Renvoie la valeur du pourcentage de l'humidite issue de l'interpolation entre les valeur de tension
    density = interpolation(voltage, DENSITY_CHARACTERISTICS['voltage'][indinf], DENSITY_CHARACTERISTICS['voltage'][indsup], 
                            DENSITY_CHARACTERISTICS['density'][indinf], DENSITY_CHARACTERISTICS['density'][indsup])

    density_str = "{:10.2f}".format(density * 100) + "%"
    print(density_str)
    return density * 100
    