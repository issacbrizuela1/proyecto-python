import collections
import gc
import datetime
from pymongo import MongoClient
import pprint
import asyncio

from jsonfileSensor import JsonFile


class Sensor(JsonFile):

    url = 'mongodb+srv://root:ZXCVzxcv1234@sandbox1.1jic6.mongodb.net/proyecto?authSource=admin&replicaSet=atlas-lz7100-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true'
    client = MongoClient(url)
    db = 'proyecto'
    collection = client[db]['sensores']
    Estados = ["indefinido", "habilitado", "deshabilitado"]

    def __init__(self, idSensor=0, idUsuario=0, NombreSensor='', Descripcion='', Fechadecreacion='', Fechadeactualisacion='', GPIO=list(), IMG=''):
        super(Sensor,self).__init__('DB/sensores.json')

        self.idSensor = idSensor
        self.idUsuario = idUsuario
        self.NombreSensor = NombreSensor
        self.Descripcion = Descripcion
        self.Fechadecreacion = Fechadecreacion
        self.Fechadeactualisacion = Fechadeactualisacion
        self.Estado = ""
        self.GPIO = GPIO
        self.IMG = IMG
        #
        self.lista = list()
        pass

    def crear_sensor(self, sensor):
        self.lista.append(sensor)

    def mostrar_sensor(self, index):
        return self.lista[index]

    def mostrar_sensores(self):
        return self.lista

    def modificar_sensor(self, index, sensor):
        self.lista[index] = sensor

    def eliminar(self, sensor):
        self.lista.remove(sensor)

    def tamano(self):
        return len(self.lista)

    def toObjects(self):
        lista = list()
        data = self.getDataJson()
        for x in data:
            lista.append(Sensor(idSensor=x['idSensor'], idUsuario=x['idUsuario'], NombreSensor=x["NombreSensor"],
                                Descripcion=x["Descripcion"], Estado=x["Estado"], GPIO=x["GPIO"], IMG=x["IMG"]))
        self.lista = lista

    def iterar(v):
        for val in list(v):
            if isinstance(val, list):
                for subval in list(val):
                    print(subval)
            else:
                print(val)

    def __str__(self):
        return str(self.idSensor) +\
            str(self.idUsuario) +\
            self.NombreSensor +\
            self.Descripcion +\
            self.Fechadecreacion +\
            self.Fechadeactualisacion +\
            self.Estado +\
            str(self.GPIO) +\
            self.IMG

    def typo(self):
        return type(self.GPIO)

    def getDictory(self):
        return {
            'idSensor': self.idSensor,
            'idUsuario': self.idUsuario,
            'NombreSensor': self.NombreSensor,
            'Descripcion': self.Descripcion,
            'Fechadecreacion': self.Fechadecreacion,
            'Fechadeactualisacion': self.Fechadeactualisacion,
            'Estado': self.Estado,
            'GPIO': self.GPIO,
            'IMG': self.IMG
        }

    def listDict(self):
        listDiccionario = list()
        for x in self.lista:
            listDiccionario.append(x.__dict__)
            print(x.getDictory())
        return listDiccionario

    def __iter__(self):
        self.__idx__ = 0
        return self

    def __next__(self):
        if self.__idx__ < len(self.lista):
            x = self.lista[self.__idx__]
            self.__idx__ += 1
            return x
        else:
            raise StopIteration
