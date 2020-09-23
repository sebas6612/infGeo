from abc import ABC, abstractmethod

class IExportador(ABC):
    """docstring for INotificador."""

    def __init__(self, arg):
        pass

    @abstractmethod
    def enviar(self, msj):
        pass

class ExportadorXML(IExportador):
    """docstring for NotificadorSMS."""

    def __init__(self):
        super().__init__()

    def enviar(self, msj):
        print('Exportado como XML')


class ExportadorPDF(IExportador):
    """docstring for NotificadorCorreo."""

    def __init__(self):
        super().__init__()

    def enviar(self, msj):
        print('Exportado como PDF')
