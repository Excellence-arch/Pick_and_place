from machine import PWM, Pin
from time import sleep

def setup_servo(pin_num):
    pwm = PWM(Pin(pin_num))
    pwm.freq(50)
    return pwm

mouthServo = setup_servo(0)
neck1Servo = setup_servo(1)
neck2Servo = setup_servo(2)
elbowServo = setup_servo(3)
shoulderServo = setup_servo(4)
baseServo = setup_servo(5)

SERVO_MIN = 2000   # ~0°
SERVO_MAX = 8000   # ~180°
SERVO_MID = (SERVO_MIN + SERVO_MAX) // 2

def move_smoothly(servo, start, end, step=100, delay=0.02):
    if start < end:
        for duty in range(start, end, step):
            servo.duty_u16(duty)
            sleep(delay)
    else:
        for duty in range(start, end, -step):
            servo.duty_u16(duty)
            sleep(delay)
    servo.duty_u16(end)

def pick_and_place():
    print("Rotating to object...")
    move_smoothly(baseServo, SERVO_MID, SERVO_MIN)
    sleep(1)

    print("Lowering arm...")
    move_smoothly(shoulderServo, SERVO_MIN, SERVO_MID)
    move_smoothly(elbowServo, SERVO_MAX, SERVO_MIN)
    sleep(1)

    print("Opening mouth...")
    move_smoothly(mouthServo, SERVO_MIN, SERVO_MAX)
    sleep(0.5)

    print("Closing mouth to grab...")
    move_smoothly(mouthServo, SERVO_MAX, SERVO_MIN)
    sleep(0.5)

    print("Lifting object...")
    move_smoothly(elbowServo, SERVO_MIN, SERVO_MAX)
    sleep(1)

    print("Rotating to drop location...")
    move_smoothly(baseServo, SERVO_MIN, SERVO_MAX)
    sleep(1)

    print("Dropping object...")
    move_smoothly(mouthServo, SERVO_MIN, SERVO_MAX)
    sleep(0.5)

    print("Resetting arm...")
    move_smoothly(shoulderServo, SERVO_MID, SERVO_MIN)
    move_smoothly(baseServo, SERVO_MAX, SERVO_MID)
    move_smoothly(mouthServo, SERVO_MAX, SERVO_MIN)

while True:
    pick_and_place()
    sleep(5)
