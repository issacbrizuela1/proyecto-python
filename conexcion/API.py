from urllib import response
import configuracion
import requests 
import json
from requests.structures import CaseInsensitiveDict
class api:
    def __init__(self):
        tabla=configuracion.URL
        dbuser=configuracion.USUARIO
        dbpassword=configuracion.PASSWORD
        usuario=configuracion.U_USUARIO
        password=configuracion.U_PASSWORD
        HEADEr=''
        token=''
        datos=list()
        path=''
    def GET(self,header,token,datos,path):
        response=requests.get(self.tabla+path)
    def POST(self,header,token,datos,path):
        response=requests.post(self.tabla+path)
    def PUT(self,header,token,datos,path):
        response=requests.put(self.tabla+path)
    def DEL(self,header,token,datos,path):
        response=requests.delete(self.tabla+path)
