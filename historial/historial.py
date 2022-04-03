
from configuracion import Configuracion


class Historial(Configuracion):
    def __init__(self) -> None:
        super().__init__()
        url = self.URL
        client = MongoClient(url)
        collection = client[self.DB]['sensores']
        id=0
        idSensor=0
        Valor=list()
        Fechadecreacion=""
        Fechadeactualizacion=""