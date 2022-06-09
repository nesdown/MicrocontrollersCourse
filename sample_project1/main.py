from machine import Pin
from machine import PWM
import time

# Set our pin 2 to PWM
pwm = PWM(Pin(2))

# Brightness between 0 and 1023
pwm.duty(1023)

# Frequency in Hertz
while true:
  pwm.freq(1)