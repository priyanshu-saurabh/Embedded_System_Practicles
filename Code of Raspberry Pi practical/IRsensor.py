import machine
import utime
reed = machine.Pin(0, machine.Pin.IN)
led = machine.Pin(16, machine.Pin.OUT)
while True:
 if reed.value() == 0:
  led.value(1)
  print("IR Sensor Detected!")
  utime.sleep(0.01)
  led.value(0)
