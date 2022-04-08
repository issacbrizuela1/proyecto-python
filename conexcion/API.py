#from ctypes.wintypes import HACCEL
from email import header
from conf.configuracion import Configuracions
from urllib import response
import requests
import json
from requests.structures import CaseInsensitiveDict
class api:
    tabla = Configuracions.URL
    usuario = Configuracions.U_USUARIO
    password = Configuracions.U_PASSWORD
    HEADEr = ''
    token = ''
    datos = list()
    path = ''
    def __init__(self):
        pass

    def GET(self,url,path,datos):
        try:
            if path=="login" or path!="":
                headers = CaseInsensitiveDict()
                headers["Accept"] = "application/json"
                data = {
                    "usuario":datos.usuario,
                    "contraseña":datos.contrasena
                }
                resp = requests.post(path,data=data, headers=headers)
                return resp.json()
            elif path!="" or path!="register":
                path=self.endpoint+path
                headers = CaseInsensitiveDict()
                headers["Accept"] = "application/json"
                headers["Authorization"] = "Bearer %s" % self.token
                resp = requests.get(url+path,data=datos, headers=headers)
                return resp
        except Exception as error:
            print(error)

    def POST(self,url,path):
        #return requests.post(url+path)
        try:
            if path!="":
                path=self.endpoint+path
                data = {}
                headers = CaseInsensitiveDict()
                headers["Accept"] = "application/json"
                headers["Authorization"] = "Bearer %s" % self.token
                resp = requests.get(url+path,data=data, headers=headers)
                return resp
        except Exception as error:
            print(error)


    def PUT(self,url,path):
        try:
            if path!="":
                path=self.endpoint+path
                data = {}
                headers = CaseInsensitiveDict()
                headers["Accept"] = "application/json"
                headers["Authorization"] = "Bearer %s" % self.token
                resp = requests.get(url+path,data=data, headers=headers)
                return resp
        except Exception as error:
            print(error)

    def DEL(self,url,path):
        try:
            if path!="":
                path=self.endpoint+path
                data = {}
                headers = CaseInsensitiveDict()
                headers["Accept"] = "application/json"
                headers["Authorization"] = "Bearer %s" % self.token
                resp = requests.get(url+path,data=data, headers=headers)
                return resp
        except Exception as error:
            print(error)

    def getToken(self,credenciales,path="login"):
        try:
            path=self.endpoint+path
            headers = CaseInsensitiveDict()
            headers["Accept"] = "application/json"
            resp = requests.post(path,data=credenciales, headers=headers)
            return resp.json()
        except Exception as error:
            print(error)
