import RPi.GPIO as GPIO
from time import sleep


class MOTOR():
    def __init__(self):
        try:
            self.Motor1A = 37  # GPIO 23-26|pin 16 nueba ubicasion pasa al pin 29 L293d pin 7
            self.Motor1B = 31  # GPIO 24-6|pin 18 nueba ubicasion pasa al pin 37 L293d pin 2
            self.Motor1E = 29  # GPIO 25-5|pin 22 nueba ubicasion pasa al pin 31 L293d pin 1
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(self.Motor1A,GPIO.OUT)
            GPIO.setup(self.Motor1B,GPIO.OUT)
            GPIO.setup(self.Motor1E,GPIO.OUT)
        except Exception as error:
            print(error)

    def adelante(self):
        print("hacia adelante")
        GPIO.output(self.Motor1A,GPIO.HIGH)
        GPIO.output(self.Motor1B,GPIO.LOW)
        GPIO.output(self.Motor1E,GPIO.HIGH)
        sleep(2)

    def atras(self):
        print("hacia atras")
        GPIO.output(self.Motor1A,GPIO.LOW)
        GPIO.output(self.Motor1B,GPIO.HIGH)
        GPIO.output(self.Motor1E,GPIO.HIGH)
        sleep(2)

    def stop(self):
        print("deteniendo")
        GPIO.output(self.Motor1E,GPIO.LOW)
        sleep(1)

    def limpiesa(self):
       GPIO.cleanup()

x=MOTOR()
x.adelante()
x.stop()
x.atras()
x.limpiesa()