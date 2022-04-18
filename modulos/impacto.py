import RPi.GPIO as GPIO
import time
class KY031:
    defaultsensor = 17
    def __init__(self,sensor)->None:
        if sensor!=None:
            self.sensor = sensor
        else:
            self.sensor=self.defaultsensor
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # funcion que ejecutara algo al detectar el golpe
    def active(null):
        #GPIO.out(led, GPIO.HIGH)
        pass
    def deteccion(self):
        # On detecting signal (falling edge), active function will be activated.
        GPIO.add_event_detect(self.sensor, GPIO.FALLING, callback=self.active, bouncetime=100)
        # main program loop
        try:
            while True:
                time.sleep(1)
        # Scavenging work after the end of the program
        except KeyboardInterrupt:
            GPIO.cleanup()

