from machine import Pin, Timer

led = Pin(25, Pin.OUT)
LED_state = True
tim = Timer()

def tick(timer):
    global led, LED_state
    LED_state = notLED state
    led.value(LEd_state)
    
    
tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)