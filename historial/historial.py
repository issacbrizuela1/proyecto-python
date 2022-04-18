"""
clase que mandara la informacion dada por los sensores a la bd por medio de la api una vez este jalando al 100
"""
import datetime
import gc
from random import randrange

from modulos.configuracion import Configuracion
from pymongo import MongoClient
from conexcion.API2 import Servicio
from modulos.configuracion import Configuracion

import pprint



class Historial(Servicio):
    API_url=Configuracion.API_URL
    url = Configuracion.URL
    client = MongoClient(url)
    PATH=['crearHistorial','mostrarHistorial','updateHistorial','deleteHistorial']
    collection = client[Configuracion.DB]['historialsensores']
    def __init__(self) -> None:
        self.id = 0
        self.idSensor = 0
        self.Valor = list()
        self.Fechadecreacion = ""
        self.Fechadeactualizacion = ""
        self.lista = list()
    # gets
    def getHistorial(self):
        r = self.collection.find({'idSensor': 1})
        t = self.collection.count_documents({'idSensor': 1})
        pp = pprint.PrettyPrinter(indent=4)
        for s in range(t):
            pp.pprint(r[s])
    def APIgetHistorialH(self,token):
        resp=self.HGET(url=self.API_url,path=self.PATH[1],HEADER=token)
        return resp
    def APIgetHistorial(self):
        resp=self.GET(url='http://127.0.0.1:3333/',path=self.PATH[1])
        return resp
    # adds
    def addMongoHistorial(self, datos):
        self.collection.insert_one(datos)
    def NaddhistorialH(self,datos,token):
        if datos!="" and token !="":
            resp=self.HPOST(self.API_url,self.PATH[0],datos,token)
        else:
            resp="no se proporcionaron los datos de autenticasion o no se proporcionaron los datos a guardar"
        return resp
    def Naddhistorial(self,datos):
        if datos!="":
            resp=self.POST(url='http://127.0.0.1:3333/',path=self.PATH[0],datos=datos)
        else:
            resp="no se proporcionaron los datos de autenticasion o no se proporcionaron los datos a guardar"
        return resp
    # del
    def eliminarMongoHistorial(self, datos):
        self.collection.delete_one(datos)
    def NeliminarSensor(self,id,token):
        resp=self.HDEL(url=self.url,path=self.PATH[3],param=id,HEADER=token)
        return resp
    # mod
    def modificarHistorial(self, datos, index):
        self.collection.update_one(index, datos)
    def NmodificarHistorial(self,id,datos,token):
        resp=self.HPUT(url=self.API_url,path=self.PATH[2],param=id,datos=datos,HEADER=token)
        return resp
    # EXTRAS
    def tamanoMongoHistorial(self):
        return self.collection.count_documents({'idSensor': 1})


#pequeño script para generar datos de prueba
p = Historial()
try:
    for i in range(1,5):

        p.addMongoHistorial(datos={
        "id": i,
        "idSensor": i,
        "Valor":{
            "temparatura":randrange(30),
            "humedad":randrange(30),
            "pruebainsercion":"api"
        },
        "Fechadecreacion": datetime.datetime.now(),
        "Fechadeactualizacion": ""
        })
        print(i)
except Exception as err:
    print(err)
p.APIgetHistorial()
gc.enable()