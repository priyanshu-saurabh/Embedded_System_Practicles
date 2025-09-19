import machine
import time
pin28 = machine.Pin(28, machine.Pin.OUT)
pin25 = machine.Pin(25, machine.Pin.OUT)
pin8 = machine.Pin(8, machine.Pin.OUT)
pin7 = machine.Pin(7, machine.Pin.OUT)
while True:
   pin7.on()
   time.sleep(1)
   pin7.off()
   pin25.on()
   time.sleep(0.1)
   pin25.off()
   time.sleep(0.1)

   
   
   
  
     
     

