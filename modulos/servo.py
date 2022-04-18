import RPi.GPIO as GPIO
import time
class SERVO:
    #usar el pin 32 para la señal PWM
    pwm_gpio = 32
    frequence = 50
    default_centro=130
    default_IZQ=100
    default_DER=145
    # funcion para calcular el porcentaje del angulo
    def angle_to_percent(angle):
        if angle > 180 or angle < 0:
            return False

        start = 1
        end = 12.5
        ratio = (end - start) / 180  # Calcul ratio from angle to percent

        angle_as_percent = angle * ratio

        return start + angle_as_percent
    def __init__(self,izq,centro,der)->None:

        if izq!=None and centro != None and der!= None:
            self.ang_der=der
            self.ang_izq=izq
            self.ang_centro=centro
        else:
            self.ang_der = self.default_DER
            self.ang_izq = self.default_IZQ
            self.ang_centro = self.default_centro
        GPIO.setup(self.pwm_gpio, GPIO.OUT)
        pwm = GPIO.PWM(self.pwm_gpio, self.frequence)
        GPIO.setmode(GPIO.BOARD)  # usa el modo de numeracion de la placa
        GPIO.setwarnings(False)  # deshabilita advertencias
        time.sleep(5)

    # poner a la derecha
    def Sder(self):
        ang_der = 145
        self.pwm.start(self.angle_to_percent(ang_der))
        print('angulo ' + str(ang_der) + "°")
        time.sleep(5)

    # poner a la izquierda
    def Sizq(self):
        ang_izq = 100
        self.pwm.ChangeDutyCycle(self.angle_to_percent(ang_izq))
        print('angulo ' + str(ang_izq) + "°")
        time.sleep(5)

    # poner al centro
    def Sdelante(self):
        ang_centro = 130
        self.pwm.ChangeDutyCycle(self.angle_to_percent(ang_centro))
        print('angulo ' + str(ang_centro) + "°")
        time.sleep(5)

    # limpia los GPIO
    def Slimpiesa(self):
        self.pwm.stop()
        GPIO.cleanup()