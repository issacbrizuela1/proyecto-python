from ctypes.wintypes import HACCEL
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

    def GET(self,path,datos):
        if path=="login":
            headers = CaseInsensitiveDict()
            headers["Accept"] = "application/json"
            resp = requests.post(path,data=datos, headers=headers)
            return resp.json()
        elif path!="":
            path=self.endpoint+path
            data = {}
            headers = CaseInsensitiveDict()
            headers["Accept"] = "application/json"
            headers["Authorization"] = "Bearer %s" % self.token
            resp = requests.get(path,data=data, headers=headers)
            return resp

    def POST(self,path):
        return requests.post(self.tabla+path)

    def PUT(self,path):
        return  requests.put(self.tabla+path)

    def DEL(self,path):
        return  requests.delete(self.tabla+path)
