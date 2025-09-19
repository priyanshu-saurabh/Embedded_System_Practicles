from machine import Pin
import time
import dht 
dSensor = dht.DHT22(Pin(2))
def readDHT():
 try:
  dSensor.measure()
  temp = dSensor.temperature()
  temp_f = (temp * (9/5)) + 32.0
  hum = dSensor.humidity()
  print('Temperature= {} C, {} F'.format(temp, temp_f))
  print('Humidity= {} '.format(hum))
 except OSError as e:
  print('Failed to read data from DHT sensor')
 
while True:
 readDHT()
 time.sleep(2)
