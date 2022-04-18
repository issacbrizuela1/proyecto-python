#!/usr/bin/env python3
#-- coding: utf-8 --
import RPi.GPIO as GPIO
import time


#Set function to calculate percent from angle
def angle_to_percent (angle) :
    if angle > 180 or angle < 0 :
        return False

    start = 1
    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent


GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
GPIO.setwarnings(False) #Disable warnings

#Use pin 32 for PWM signal
pwm_gpio = 32
frequence = 50
GPIO.setup(pwm_gpio, GPIO.OUT)
pwm = GPIO.PWM(pwm_gpio, frequence)
time.sleep(5)


#Init at right
angulo1=145
pwm.start(angle_to_percent(angulo1))
print('angulo '+str(angulo1)+"°")
time.sleep(5)

#Go at left
angulo1=100
pwm.ChangeDutyCycle(angle_to_percent(angulo1))
print('angulo '+str(angulo1)+"°")
time.sleep(5)

#Finish at center
angulo1=130
pwm.ChangeDutyCycle(angle_to_percent(angulo1))
print('angulo '+str(angulo1)+"°")
time.sleep(5)

#Close GPIO & cleanup
pwm.stop()
GPIO.cleanup()