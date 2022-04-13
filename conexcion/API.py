#from ctypes.wintypes import HACCEL
from email import header
#from configuracion import Configuracion
from urllib import response
import requests
import json
from requests.structures import CaseInsensitiveDict


class api:
    #tabla = Configuracion.API_URL

    HEADEr = ''
    token = ''
    datos = list()
    path = ''

    def __init__(self):
        self.usuario=""
        self.constrasena=""
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
            if path == "Login":
                headers = CaseInsensitiveDict()
                headers["Accept"] = "application/json"
                data = {
                    "email": 'qwerty1@gmail.com',
                    "password": '123456789'
                }
                s=url+path
                resp = requests.get(url=s, data=data, headers=headers)
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
#path, data=credenciales, headers=headers
    def getToken(self):
        try:
            path ='http://127.0.0.1:3333/revisarToken'
            headers = CaseInsensitiveDict()
            headers["bearer"] = "application/json"
            resp = requests.get(url=path,data={'password':'123456789','email':'qwerty1@gmail.com'},headers=headers)
            return resp.json()
        except Exception as error:
            print(error)


p = api()
#x = p.GET(path='mostrarSensores', url='http://127.0.0.1:3333/')
r=p.GET(path='Login',url='http://127.0.0.1:3333/')
#r=p.getToken()
print(r)
