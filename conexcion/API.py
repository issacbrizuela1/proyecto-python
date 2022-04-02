from urllib import response
import requests
import json
from requests.structures import CaseInsensitiveDict
from conf.configuracion import conf


class api:
    def __init__(self):

        tabla = conf.URL
        dbuser = conf.USUARIO
        dbpassword = conf.PASSWORD
        usuario = conf.U_USUARIO
        password = conf.U_PASSWORD
        HEADEr = ''
        token = ''
        datos = list()
        path = ''

    def GET(self, header, token, datos, path):
        response = requests.get(self.tabla+path)

    def POST(self, header, token, datos, path):
        response = requests.post(self.tabla+path)

    def PUT(self, header, token, datos, path):
        response = requests.put(self.tabla+path)

    def DEL(self, header, token, datos, path):
        response = requests.delete(self.tabla+path)


s = api.tabla
print(s)
