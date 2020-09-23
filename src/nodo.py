from abc import ABC, abstractmethod

class Nodo(ABC):

    def __init__(self, arg):
        pass


class Ciudad(Nodo):
    estadoEspecifico=""

    def __init__(self):
        super().__init__()

    def funcInfoGeo(self):
        print('Ciudad')

class Industria(Nodo):
    estadoEspecifico=""

    def __init__(self):
        super().__init__()

    def funcInfoGeo(self):
        print('Industria')

class LugarTuristico(Nodo):
    estadoEspecifico=""

    def __init__(self):
        super().__init__()

    def funcInfoGeo(self):
        print('Lugar Turistico')
