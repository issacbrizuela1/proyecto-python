import requests 
import json
from requests.structures import CaseInsensitiveDict

class APIRestProyecto:
    def _init_(self,domain,prefix):
        self.domain=domain
        self.prefix=prefix
        #self.domain="http://dominio"
        #self.prefix="/api/v1/"
        self.endpoint=self.domain+self.prefix
        self.token=""
        
    def getToken(self,credenciales,path="login"):
        path=self.endpoint+path
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        resp = requests.post(path,data=credenciales, headers=headers)
        return resp.json()
    
    def metodoGet(self,data,path):
        path=self.endpoint+path
        data = {}
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = "Bearer %s" % self.token
        resp = requests.get(path,data=data, headers=headers)
        return resp
            
communication = APIRestProyecto("https://pokeapi.co/","api/v2/")
data = {
	"email": "micorreo",
	"password": "password"
}

#print(comunicacion.getToken(data,"users/login")) 
token="Mzcz.fP6eO3oaVgyqJdPAbUeOWWveXyxlb3ghxeGgf6cS9E9TMazRyhTQN9qeNAIf"
communication.token=token
print(communication.metodoGet(data,"pokemon"))