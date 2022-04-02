from sqlite3 import Date


class Sensor:
    def __init__(self):
        idSensor = 0
        idUsuario = 0
        NombreSensor = ""
        Descripcion = ""
        Fechadecreacion = Date()
        Fechadeactualisacion = Date()
        Estado = ""
        GPIO = 0
