import collections
from configuracion import Configuracion
import gc
import datetime
from pymongo import MongoClient
import pprint


class Sensor(Configuracion):
    url = Configuracions.URL
    client = MongoClient(url)
    collection = client[Configuracions.DB]['sensores']
    idSensor = 0
    idUsuario = 0
    NombreSensor = ""
    Descripcion = ""
    Fechadecreacion = ""
    Fechadeactualisacion = ""
    Estado = ""
    GPIO = 0
    IMG = ""
    lista = list()

    def __init__(self):
        
        pass
    #gets
    def getSensores(self):
        r = self.collection.find({'idUsuario': 1})
        t=self.collection.count_documents({'idUsuario': 1})
        pp = pprint.PrettyPrinter(indent=4)
        for s in range(t):
            pp.pprint(r[s])
    def getsensor(self,index):
        r = self.collection.find({'idUsuario': 1})
        print(r[index])
    def getallList(self):
        print(len(self.lista))
        for s in self.lista:
            print(s)

    #adds
    def addList(self):
        r = self.collection.find({'idUsuario': 1})
        t=self.tamano()
        for s in range(t):
            self.lista.append(r[s])
    def addMongo(self, datos):
        self.collection.insert_one(datos)
    #del
    def eliminarMongo(self, datos):
        self.collection.delete_one(datos)
    def eliminarList(self,sensor):
        self.lista.remove(sensor)
    #mod
    def modificar(self, datos, index):
        self.collection.update_one(index, datos)
    #tamaño
    def tamanoMongo(self):
        return self.collection.count_documents({'idUsuario': 1})
#gc.enable()
