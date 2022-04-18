import RPi.GPIO as GPIO
from time import sleep
class MOTOR:
    GPIO.setmode(GPIO.BOARD)
    default_Motor1A=37  # GPIO 23-26|pin 16 nueba ubicasion pasa al pin 29 L293d pin 7
    default1_Motor1B=31 # GPIO 24-6|pin 18 nueba ubicasion pasa al pin 37 L293d pin 2
    default_Motor1E=29  # GPIO 25-5|pin 22 nueba ubicasion pasa al pin 31 L293d pin 1
    def __init__(self,nMotor1A,nMotor1B,nMotor1E):
        try:
            if nMotor1A!=None and nMotor1B!=None and nMotor1E!=None:
                Motor1A =  nMotor1A
                Motor1B =  nMotor1B
                Motor1E =  nMotor1E
            else:
                Motor1A = self.default_Motor1A
                Motor1B = self.default1_Motor1B
                Motor1E = self.default_Motor1E
            GPIO.setup(Motor1A, GPIO.OUT)
            GPIO.setup(Motor1B, GPIO.OUT)
            GPIO.setup(Motor1E, GPIO.OUT)
        except Exception as error:
            print(error)
    def adelante(self):
        print("hacia adelante")
        GPIO.output(self.Motor1A, GPIO.HIGH)
        GPIO.output(self.Motor1B, GPIO.LOW)
        GPIO.output(self.Motor1E, GPIO.HIGH)
        sleep(5)
    def atras(self):
        print("hacia atras")
        GPIO.output(self.Motor1A, GPIO.LOW)
        GPIO.output(self.Motor1B, GPIO.HIGH)
        GPIO.output(self.Motor1E, GPIO.HIGH)
        sleep(5)
    def stop(self):
        print("deteniendo")
        GPIO.output(self.Motor1E, GPIO.LOW)
        sleep(1)
    def limpiesa(self):
        GPIO.cleanup()