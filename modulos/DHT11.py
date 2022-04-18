#!/usr/bin/python3

# Internet de las Cosas - http://internetdelascosas.cl
#
# Descripcion  : Programa que permite obtener la lectura de un sensor DHT11 Lenguaje     : Python version 3 Autor
# : Jose Zorrilla <jzorrilla@iot.cl> Dependencias : Libreria Circuit Python de Adafruit
# https://github.com/adafruit/Adafruit_CircuitPython_DHT Web          :
# https://www.internetdelascosas.cl/2017/05/19/raspberry-pi-conectando-un-sensor-de-temperatura-y-humedad-dht11/

# Importa las librerias necesarias
import sys
import time
import adafruit_dht


# Crea el objeto para acceder al sensor
# se debe descomentar la linea dependiendo del tipo de sensor (DHT11 o DHT22)
class Dht11:
    # Configuracion del puerto GPIO al cual esta conectado  (GPIO 23)
    defaultpin = 22

    def __init__(self, pin) -> None:
        if pin is not None:
            self.pin = pin
        else:
            self.pin = self.defaultpin
        # sensor = adafruit_dht.DHT11(pin)
        self.sensor = adafruit_dht.DHT11(self.pin)

    # Funcion principal en consola
    def consolatemphum(self):
        # Ciclo principal infinito
        while True:
            # Intenta ejecutar las siguientes instrucciones, si falla va a la instruccion except
            try:
                # Obtiene la humedad y la temperatura desde el sensor
                humedad = self.sensor.humidity
                temperatura = self.sensor.temperature
                # Imprime en la consola las variables temperatura y humedad con un decimal
                print('Temperatura={0:0.1f} C  Humedad={1:0.1f}%'.format(temperatura, humedad))
            # Se ejecuta en caso de que falle alguna instruccion dentro del try
            except RuntimeError as error:
                # Imprime en pantalla el error
                print(error.args[0])
            # Duerme 10 segundos
            time.sleep(10)

    # Funcion principal en para api
    def apitemphum(self):
        # Ciclo principal infinito
        while True:
            try:
                humedad = self.sensor.humidity
                temperatura = self.sensor.temperature
                return [temperatura, humedad]
            except RuntimeError as error:
                print(error.args[0])
            time.sleep(10)
