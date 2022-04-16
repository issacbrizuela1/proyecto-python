import os
import datetime
from sensores import Sensor


class InterfasSensor:

    def __init__(self) -> None:
        self.lista = Sensor()
        self.lista.toObjects()

    def limpirarConsola(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def crearNuevoSensor(self):
        s = Sensor()
        ultimosensor = s.tamano()
        s.idSensor = ultimosensor+1
        s.idUsuario = ""  # usuario en sesion
        s.NombreSensor = input("Nombre del Sensor:")
        s.Descripcion = input("Descripción del Sensor:")
        s.Estado = "indefinido"
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
        fecha = datetime.datetime.now()
        parse = fecha.isoformat()
        s.Fechadecreacion = parse
        s.IMG = input(
            "ingrese una url de una imagen siquiere que su sensor tenga una\t:")
        return s

    def iterar(self, lista):
        i = 0
        for valor in list(lista):
            if isinstance(valor, list):
                for subval in list(valor):
                    self.iterar(subval)
            else:
                print(str(i)+'      ' +
                      str(valor.idSensor)+'      ' +
                      str(valor.idUsuario)+'      ' +
                      str(valor.NombreSensor)+'      ' +
                      str(valor.Descripcion)+'      ' +
                      str(valor.Estado)+'      ' +
                      str(valor.GPIO)+'      ' +
                      str(valor.Fechadecreacion)+'      ' +
                      str(valor.Fechadeactualisacion)+'      ' +
                      str(valor.IMG)+'      '
                      )
                i += 1
        pass

    def mostrarSensores(self, lista=None):
        self.limpirarConsola()
        print("\n\n" + "*" * 30 + "Datos de Sensores" + "*" * 30)
        if (lista == None):
            mylista = self.lista
        else:
            mylista = self.lista
            print("#")
            """
        print("#" + '      ' +
              "idSensor"+'      ' +
              "idUsuario"+'      ' +
              "NombreSensor"+'      ' +
              'Descripcion'+'      ' +
              'Estado'+'      ' +
              'GPIO'+'      ' +
              'Fechadecreacion'+'      ' +
              'Fechadeactualisacion'+'      ' +
              'IMG'+'      ')
              """
        self.iterar(mylista)
        input("oprime enter para continuar .....")

    def buscarSensor(self):
        print("por medio de que desea buscar el sensor:\n"+"1.por id\n2.nommbre")
        opcion = int(input(">>>"))
        if opcion == 1:
            nombre = str(input("ingrese el nombre del sensor:"))
            mylista = [p for p in self.lista if p.NombreSensor == nombre]
        elif opcion == 2:
            id = str(input("ingrese el nombre del sensor:"))
            mylista = [p for p in self.lista if p.idSensor == id]
        self.mostrarSensores(mylista)

    def getListaSensores(self):
        return self.lista

    def modificarSensor(self):
        es = Sensor()
        print("si no desea modificar todo solo presione enter para omitir dependiendo del campo.")
        id = int(input("ingrese el id del sensor: "))
        mSensor = self.lista.mostrar_sensor(id)
        nNombre = input("ingrese el nuevo nombre del sensor: ")
        nDescripcion = input("ingrese la nuevo descripcion del sensor: ")
        if (len(nNombre) > 0):
            mSensor.NombreSensor = nNombre
        if (len(nDescripcion) > 0):
            mSensor.Descripcion = nDescripcion
        ind = 0
        for x in es.Estados:
            ind += 1
            print(str(ind)+"-"+str(x))
        nEstado = int(input("seleccione el nuevo estado.\n elija el numero"))
        if (nEstado > 0):
            mSensor.Estado = es.Estados[nEstado]
        print(
            "acontinuacion ingrese los nuevos puertos GPIO que usara y un nombre para cada puerto.")
        control = True
        GPIO = list()
        while control:
            nombrePuerto = input("nombre del puerto\t:")
            puerto = input("numero del puerto a usar\t:")
            opcion = input("¿Desea terminar de agregar puertos GPIO? Y/N")
            GPIO.append({str(nombrePuerto): int(puerto)})
            if opcion.upper() == "Y":
                mSensor.GPIO = GPIO
                control = False
        fecha = datetime.datetime.now()
        mSensor.Fechadeactualisacion = str(fecha)
        mSensor.IMG = str(input("ingrese la nueva url para la imagen"))
        pass

    def eliminarSensor(self):
        id = input("Introduce el #:")
        id = int(id)
        print(self.lista.mostrar_sensor(id))
        self.lista.eliminar(self.lista.mostrar_sensor(id))

    def menuSensor(self):
        a = 10
        while a != 0:
            self.limpirarConsola()
            print("\n\n" + "*" * 30 + "Menu de Sensores" + "*" * 30)
            print("1) Nuevo Sensor")
            print("2) Modificar Sensor")
            print("3) Eliminar Sensor")
            print("4) Consultar Sensor")
            print("5) Mostrar Sensores")
            print("0) Salir")
            a = input("Selecciona una opción: ")
            if (a == '1'):
                p = self.crearNuevoSensor()
                self.lista.crear_sensor(p)
                self.lista.toJson(self.lista)
            elif (a == '2'):
                self.mostrarSensores()
                self.modificarSensor()
                self.lista.toJson(self.lista)
            elif (a == '3'):
                self.mostrarSensores()
                self.eliminarSensor()
                self.lista.toJson(self.lista)
            elif (a == '4'):
                self.buscarSensor()
            elif (a == '5'):
                self.mostrarSensores()
            elif (a == '0'):
                break
            else:
                print(
                    "La opcion no es correcta vuelve a seleccionar da enter para continuar.....")
                input()


if __name__ == '__main__':
    s = InterfasSensor()
    s.menuSensor()
