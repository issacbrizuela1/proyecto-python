import os
import datetime
from login import Login


class InterfasLogin:

    def __init__(self) -> None:
        self.LG = Login()

    def limpirarConsola(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def inicio_de_sesion(self):
        us=str(input("ingrese el email:\t"))
        ps=str(input("ingrese el password:\t"))
        self.LG.login(us,ps)
        return s

    def mostrarsesion(self):
        print(self.LG.getusuario())
        input("presione enter para continuar")

    def cerrarSesion(self):
        self.LG.logout()

    def manusession(self):
        a = True
        while a:
            self.limpirarConsola()
            print("\n\n" + "*" * 30 + "Menu de Sensores" + "*" * 30)
            print("1) Nueva Sesion")
            print("2) Mostrar Sesion")
            print("3) Cerrar Sesion")
            print("0) Salir")
            opcion = input("Selecciona una opción: ")
            if (opcion == '1'):
                self.inicio_de_sesion()
            elif (opcion == '2'):
                self.mostrarsesion()
            elif (opcion == '3'):
                self.cerrarSesion()
            elif (opcion == '0'):
                a=False
                break
            else:
                print(
                    "La opcion no es correcta vuelve a seleccionar da enter para continuar.....")
                input()

if __name__ == '__main__':
    s = InterfasLogin()
    s.manusession()
