import pycom
import machine
import math


def which_color(val):
    where = math.floor(val/(40996/9))
    print(where)
    return colors[where]

colors = [0x8a2be2, 0x0000ff, 0x6495ed, 0x00d4ff, 0x228b22, 0x32cd32, 0xffd400, 0xffa500, 0xff0000]

adc = machine.ADC()             # create an ADC object
#apin = adc.channel(pin='P13')   # create an analog pin on P16
apin = adc.channel(pin='P13', attn=machine.ADC.ATTN_11DB)
while True:
    pycom.heartbeat(False)  # disable the heartbeat LED
    #pycom.heartbeat()       # get the heartbeat state
    val = apin()                    # read an analog value
    pycom.rgbled(which_color(val))    # make the LED light up in green color
    print(val)

    time.sleep(1)