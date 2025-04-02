from machine import PWM, Pin
from time import sleep

mouthPin = machine.Pin(0)
neck1Pin = machine.Pin(1)
neck2Pin = machine.Pin(2)
elbowPin = machine.Pin(3)
shoulderPin = machine.Pin(4)
basePin = machine.Pin(5)

mouth = PWM(mouthPin)
neck1 = PWM(neck1Pin)
neck2 = PWM(neck2Pin)
elbow = PWM(elbowPin)
shoulder = PWM(shoulderPin)
base = PWM(basePin)

# Set Duty Cycle for Different Angles
max_duty = 8064
maxx_duty = 3000
min_duty = 1702
half_duty = int(max_duty / 2)
halff_duty = int(maxx_duty / 2)

# Set PWM frequency
frequency = 50
mouth.freq(frequency)
neck1.freq(frequency)
neck2.freq(frequency)
elbow.freq(frequency)
shoulder.freq(frequency)
base.freq(frequency)


def move_smoothly(pin, start_duty, end_duty, step=100, delay=0.05):
    """Move smoothly from start_duty to end_duty."""
    if start_duty < end_duty:
        for duty in range(start_duty, end_duty, step):
            pin.duty_u16(duty)
            sleep(delay)
    else:
        for duty in range(start_duty, end_duty, -step):
            pin.duty_u16(duty)
            sleep(delay)
            
#move_smoothly(shoulder, min_duty, maxx_duty)
#sleep(2)

while True:
    #Move to where the object is
    move_smoothly(base, min_duty, max_duty)
    sleep(2)
    '''move_smoothly(shoulder, min_duty, maxx_duty)
    sleep(2)'''
    #open the mouth to pick the object
    move_smoothly(mouth, min_duty, half_duty)
    sleep(2)
    #bring the elbow down to the height of the object
    move_smoothly(elbow, maxx_duty, min_duty)
    sleep(2)
    #Close the mouth to pick the object
    move_smoothly(mouth, half_duty, min_duty)
    sleep(2)
    #Raise the elbow back to carry the object
    move_smoothly(elbow, min_duty, maxx_duty)
    sleep(2)
    '''move_smoothly(shoulder, half_duty, min_duty)
    sleep(2)'''
    #Rotate to where to drop the object
    move_smoothly(base, max_duty, min_duty)
    sleep(2)
    #open the mouth to drop the object
    move_smoothly(mouth, min_duty, half_duty)
    sleep(2)
    #Close the mouth to after picking the object
    move_smoothly(mouth, half_duty, min_duty)
    sleep(2)
    
    
    """ move_smoothly(mouth, min_duty, maxx_duty)
    sleep(2)
    move_smoothly(mouth, maxx_duty, min_duty)
    sleep(2)
    
    move_smoothly(neck1, maxx_duty, min_duty)
    sleep(2)
    move_smoothly(neck1, min_duty, maxx_duty)
    sleep(2)
    
    move_smoothly(neck2, max_duty, min_duty)
    sleep(2)
    move_smoothly(neck2, min_duty, max_duty)
    sleep(2)
    
    move_smoothly(elbow, maxx_duty, min_duty)
    sleep(2)
    move_smoothly(elbow, min_duty, maxx_duty)
    sleep(2)
    
    move_smoothly(shoulder, min_duty, halff_duty)
    sleep(2)
    move_smoothly(shoulder, halff_duty, min_duty)
    sleep(2)
    
    move_smoothly(base, min_duty, half_duty)
    sleep(2)
    move_smoothly(base, half_duty, min_duty)
    sleep(2) """

