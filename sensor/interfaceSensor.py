import json
from operator import truediv
import os
import datetime

from sensores2 import Sensor
class InterfasSensor:
    def __init__(self) -> None:
        self.lista = Sensor()
        self.lista.toObjects()
    def limpirarConsola(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    def crearNuevoSensor():
        s = Sensor()
        s.NombreSensor = input("Nombre del Producto:")
        s.Descripcion = input("Nombre del Producto:")
        s.Estado = "indefinido"
        
        s.Fechadecreacion=datetime.datetime.now()
        s.IMG = input("ingrese una url de una imagen siquiere que su sensor tenga una\t:")
        return s
    def agregarGPIO(self,s):
        print("acontinuacion ingrese los puertos GPIO que usara y un nombre para cada puerto.")
        control=True
        while control:
            nombrePuerto=input("nombre del puerto\t:")
            puerto=input("numero del puerto a usar\t:")
            opcion=input("¿Desea terminar de agregar puertos GPIO? Y/N")
            s.GPIO.append({str(nombrePuerto):int(puerto)})
            if opcion.upper()=="Y":
                control=False
    def iterar(self,lista):
        for valor in list(lista):
            if isinstance(valor,list):
                for subval in list(valor):
                    self.iterar(subval)
            else:
                print(valor)
        pass
    def mostrarSensores(self,lista=None):
        self.limpirarConsola()
        print("\n\n" + "*" * 30 + "Datos de Productos" + "*" * 30)
        if (lista == None):
            mylista = self.lista
        else:
            mylista = lista
        print("NombreSensor".ljust(5) + "\t\t" + 
            'Descripcion'.ljust(20) + '\t\t' + 
            'Estado'.ljust(20) + '\t\t'+
            'GPIO'.ljust(20) + '\t\t'+
            'Fechadecreacion'.ljust(20) + '\t\t'+
            'Fechadeactualisacion'.ljust(20) + '\t\t'+
            'IMG'.ljust(20) + '\t\t')
        i = 0
        for p in mylista:
            print(str(i).ljust(5) + "\t\t" + str(p))
            i += 1
        input("oprime enter para continuar .....")
    def buscarSensor(self, nombre):
        mylista = [p for p in self.lista if p.codigo == nombre]
        self.mostrarProducto(mylista)
    def getListaSensores(self):
        return self.lista