import requests
from requests.structures import CaseInsensitiveDict


class Servicio:
    aTOKEN = ""
    aESTADO = ""
    def __init__(self):
        pass

    def setToken(self, token):
        self.aTOKEN = token

    def getToken(self):
        return self.aTOKEN

    def setEstado(self, estado):
        self.aESTADO = estado

    def getEstado(self):
        return self.aESTADO

    def GET(self, url, path):
        try:
            if path != "":
                s = requests.get(url=url+path)
                return s.json()
        except Exception as error:
            print(error)

    def DGET(self, url, path, datos):
        if datos == "":
            try:
                if path != "":
                    s = requests.get(url=url+path, data=datos)
                    return s.json()
            except Exception as error:
                print(error)

    def HGET(self, url, path, HEADER):
        try:
            if path != "":
                headers = CaseInsensitiveDict()
                headers["Accept"] = "application/json"
                headers["Authorization"] = "Bearer "+HEADER
                s = requests.get(url=url+path, headers=headers)
                return s.json()
        except Exception as error:
            print(error)

    def DHGET(self, url, path, datos, HEADER):
        try:
            if path != "":
                headers = CaseInsensitiveDict()
                headers["Accept"] = "application/json"
                headers["Authorization"] = "Bearer "+HEADER
                s = requests.get(url=url+path, data=datos, headers=headers)
                return s.json()
        except Exception as error:
            print(error)

    def POST(self, url, path, datos):
        try:
            if path != "":
                s = requests.post(url=url+path, data=datos)
                return s.json()

        except Exception as error:
            print(error)

    def HPOST(self, url, path, datos, HEADER):
        try:
            if path != "":
                headers = CaseInsensitiveDict()
                headers["Accept"] = "application/json"
                headers["Authorization"] = "Bearer "+HEADER
                s = requests.post(url=url+path, data=datos, headers=headers)
                return s.json()
        except Exception as error:
            return error

    def nHPOST(self, url, path, HEADER):
        try:
            if path != "":
                headers = CaseInsensitiveDict()
                headers["Accept"] = "application/json"
                headers["Authorization"] = "Bearer "+HEADER
                s = requests.post(url=url+path, headers=headers)
                return s.json()
        except Exception as error:
            return error

    def PUT(self, url, path, param, datos):
        try:
            if path != "":
                s = requests.put(url=url+path, params=param, data=datos)
                return s.json()
        except Exception as error:
            print(error)

    def HPUT(self, url, path, param, datos, HEADER):
        try:
            if path != "":
                headers = CaseInsensitiveDict()
                headers["Accept"] = "application/json"
                headers["Authorization"] = "Bearer "+HEADER
                s = requests.put(url=url+path, params=param,data=datos, headers=headers)
                return s.json()
        except Exception as error:
            print(error)

    def DEL(self, url, path, param):
        try:
            if path != "":
                s = requests.delete(url=url+path, params=param)
                return s.json()
        except Exception as error:
            print(error)

    def HDEL(self, url, path, param, HEADER):
        try:
            if path != "":
                headers = CaseInsensitiveDict()
                headers["Accept"] = "application/json"
                headers["Authorization"] = "Bearer "+HEADER
                s = requests.delete(
                    url=url+path, params=param, headers=headers)
                return s.json()
        except Exception as error:
            print(error)

    def comprovartoken(self, url):
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = "Bearer "+self.aTOKEN
        resp = requests.get(url=url+'revisarToken', headers=headers)
        return resp.json()

"""
p = Servicio()
resp=p.POST(url='http://127.0.0.1:3333/', path='Login',datos={'password': '123456789', 'email':'qwerty1@gmail.com'})
p.aTOKEN=resp['token']
s=p.comprovartoken(url='http://127.0.0.1:3333/')
print(s)
"""