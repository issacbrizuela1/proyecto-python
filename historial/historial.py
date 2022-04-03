import collections
from configuracion import Configuracion
import gc
import datetime
from pymongo import MongoClient
import pprint
class Historial(Configuracion):
    def __init__(self) -> None:
        super().__init__()
        url = self.URL
        client = MongoClient(url)
        collection = client[self.DB]['historialsensores']
        id=0
        idSensor=0
        Valor=list()
        Fechadecreacion=""
        Fechadeactualizacion=""
        lista = list()
    #gets
    def getHistorial(self):
        r = self.collection.find({'idSensor': 1})
        t=self.collection.count_documents({'idSensor': 1})
        pp = pprint.PrettyPrinter(indent=4)
        for s in range(t):
            pp.pprint(r[s])
    def getlistaHistorial(self,index):
        r = self.collection.find({'idSensor': 1})
        print(r[index])
    def getallList(self):
        print(len(self.lista))
        for s in self.lista:
            print(s)

    #adds
    def addListHistorial(self):
        r = self.collection.find({'idSensor': 1})
        t=self.tamano()
        for s in range(t):
            self.lista.append(r[s])
    def addMongoHistorial(self, datos):
        self.collection.insert_one(datos)
    #del
    def eliminarMongoHistorial(self, datos):
        self.collection.delete_one(datos)
    def eliminarList(self,sensor):
        self.lista.remove(sensor)
    #mod
    def modificarHistorial(self, datos, index):
        self.collection.update_one(index, datos)
    #tamaño
    def tamanoMongoHistorial(self):
        return self.collection.count_documents({'idSensor': 1})
p=Historial()
p.addMongoHistorial()
gc.enable()