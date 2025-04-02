#Import necessary libraries
from machine import Pin, PWM
from time import sleep
import utime


frequency = 50
#Declaring and defining Pins for motor1
output_1= Pin(11, Pin.OUT)
output_2= Pin(12, Pin.OUT)
ENA=Pin(13, Pin.OUT)

#Declaring and defining Pins for motor2
output_3= Pin(6, Pin.OUT)
output_4= Pin(7, Pin.OUT)
ENB=Pin(5, Pin.OUT)


#Declaring and defining for servos
base_servo = PWM(Pin(2), freq=frequency)
arm_servo = PWM(Pin(4), freq=frequency)
mouth_servo = PWM(Pin(10), freq=frequency)

sensor_servo = PWM(Pin(3), freq=frequency) # For ultrasonic sensor servo

#Declaring and defining for ultrasonic sensor
trigger = Pin(0, Pin.OUT)
echo = Pin(1, Pin.IN)

max_servo = 6000
min_servo = 1702

   
   
def duty_cycle(speed):
    if speed <= 0 or speed > 100:
        duty_cycle = 0
    else:
        duty_cycle = int(min_servo + (max_servo - min_servo) * (speed / 100))
    return duty_cycle

# def move(in1, in2, speed_1 = 65535 , speed_2 = 65535):
def move(in1, in2, speed_1 = 65535 , speed_2 = 65535):
    output_1.value(in1)
    output_2.value(in2)
    ENA.value(1)
    #ENA.duty_u16(speed_1)
    output_3.value(in1)
    output_4.value(in2)
    ENB.value(1)
    #ENB.duty_u16(speed_2)
    
def ultrasonic():
    #all your sensing code will be here...
    #return
    trigger.low()
    utime.sleep_ms(2)
    trigger.high()
    utime.sleep_ms(5)
    trigger.low()
    while echo.value() == 0:
       signal_off = utime.ticks_us()
    while echo.value() == 1:
       signal_on = utime.ticks_us()
    time_passed = signal_on - signal_off
    distance = (time_passed * 0.0343) / 2
    print("The distance from object is ",distance,"cm")
    return distance
    

def pick():
    arm_servo.duty_u16(max_servo)
    sleep(2)
    mouth_servo.duty_u16(min_servo)
    sleep(2)
    arm_servo.duty_u16(min_servo)
    sleep(2)
    base_servo.duty_u16(max_servo)
    sleep(2)
    arm_servo.duty_u16(max_servo)
    sleep(2)
    mouth_servo.duty_u16(max_servo)
    sleep(2)
    
def sensor_sense():
    sensor_servo.duty_u16(max_servo)
    distance = ultrasonic()
    if distance > 5:
        move(1, 0)
    if distance < 5:
        move(0, 0)
        pick()
    sleep(2)
    sensor_servo.duty_u16(min_servo)
    
while True:
    # pick()
    sensor_sense()
    sleep(2)
        
