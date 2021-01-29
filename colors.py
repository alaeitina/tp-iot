import pycom
import machine
import math
import time

colors = [0x8a2be2,  0x7e27e4,  0x7324e7,  0x6820e9,  0x5c1dec,  0x5119ee,  0x4515f1, 0x0000ff,  0x2a3ef7,  0x324bf6,  0x3a57f4,  0x4363f3,  0x4b70f1,  0x537cf0,  0x5c89ee,  0x6495ed, 0x6495ed,  0x5c9aee,  0x53a0f0,  0x4ba5f1,  0x43aaf3,  0x32b4f6,  0x21bff9,  0x11cafc, 0x00d4ff,  0x06c8da,  0x0bbcb5,  0x11b091,  0x17a36c,  0x1c9747, 0x228b22,  0x259625,  0x27a127,  0x2aac2a,  0x2db72d,  0x2fc22f, 0x32cd32,  0x76cf21,  0x98d119,  0xbbd211,  0xddd308, 0xffd400,  0xffc400,  0xffbd00,  0xffb500,  0xffad00,  0xffa500,  0xff9700,  0xff8a00,  0xff7c00,  0xff6e00,  0xff6000,  0xff5200,  0xff4500,  0xff3700,  0xff0000]
n = len(colors)
print(n)

def which_color(val):
    where = math.floor(val/(4096/n))
    return colors[where]


adc = machine.ADC()             # create an ADC object
#apin = adc.channel(pin='P13')   # create an analog pin on P16
apin = adc.channel(pin='P13', attn=machine.ADC.ATTN_11DB)
while True:
    pycom.heartbeat(False)  # disable the heartbeat LED
    #pycom.heartbeat()       # get the heartbeat state
    val = apin()                    # read an analog value
    pycom.rgbled(which_color(val))    # make the LED light up in green color
    #print(val)

    #time.sleep(1)