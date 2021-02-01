import machine
import time

adc = machine.ADC()             # create an ADC object
apin = adc.channel(pin='P13')   # create an analog pin on P16
apin = adc.channel(pin='P13', attn=machine.ADC.ATTN_11DB)

while True:
    print(val)
    val = apin()                    # read an analog value
    time.sleep(3)