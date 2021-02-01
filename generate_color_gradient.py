"""
Script permettant de générer un gradient de couleur. A ne pas executer sur micropython
Pour le faire fonctionner, il faut installer le module Color avec l'instruction:
pip install Color
"""

from colour import Color
import ujson

if __name__ == '__main__':
    color_list = [
        Color("purple"),
        Color("blue"),
        Color("cyan"),
        Color("green"),
        Color("yellow"),
        Color("red")
    ]  # Liste des couleurs par lesquelles il faut passer
    gradient = []  # Liste des couleurs qui vont faire le gradient
    n = len(color_list)
    for i in range(1, n):
        c1 = color_list[i - 1]
        c2 = color_list[i]
        gradient.extend(list(c1.range_to(c2, 100))[:-1])  # Génération des 100 couleurs intermédiaires
    gradient.append(color_list[-1])
    gradient_int = list(map(lambda color: int(color.get_hex_l()[1:], 16), gradient))  # Conversion des couleurs en nombre entiers
    with open("colors.json", "w") as outfile:  # Enregistrement du gradient de couleurs
        ujson.dump(gradient_int, outfile)
