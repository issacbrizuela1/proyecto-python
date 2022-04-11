import collections
import gc
import datetime
from pymongo import MongoClient
import pprint
import asyncio
from jsonfileSensor import JsonFile


class Sensor(JsonFile):

    def __init__(self, url, db):
        self.url = url
        client = MongoClient(self.url)
        self.db = db
        self.collection = client[db]['sensores']
        #
        self.idSensor = 0
        self.idUsuario = 0
        self.NombreSensor = ""
        self.Descripcion = ""
        self.Fechadecreacion = ""
        self.Fechadeactualisacion = ""
        self.Estados = ["indefinido", "habilitado", "deshabilitado"]
        self.Estado = self.Estados[0]
        self.GPIO = list()
        self.IMG = ""
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
