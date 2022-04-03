import collections

import self
from configuracion import Configuracion
import gc
import datetime
from pymongo import MongoClient
import pprint


class Historial():
    url = Configuracion.URL
    client = MongoClient(url)
    collection = client[Configuracion.DB]['historialsensores']
    def __init__(self) -> None:
        super().__init__()
        url = Configuracion.URL
        client = MongoClient(url)
        collection = client[Configuracion.DB]['historialsensores']
        id = 0
        idSensor = 0
        Valor = list()
        Fechadecreacion = ""
        Fechadeactualizacion = ""
        lista = list()
    # gets

    def getHistorial(self):
        r = self.collection.find({'idSensor': 1})
        t = self.collection.count_documents({'idSensor': 1})
        pp = pprint.PrettyPrinter(indent=4)
        for s in range(t):
            pp.pprint(r[s])

    # adds
    def addMongoHistorial(self, datos):
        self.collection.insert_one(datos)
    # del

    def eliminarMongoHistorial(self, datos):
        self.collection.delete_one(datos)
    # mod

    def modificarHistorial(self, datos, index):
        self.collection.update_one(index, datos)
    # tamaño

    def tamanoMongoHistorial(self):
        return self.collection.count_documents({'idSensor': 1})


p = Historial()
p.addMongoHistorial({
    "id": 2,
    "idSensor": 1,
    "Valor":{
        "temparatura":5,
        "humedad":6
    },
    "Fechadecreacion": datetime.datetime.now(),
    "Fechadeactualizacion": ""
})
p.getHistorial()
gc.enable()
