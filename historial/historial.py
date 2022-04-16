from modulos.configuracion import Configuracion
from pymongo import MongoClient
import pprint



class Historial():
    def __init__(self) -> None:
        super().__init__()
        self.url = Configuracion.URL
        self.client = MongoClient(url)
        self.collection = client[Configuracion.DB]['historialsensores']
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

"""
pequeño script para generar datos de prueba
p = Historial()
for i in range(3,15):
    p.addMongoHistorial({
    "id": i,
    "idSensor": 1,
    "Valor":{
        "temparatura":randrange(30),
        "humedad":randrange(30)
    },
    "Fechadecreacion": datetime.datetime.now(),
    "Fechadeactualizacion": ""
    })
p.getHistorial()
gc.enable()"""