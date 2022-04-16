import sys
from conexcion.API2 import Servicio


class Login():

    path = ['Login', 'Register', 'revisarToken','straerUsuario','scerrarSesion']
    lista=list()
    LToken=''
    LEstado=''
    def __init__(self):
        self.usuario = ""
        self.contrasena = ""
        self.id = ""
        pass

    def login(self,user,password):
        self.usuario=user
        self.contrasena=password
        resp = Servicio.POST(self,url='http://127.0.0.1:3333/', path=self.path[0],datos={'email':self.usuario, 'password':self.contrasena})
        Servicio.setToken(self,resp['token'])
        self.LToken =Servicio.getToken(self)
        s = Servicio.comprovartoken(self,url='http://127.0.0.1:3333/')
        if s==True:
            self.LEstado=Servicio.aESTADO='activo'
        else:
            self.LEstado=Servicio.aESTADO='invalido'
        datosuser=self.getusuario()
        self.id=datosuser['id']
        return s

    def logout(self):
        resp = Servicio.nHPOST(self, url='http://127.0.0.1:3333/', path=self.path[4], HEADER=self.LToken)
        return resp
        pass

    def getusuario(self):
        resp=Servicio.HGET(self,url='http://127.0.0.1:3333/', path=self.path[3],HEADER=self.LToken)
        return resp

    def crearUsuario(self, login):
        self.lista.append(login)

    def modificarUsuario(self, index, login):
        self.lista[index] = login

    def eliminar(self, login):
        self.lista.remove(login)
"""
s=Login()
x=s.login('qwerty1@gmail.com','123456789')
print(x)
"""
"""
p = Login()
s = p.login()
p.usuario='qwerty1@gmail.com'
p.contrasena='123456789'
print(s)
print(p.usuario)
print(p.contrasena)
print(p.LToken)
print(p.LEstado)
print(p.id)
print(p.logout())

"""
"""
sys.path.append('\conexcion')
x=len(sys.path)
print(x)
for x in range(0,x):
    print(sys.path[x])
"""
