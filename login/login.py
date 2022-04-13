
from importlib.resources import path
from apis import SERVAPI
from urllib import response


class Login(SERVAPI):
    usuario=""
    contrasena=""
    def __init__(self) -> None:
        super(SERVAPI)
        
        self.path=['Login','Register','revisarToken']
        pass
    def setContrasena(self, contrasena):
        return super().setContrasena(contrasena)
    def setUsuario(self, usuario):
        return super().setUsuario(usuario)
    def login(self):
        #resp=self.GET(path=self.path[0],url='http://127.0.0.1:3333/',datos={'password':self.constrasena,'email':self.usuario})
        pass
    def session(self):
        resp=self.getToken(path=self.path[2],url='http://127.0.0.1:3333/',credenciales={'password':'123456789','email':'qwerty1@gmail.com'})
        print(resp)
x=Login()
x.session()