from .temperature import get_temperature

values = [
    [0.76, 0.73, 0.70, 0.67, 0.63, 0.60, 0.56],
    [1.06, 1.03, 1.03, 1.02, 0.99, 0.96, 0.93],
    [1.36, 1.34, 1.35, 1.36, 1.34, 1.32, 1.29],
    [1.67, 1.66, 1.67, 1.68, 1.67, 1.66, 1.64],
    [1.97, 1.97, 1.98, 1.98, 1.98, 1.98, 1.96],
    [2.25, 2.25, 2.26, 2.26, 2.26, 2.26, 2.25],
    [2.51, 2.51, 2.50, 2.51, 2.50, 2.50, 2.48],
    [2.73, 2.72, 2.70, 2.73, 2.70, 2.68, 2.66]
]  # Tableau de valeur issu de la documentation

abscisses = [10, 15, 20, 25, 30, 35, 40]  # Liste des températures associées
ordonnees = [20 + 10*k for k in range(8)]  # Liste des pourcentages d'humidité associé

def get_indices_of_neighbour(value, liste):
    """
    Cette fonction retourne les indices des valeurs qui encadrent la valeur choisie.
    """
    for item_id, item in enumerate(liste):
        if value >= item:
            return item_id, item_id + 1


def interpolation(x, x1, x2, y1, y2):
    """
    Cette fonction renvoie la valeur associée à x grâce à l'interpolation linéaire entre les points (x1, y1) et (x2, y2)
    """
    return y1 + ((x - x1) / (x2 - x1)) * (y2 - y1)


def get_colonne(indinf, indsup, temperature):
    """
    Cette fonction retourne la colonne issue de l'interpolation entre chaque valeur de tension pour les valeurs de températures associées
    """
    newcol = []
    valinf = [values[k][indinf] for k in range(len(values))]
    valsup = [values[k][indsup] for k in range(len(values))]

    for i in range(len(valinf)):
        newcol.append(interpolation(temperature, abscisses[indinf], abscisses[indsup], valinf[i], valsup[i]))

    return newcol


def get_humidite(temperature, tension):
    """
    Cette fonction renvoie une liste associant le pourcentage d'humidité aux valeur de tension du capteur.
    Cette liste est crée en faisant une interpolation linéaire entre les listes des deux températures les plus proches
    """

    #Récupération des indices correspondant à l'intervalle (dans abscisses) dans lequel est contenu la température
    indinftemp, indsuptemp = get_indices_of_neighbour(temperature, abscisses)

    #Génération de la colonne des tensions correspondant à la température récupérée (via l'interpolation)
    newcol = get_colonne(indinftemp, indsuptemp, temperature)

    #Récupération des indices correspondant à l'intervalle (dans newcol) dans lequel est contenu la tension
    indinftens, indsuptens = get_indices_of_neighbour(tension, newcol)

    #Renvoie la valeur du pourcentage de l'humidite issue de l'interpolation entre les valeur de tension
    return interpolation(tension, newcol[indinftens], newcol[indsuptens], ordonnees[indinftens], ordonnees[indsuptens])


temperature = 12 #get_temperature()

tension = 1.92 #Récupérer ici la valeur de la tension

print(get_humidite(temperature, tension))