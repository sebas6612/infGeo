from abc import ABC, abstractmethod
import Nodo

class IExportador(ABC):

    def __init__(self, arg):
        pass

    @abstractmethod
    def enviar(self, msj):
        pass

class ExportadorXML(IExportador):

    def __init__(self):
        super().__init__()

    def enviar(self, msj):
        print('Exportado como XML')


class ExportadorPDF(IExportador):

    def __init__(self):
        super().__init__()

    def enviar(self, msj):
        print('Exportado como PDF')
