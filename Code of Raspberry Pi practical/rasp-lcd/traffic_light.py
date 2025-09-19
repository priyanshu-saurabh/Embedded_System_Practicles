
from machine import Pin
from time import sleep
import tm1637
 
tm = tm1637.TM1637(clk=Pin(4), dio=Pin(5))
Led_R = Pin(15, Pin.OUT)
Led_Y = Pin(14, Pin.OUT)
Led_G = Pin(10, Pin.OUT)         
 
if __name__ == '__main__':
    while True:
        num = 5000
        Led_R.value(1)
        for i in range(5000):
            num=num-1
            tm.number(num)
            sleep(1)
            
        Led_R.value(0)
        for i in range(20):
            Led_Y.value(1)
            sleep(0.3)
            Led_Y.value(0)
            sleep(0.3)
        
        Led_G.value(1)
        sleep(10)
        Led_G.value(0)

