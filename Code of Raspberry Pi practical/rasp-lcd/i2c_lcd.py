from machine import Pin,ADC,PWM,I2C
from i2c_lcd import I2cLcd    
from time import sleep
 
DEFAULT_I2C_ADDR = 0x27     # LCD 1602 I2C address
Flame_AO = ADC(0)           # ADC0 multiplexing pin is GP26
 
 
Led_R = PWM(Pin(4))
Led_G = PWM(Pin(3))
Led_B = PWM(Pin(2))
Led_R.freq(2000)            # Set the frequency to 2KHz
Led_G.freq(2000)   
Led_B.freq(2000)   
 
i2c = I2C(0,sda=Pin(0),scl=Pin(1),freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)          # Initialize(device address, cursor settings)
 
if __name__ == '__main__':
    while True:
        text = 'Warning!\nBe On Fire!'              # show alert information                   
        Flame_value = Flame_AO.read_u16()           # Get the analog value of the flame sensor
        if Flame_value < 30000:
            lcd.putstr(text)
            Led_R.duty_u16(65535)
            Led_G.duty_u16(0)
            Led_B.duty_u16(0)
            sleep(0.5)
            lcd.clear()
            Led_R.duty_u16(0)
            Led_G.duty_u16(0)
            Led_B.duty_u16(65535)
            sleep(0.5)
        else:
            Led_R.duty_u16(0)
            Led_G.duty_u16(65535)
            Led_B.duty_u16(0)