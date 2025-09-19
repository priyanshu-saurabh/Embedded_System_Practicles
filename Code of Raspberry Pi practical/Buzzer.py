from machine import Pin
import time
button = Pin(0, Pin.IN, Pin.PULL_UP)
buzzer = Pin(11, Pin.OUT)
while True:
 if button.value() == 0:
  print("button pressed")
  buzzer.value(1)
  time.sleep(1)
 else:
  buzzer.value(0)