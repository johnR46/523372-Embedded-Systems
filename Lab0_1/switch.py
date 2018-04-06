import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.IN,pull_up_down=GPIO.PUD_UP)
status = 0

while True :
	if(status == 0):
		GPIO.output(8,GPIO.HIGH)
		print("input  = HIGH")
	else:
		GPIO.output(8,GPIO.LOW)
		print("input = LOW")
	time.sleep(0.5)
	if(GPIO.input(10) == 0):
		time.sleep(0.1)
		status    = ~status

