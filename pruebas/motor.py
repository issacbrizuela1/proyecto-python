import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 16#GPIO 23-13|pin 16 nueba ubicasion pasa al pin 29 L293d pin 7
Motor1B = 18#GPIO 24-26|pin 18 nueba ubicasion pasa al pin 37 L293d pin 2
Motor1E = 22#GPIO 25-19|pin 22 nueba ubicasion pasa al pin 31 L293d pin 1
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
print ("Going forwards")
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
 
sleep(2)
 
print ("Going backwards")
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)
 
sleep(2)
 
print ("Now stop")
GPIO.output(Motor1E,GPIO.LOW)
 
GPIO.cleanup()