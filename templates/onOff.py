import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)


if(GPIO.input(18) == 1):GPIO.output(18, False) 
else: GPIO.output(18, True) 

