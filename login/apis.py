#from ctypes.wintypes import HACCEL
#from configuracion import Configuracion
from urllib import response
import requests
import json
from requests.structures import CaseInsensitiveDict


class SERVAPI:
    #tabla = Configuracion.API_URL

    HEADEr = ''
    token = ''
    datos = list()
    path = ''

    def __init__(self):
        # self.usuario
        # self.constrasena
        pass

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setContrasena(self, contrasena):
        self.constrasena = contrasena

    def getUsuario(self, usuario):
        return self.usuario

    def getContrasena(self, contrasena):
        return self.constrasena

    def GET(self, url, path, datos):
        try:
            if path == "login":
                headers = CaseInsensitiveDict()
                headers["Accept"] = "application/json"
                data = {
                    "usuario": datos.usuario,
                    "contraseña": datos.contrasena
                }
                resp = requests.post(path, data=data, headers=headers)
                return resp.json()
            elif path == "register":
                path = self.endpoint+path
                headers = CaseInsensitiveDict()
                headers["Accept"] = "application/json"
                headers["Authorization"] = "Bearer %s" % self.token
                resp = requests.get(url+path, data=datos, headers=headers)
                return resp
            elif path != "" and datos == "":
                resp = requests.get(url+path)
                return resp
        except Exception as error:
            print(error)

    def GET(self, url, path):
        try:
            if path != "":
                resp = requests.get(url+path)
                return resp

        except Exception as error:
            print(error)

    def POST(self, url, path):
        # return requests.post(url+path)
        try:
            if path != "":
                path = self.endpoint+path
                data = {}
                headers = CaseInsensitiveDict()
                headers["Accept"] = "application/json"
                headers["Authorization"] = "Bearer %s" % self.token
                resp = requests.get(url+path, data=data, headers=headers)
                return resp
        except Exception as error:
            print(error)

    def PUT(self, url, path):
        try:
            if path != "":
                path = self.endpoint+path
                data = {}
                headers = CaseInsensitiveDict()
                headers["Accept"] = "application/json"
                headers["Authorization"] = "Bearer %s" % self.token
                resp = requests.get(url+path, data=data, headers=headers)
                return resp
        except Exception as error:
            print(error)

    def DEL(self, url, path):
        try:
            if path != "":
                path = self.endpoint+path
                data = {}
                headers = CaseInsensitiveDict()
                headers["Accept"] = "application/json"
                headers["Authorization"] = "Bearer %s" % self.token
                resp = requests.get(url+path, data=data, headers=headers)
                return resp
        except Exception as error:
            print(error)

    def getToken(self, credenciales, path):
        try:
            path ='http://127.0.0.1:3333/'+path
            headers = CaseInsensitiveDict()
            headers["Accept"] = "application/json"
            resp = requests.post()
            return resp.json()
        except Exception as error:
            print(error)


##p = SERVAPI()
#x = p.GET(path='mostrarSensores', url='http://127.0.0.1:3333/')
#r=p.GET(path='mostrarSensores', url='http://127.0.0.1:3333/',datos={})
#print(x)
