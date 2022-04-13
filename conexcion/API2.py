#from ctypes.wintypes import HACCEL
from email import header
#from configuracion import Configuracion
from urllib import response
import requests
import json
from requests.structures import CaseInsensitiveDict


class api:
    def __init__(self):
        self.usuario = ""
        self.constrasena = ""
        pass

    def setUsuario(self, usuario):
        self.usuario = str(usuario)

    def setContrasena(self, contrasena):
        self.constrasena = contrasena

    def getUsuario(self):
        return self.usuario

    def getContrasena(self):
        return self.constrasena

    def GET(self, url, path):
        try:
            if path != "":
                s = requests.get(url=url+path)
                return s.text
        except Exception as error:
            print(error)
    def DGET(self, url, path,datos):
        if datos=="":
            try:
                if path != "":
                    s = requests.get(url=url+path)
                    return s.text
            except Exception as error:
                print(error)
    def HGET(self, url, path,HEADER):
        try:
            if path != "":
                s = requests.get(url=url+path,headers=HEADER)
                return s.text
        except Exception as error:
            print(error)
    def DHGET(self, url, path,datos,HEADER):
        try:
            if path != "":
                s = requests.get(url=url+path,data=datos,headers=HEADER)
                return s.text
        except Exception as error:
            print(error)
    
    def POST(self, url, path, datos):
        try:
            if path != "":
                s = requests.post(url=url+path, data=datos)
                return s.text

        except Exception as error:
            print(error)

    def PUT(self, url, path):
        try:
            if path != "":
                s = requests.put(url=url+path)
                return s.text

        except Exception as error:
            print(error)

    def DEL(self, url, path):
        try:
            if path != "":
                s = requests.delete(url=url+path)
                return s.text

        except Exception as error:
            print(error)


p = api()
user = p.setUsuario('qwerty1@gmail.com')
contra = p.setContrasena('123456789')
# print(p.getUsuario())
pget1 = p.GET(url='http://127.0.0.1:3333/', path='mostrarSensores',datos='',HEADER='')
xd = type(pget1)
# print(xd)
# print(pget1)
session = p.POST(url='http://127.0.0.1:3333/', path='Login',datos={'password': '123456789', 'email': 'qwerty1@gmail.com'})
print(session)
veritoken = p.HGET(url='http://127.0.0.1:3333/', path='token',HEADER=session)
print(veritoken)
