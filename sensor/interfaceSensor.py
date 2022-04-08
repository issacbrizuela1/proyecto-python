import json
from operator import truediv
import os
import datetime
from sensores import Sensor


class InterfasSensor:
    def __init__(self) -> None:
        self.lista = Sensor()
        self.lista.toObjects()

    def limpirarConsola(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def crearNuevoSensor():
        s = Sensor()
        ultimosensor=s.tamano()
        s.idSensor=ultimosensor+1
        s.idUsuario=""#usuario en sesion
        s.NombreSensor = input("Nombre del Producto:")
        s.Descripcion = input("Nombre del Producto:")
        s.Estado[0]
        print(
            "acontinuacion ingrese los puertos GPIO que usara y un nombre para cada puerto.")
        control = True
        while control:
            nombrePuerto = input("nombre del puerto\t:")
            puerto = input("numero del puerto a usar\t:")
            opcion = input("¿Desea terminar de agregar puertos GPIO? Y/N")
            s.GPIO.append({str(nombrePuerto): int(puerto)})
            if opcion.upper() == "Y":
                control = False
        s.Fechadecreacion = datetime.datetime.now()
        s.IMG = input(
            "ingrese una url de una imagen siquiere que su sensor tenga una\t:")
        return s

    def iterar(self, lista):
        for valor in list(lista):
            if isinstance(valor, list):
                for subval in list(valor):
                    self.iterar(subval)
            else:
                print(valor)
        pass

    def mostrarSensores(self, lista=None):
        self.limpirarConsola()
        print("\n\n" + "*" * 30 + "Datos de Productos" + "*" * 30)
        if (lista == None):
            mylista = self.lista
        else:
            mylista = lista
        print("NombreSensor".ljust(5) + "\t\t" +
              'Descripcion'.ljust(20) + '\t\t' +
              'Estado'.ljust(20) + '\t\t' +
              'GPIO'.ljust(20) + '\t\t' +
              'Fechadecreacion'.ljust(20) + '\t\t' +
              'Fechadeactualisacion'.ljust(20) + '\t\t' +
              'IMG'.ljust(20) + '\t\t')
        i = 0
        for p in mylista:
            print(str(i).ljust(5) + "\t\t" + str(p))
            i += 1
        input("oprime enter para continuar .....")

    def buscarSensor(self):
        print("por medio de que desea buscar el sensor:\n"+"1.por id\n2.nommbre")
        opcion=int(input(">>>"))
        if opcion==1:
            nombre=str(input("ingrese el nombre del sensor:"))
            mylista = [p for p in self.lista if p.NombreSensor == nombre]
        elif opcion==2:
            id=str(input("ingrese el nombre del sensor:"))
            mylista = [p for p in self.lista if p.idSensor == id]
        self.mostrarSensores(mylista)

    def getListaSensores(self):
        return self.lista

    def modificarSensor(self):
        es=Sensor()
        print("si no desea modificar todo solo presione enter para omitir dependiendo del campo.")
        id=int(input("ingrese el id del sensor: "))
        mSensor=self.lista.mostrar_sensor(id)
        nNombre=str("ingrese el nombre del producto: ")
        if (len(nNombre) > 0):
            mSensor.NombreSensor=nNombre
        nDescripcion=str("ingrese el nombre del producto: ")
        if (len(nDescripcion) > 0):
            mSensor.Descripcion=nDescripcion
        ind=0
        for x in es.Estados:
            ind+=1
            print(ind+"-"+x)
        nEstado=int(input("seleccione el nuevo estado.\n elija el numero"))
        if (nEstado > 0):
            mSensor.Estado=es.Estados[nEstado]
        print(
            "acontinuacion ingrese los nuevos puertos GPIO que usara y un nombre para cada puerto.")
        control = True
        GPIO=list()
        while control:
            nombrePuerto = input("nombre del puerto\t:")
            puerto = input("numero del puerto a usar\t:")
            opcion = input("¿Desea terminar de agregar puertos GPIO? Y/N")
            GPIO.append({str(nombrePuerto): int(puerto)})
            if opcion.upper() == "Y":
                mSensor.GPIO=GPIO
                control = False
        mSensor.Fechadeactualisacion=datetime.datetime.now()
        mSensor.IMG=str(input("ingrese la nueva url para la imagen"))
        pass
    
    def eliminarSensor(self):
        id = input("Introduce ID:")
        id = int(id)
        print(self.lista.mostrar_sensor(id))
        self.lista.eliminar(self.lista.mostrar_sensor(id))