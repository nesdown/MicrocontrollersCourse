from machine import Pin
from machine import PWM
import time

# Set our pin 2 to PWM
pwm = PWM(Pin(2))

# Frequency = 100hz
pwm.freq(100)

while 1:
  # Brightness between 0 and 1023
  for brightness in range (0, 1023, 100):
    pwm.duty(brightness)
    print(brightness)
    time.sleep(0.1)

  # Brightness between 1023 and 0
  for brightness in range (1023, 0, -100):
    pwm.duty(brightness)
    print(brightness)
    time.sleep(0.1)