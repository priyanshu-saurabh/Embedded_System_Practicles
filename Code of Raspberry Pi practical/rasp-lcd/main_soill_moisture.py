

# import required modules
from machine import ADC, Pin, I2C
import utime
from machine import Pin,I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

import utime
 
# use variables instead of numbers:
soil = ADC(Pin(26)) # Soil moisture PIN reference
 
#Calibraton values
min_moisture=250
max_moisture=65300
 
readDelay = 0.5 # delay between readings
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)       # Init I2C using pins GP0 & GP1 
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config
 
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)                # Init oled display
 
while True:
    lcd.clear()
    lcd.move_to(0,0)
    # read moisture value and convert to percentage into the calibration range
    moisture = (max_moisture-soil.read_u16())*100/(max_moisture-min_moisture) 
    # print values
 
    lcd.putstr("Soil Moisture")
    lcd.move_to(0,1)
    print("moisture: " + "%.2f" % moisture +"% (adc: "+str(soil.read_u16())+")")
    lcd.putstr(str("%.2f" % moisture))
    print(str(soil.read_u16()))
#     lcd.putstr("% (adc: "+str(soil.read_u16())+")")
    utime.sleep(readDelay) # set a delay between readings    