import RPi.GPIO as GPIO
import time

class KY031:
    def __init__(self) -> None:
        self.sensor = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # funcion que ejecutara algo al detectar el golpe

    def deteccion(self):
        # Function executed on signal detection
        def active(null):
            print("golpe detectado")

        # On detecting signal (falling edge), active function will be activated.
        GPIO.add_event_detect(self.sensor, GPIO.FALLING,
                              callback=active, bouncetime=100)

        # main program loop
        try:
            while True:
                time.sleep(1)

        # Scavenging work after the end of the program
        except KeyboardInterrupt:
            GPIO.cleanup()


x = KY031()
x.deteccion()
