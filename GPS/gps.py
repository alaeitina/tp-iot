from machine import I2C

i2c = I2C(0, pins=('P22','P21'))
print(i2c.scan())

a8 = i2c.readfrom(8, 255)
a16 = i2c.readfrom(16, 255)
a30 = i2c.readfrom(30, 255)

print(str(a16))