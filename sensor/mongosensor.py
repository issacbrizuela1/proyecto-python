import collections

import gc
import datetime
from pymongo import MongoClient
import pprint
import asyncio


class Sensor():
    url = ""
    client = MongoClient(url)
    collection = client['proyecto']['sensores']
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
    #mongo
    async def getSensores(self):
        await asyncio.sleep(1)
        return await self.collection.find({'idUsuario': 1})
        #t= await self.collection.count_documents({'idUsuario': 1})
        #pp = pprint.PrettyPrinter(indent=4)
        
        #for s in range(t):
         #   pp.pprint(r[s])
    #mongo
    def getsensor(self,index):
        r = self.collection.find({'idUsuario': 1})
        return r[index]
    def guardarsensoresenlocal(self):
        r=self.getSensores()
        c=self.tamanoMongo()
        for s in range(t):
            self.lista.append(r[t])
    #lista
    def getallList(self):
        return self.lista
        #for s in self.lista:
            #print(s)
    #lista
    def getallList(self,index):
        return self.lista[index]
#adds
    #lista
    def addList(self,sensor):
        self.lista.append(sensor)
    #mongo
    def addMongo(self, datos):
        self.collection.insert_one(datos)
#del
    #mongo
    def eliminarMongo(self, datos):
        self.collection.delete_one(datos)
    #lista
    def eliminarList(self,sensor):
        self.lista.remove(sensor)
#mod
    def modificarMongo(self, datos, index):
        self.collection.update_one(index, datos)
    def modificarLista(self, index, sensor):
        self.lista[index] = sensor
#extras
    def tamanoMongo(self):
        return self.collection.count_documents({'idUsuario': 1})
    def tamanoLista(self):
        return len(self.lista)

#gc.enable()
