values = [
    [0.76, 0.73, 0.70, 0.67, 0.63, 0.60, 0.56],
    [1.06, 1.03, 1.03, 1.02, 0.99, 0.96, 0.93],
    [1.36, 1.34, 1.35, 1.36, 1.34, 1.32, 1.29],
    [1.67, 1.66, 1.67, 1.68, 1.67, 1.66, 1.64],
    [1.97, 1.97, 1.98, 1.98, 1.98, 1.98, 1.96],
    [2.25, 2.25, 2.26, 2.26, 2.26, 2.26, 2.25],
    [2.51, 2.51, 2.50, 2.51, 2.50, 2.50, 2.48],
    [2.73, 2.72, 2.70, 2.73, 2.70, 2.68, 2.66]
]  # Tableau de valeur issu de la docuumentation

abscisses = [10, 15, 20, 25, 30, 35, 40]  # Liste des températures associées
ordonnees = [20 + 10*k for k in range(8)]  # Liste des pourcentages d'humidité associé


def get_colonne(temperature):
    """
    Cette fonction renvoie une liste associant le pourcentage d'humidité aux valeur de tension du capteur.
    Cette liste est crée en faisant une interpolation linéaire entre les listes des deux températures les plus proches
    """
    pass