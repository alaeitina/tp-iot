import pycom

pycom.heartbeat(False)  # disable the heartbeat LED
#pycom.heartbeat(True)   # enable the heartbeat LED
pycom.heartbeat()       # get the heartbeat state
pycom.rgbled(0xff00)    # make the LED light up in green color