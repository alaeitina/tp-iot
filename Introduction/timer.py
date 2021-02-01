import machine
from machine import Timer
import time

chrono = Timer.Chrono()

adc = machine.ADC()             # create an ADC object
apin = adc.channel(pin='P13')   # create an analog pin on P16
apin = adc.channel(pin='P13', attn=machine.ADC.ATTN_11DB)

while True:
    print(val)
    val = apin()                    # read an analog value
    time.sleep(3)







chrono.start()
time.sleep(1.25) # simulate the first lap took 1.25 seconds
lap = chrono.read() # read elapsed time without stopping
time.sleep(1.5)
chrono.stop()
total = chrono.read()

print()
print("\nthe racer took %f seconds to finish the race" % total)
print("  %f seconds in the first lap" % lap)
print("  %f seconds in the last lap" % (total - lap))