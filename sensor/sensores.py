from pymongo import MongoClient
from modulos.configuracion import Configuracion
from jsonfileSensor import JsonFile
from conexcion.API2 import Servicio


class Sensor(JsonFile,Servicio):
    url = 'mongodb+srv://root:ZXCVzxcv1234@sandbox1.1jic6.mongodb.net/proyecto?authSource=admin&replicaSet=atlas-lz7100-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true'
    client = MongoClient(url)
    db = 'proyecto'
    collection = client[db]['sensores']
    Llista = list()
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
        self.Llista = list()
        pass

    def lcrear_sensor(self, sensor):
        self.Llista.append(sensor)

    def lmostrar_sensor(self, index):
        return self.Llista[index]

    def lmostrar_sensores(self):
        return self.Llista

    def lmodificar_sensor(self, index, sensor):
        self.Llista[index] = sensor

    def leliminar(self, sensor):
        self.Llista.remove(sensor)

    def ltamano(self):
        return len(self.Llista)

    def toObjects(self):
        Llista = list()
        data = self.getDataJson()
        for x in data:
            Llista.append(Sensor(idSensor=x['idSensor'], idUsuario=x['idUsuario'], NombreSensor=x["NombreSensor"],
                                Descripcion=x["Descripcion"], Estado=x["Estado"], GPIO=x["GPIO"], IMG=x["IMG"]))
        self.Llista = Llista

    def iterar(v):
        for val in list(v):
            if isinstance(val, list):
                for subval in list(val):
                    print(subval)
            else:
                print(val)

    def NcrearSensor(self,):

        pass
    def NmostrarSensor(self):

        pass

    def NverificarSensor(self):

        pass
    def NeditarSensor(self):

        pass
    def NeliminarSensor(self):

        pass

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
        for x in self.Llista:
            listDiccionario.append(x.__dict__)
            print(x.getDictory())
        return listDiccionario
