from machine import I2C
import time

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
                params['latitude'] = float(paramsplit[2][:2])+float(paramsplit[2][2:])/60 * ((-1)*(paramsplit[3] == 'S'))
                params['longitude'] = float(paramsplit[5][:2])+float(paramsplit[5][2:])/60 * ((-1)*(paramsplit[3] == 'W'))
                params['altitude'] = float(paramsplit[9])
            print(params)
        time.sleep(10)


loop_read_trame_GPGGA()