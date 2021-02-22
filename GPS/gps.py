from machine import I2C
import time


#Créer la fonction loop_read_msg() qui lit toutes les trames reçues à partir du
#$ jusqu’à \r\n
#- Exécuter loop_read_msg()
#è Créer la fonction loop_read_trame_GPGGA() qui sélectionne la trame GPGGA et
#extraire heure, Latitude, Longitude, Altitude.
#- Exécuter la fonction loop_read_trame_GPGGA()
#à Aller sur https://www.coordonnees-gps.fr et obtenir la position.
#- En se faisant localiser :
#- En utilisant les information GPS Pytrack :
#Autre trame : GPRMC voir doc Quectel
#è Créer la fonction loop_read_trame_GCRMC() qui sélectionne la trame GCRMC et
#extraire Latitude, Longitude, vitesse, date (11/03/20).
#- Exécuter la fonction loop_read_trame_GNRMC()
#è Créer la fonction loop_read_ dec _trame_ GPGGA() qui sélectionne la trame GPGGA
#et extrait Latitude, Longitude en degrés décimaux
#- Exécuter la fonction loop_read_ dec _trame_ GPGGA()

def read_byte():
    i2c = I2C(0, pins=('P22','P21'))
    a16 = i2c.readfrom(16, 255)
    return a16

def read_msg():
    a = read_byte()
    astr = str(a)[2:-1]
    liste = astr.split('\\r\\n$')[1:-1]
    return liste

def loop_read_trame_GPGGA():
    while True:
        msgs = read_msg()
        gpgga = [msg for msg in msgs if 'GPGGA' in msg]
        print(gpgga)
        if gpgga:
            paramsplit = gpgga[0].split(',')
            params = {}
            params['time'] = paramsplit[1][:2]+':'+paramsplit[1][2:4]+':'+paramsplit[1][4:6]
            if paramsplit[2] != '':
                params['latitude'] = paramsplit[2]+paramsplit[3]
                params['longitude'] = paramsplit[5]+paramsplit[6]
                params['altitude'] = paramsplit[9]
            print(params)
        time.sleep(10)

def loop_read_dec_trame_GPGGA():
    while True:
        msgs = read_msg()
        gpgga = [msg for msg in msgs if 'GPGGA' in msg]
        print(gpgga)
        if gpgga:
            paramsplit = gpgga[0].split(',')
            params = {}
            params['time'] = paramsplit[1][:2]+':'+paramsplit[1][2:4]+':'+paramsplit[1][4:6]
            if paramsplit[2] != '':
                params['latitude'] = float(paramsplit[2][:2])+float(paramsplit[2][2:])/60 * ((-1)*(paramsplit[3] == 'S'))
                params['longitude'] = float(paramsplit[5][:2])+float(paramsplit[5][2:])/60 * ((-1)*(paramsplit[6] == 'W'))
                params['altitude'] = float(paramsplit[9])
            print(params)
        time.sleep(10)

def loop_read_trame_GNRMC():
    while True:
        msgs = read_msg()
        gnrmc = [msg for msg in msgs if 'GNRMC' in msg]
        print(gnrmc)
        if gnrmc:
            paramsplit = gnrmc[0].split(',')
            params = {}
            params['time'] = paramsplit[1][:2]+':'+paramsplit[1][2:4]+':'+paramsplit[1][4:6]
            if paramsplit[2] != '':
                params['latitude'] = paramsplit[3]+paramsplit[4]
                params['longitude'] = paramsplit[5]+paramsplit[6]
                params['Vitesse'] = paramsplit[7]
                params['Date'] = paramsplit[9][:2]+'/'+paramsplit[9][2:4]+'/'+paramsplit[9][4:]
            print(params)
        time.sleep(10)


loop_read_trame_GPGGA()