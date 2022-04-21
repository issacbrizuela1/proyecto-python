import RPi.GPIO as GPIO
import time


class SERVO:
    # usar el pin 32 para la señal PWM
    # Set function to calculate percent from angle
    GPIO.setmode(GPIO.BOARD)  # Use Board numerotation mode
    GPIO.setwarnings(False)  # Disable warnings
    ang_der = 145
    ang_izq = 100
    ang_centro = 130
    # Use pin 32 for PWM signal
    pwm_gpio = 32
    frequence = 50
    GPIO.setup(pwm_gpio, GPIO.OUT)
    pwm = GPIO.PWM(pwm_gpio, frequence)
    time.sleep(5)
    def angle_to_percent(angle=0):
        if angle > 180 or angle < 0:
            return False

        start = 1
        end = 12.5
        ratio = (end - start)/180  # Calcul ratio from angle to percent

        angle_as_percent = angle * ratio

        return start + angle_as_percent
    

   # poner a la derecha

    def Sder(self):
        
        self.pwm.start(self.angle_to_percent(self.ang_der))
        print('angulo ' + str(self.ang_der) + "°")
        time.sleep(5)

    # poner a la izquierda
    def Sizq(self):
        
        self.pwm.ChangeDutyCycle(self.angle_to_percent(self.ang_izq))
        print('angulo ' + str(self.ang_izq) + "°")
        time.sleep(5)

    # poner al centro
    def Sdelante(self):
        
        self.pwm.ChangeDutyCycle(self.angle_to_percent(self.ang_centro))
        print('angulo ' + str(self.ang_centro) + "°")
        time.sleep(5)

    # limpia los  GPIO
    def Slimpiesa(self):
        self.pwm.stop()
        GPIO.cleanup()


x = SERVO()
x.Sder()
x.Sizq()
x.Sdelante()
x.Slimpiesa()
