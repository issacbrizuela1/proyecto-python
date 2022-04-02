from configuracion import Configuracion
from urllib import response
import requests
import json
from requests.structures import CaseInsensitiveDict
class api:
    tabla = Configuracion.URL
    dbuser = Configuracion.USUARIO
    dbpassword = Configuracion.PASSWORD
    usuario = Configuracion.U_USUARIO
    password = Configuracion.U_PASSWORD
    HEADEr = ''
    token = ''
    datos = list()
    path = ''
    def __init__(self):
        pass

    def GET(self, header, token, datos, path):
        response = requests.get(self.tabla+path)

    def POST(self, header, token, datos, path):
        response = requests.post(self.tabla+path)

    def PUT(self, header, token, datos, path):
        response = requests.put(self.tabla+path)

    def DEL(self, header, token, datos, path):
        response = requests.delete(self.tabla+path)
