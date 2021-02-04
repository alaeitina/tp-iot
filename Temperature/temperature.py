from machine import I2C

def get_temperature():
    i2c = I2C(0, pins=('P9','P10'))              # Instancie la connexion
    i2c.init(I2C.MASTER, baudrate=20000)         # Met la Pycom en position de maître pour la liaison avec le capteur
    val = i2c.readfrom(72, 2)                    # Effectue la lecture du capteur 
    val_str = str(val)                           # Converti le byte en chaine de caractère
    hex_val = val_str[4:6] + val_str[8:10]       # Extrait les 4 caractères qui donnent la mesure de température en hexa
    bin_val = bin(int(hex_val, 16))              # Convertion hexadémicale -> binaire

    temp_bin = bin_val[2:-4]                     # Découpe le LSB de la température en binaire
    temp_int = int(temp_bin, 2)                  # Convertion Binaire -> Décimale
    temp_degree = temp_int * 0.0625              # Mise à l'échelle de la température
    i2c.deinit()                                 # Etient le périphérique
    return temp_degree


temperature = get_temperature()
print("Temperature en degre: ",temperature)
