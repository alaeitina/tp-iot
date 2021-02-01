# Rapport TP1

#### Variation de la couleur de la LED de la pycom selon la valeur de la tension renvoyée par le potentiomètre

### 1. Réalisation d’un script permettant de générer les couleurs du gradient.

Lien du code : https://github.com/t-alaei/tp-iot/blob/main/Gradient/generate_color_gradient.py

À l’aide du module _Color_ de _Python_, on construit une liste de couleurs qui vont composer le gradient. Les couleurs consécutives sont suffisamment proche l’une de l’autre pour que le changement de couleur soit fluide.

**Fonctionnement :** On part de la liste des couleurs initialement utilisées, qui seront les couleurs par lesquelles le gradient va passer. Pour chaque paire de couleurs consécutives, on génère 98 couleurs intermédiaires. Finalement, on obtient une liste de 496 couleurs.

**Note :** Le module _Color_ n’est pas disponible sur MicroPython, il faut donc l'exécuter au préalable sur Python. Pour le faire fonctionner, il faut installer le module Color avec l'instruction:
```pip install Color```.


### 2. Réalisation d’un script permettant de changer la couleur de la LED de la pycom.

Lien du code : https://github.com/t-alaei/tp-iot/blob/main/Gradient/colors.py

On copie-colle la liste des couleurs du gradient générée précédemment. On écrit la fonction ```which_color```, qui a une tension associe une couleur dans cette liste.

On prépare la lecture de la valeur sur le pin 13, puis on crée une boucle qui va changer la couleur de la LED à chaque nouvelle valeur acquise.
