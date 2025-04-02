from machine import PWM, Pin
from time import sleep

mouthPin = machine.Pin(0)
mouth = PWM(mouthPin)

# Set Duty Cycle for Different Angles
max_duty = 8064
maxx_duty=3000
min_duty = 1702
half_duty = int(max_duty/2)
halff_duty = int(maxx_duty/2)

#Set PWM frequency
frequency = 50
mouth.freq(frequency)

while True:
    mouth.duty_u16(max_duty)
    sleep(2)
    mouth.duty_u16(maxx_duty)
    sleep(2)
      
      

