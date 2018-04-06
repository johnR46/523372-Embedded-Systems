import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.IN)
status = 0


while True :
    if(GPIO.input (10) == 1):
            GPIO.output(8,GPIO.HIGH)
            print("Input = HIGH")
	    print(time.time())
    else:
        GPIO.output(8,GPIO.LOW)
        print("Input = LOW")
    
    
