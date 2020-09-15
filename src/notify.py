from abc import ABC, abstractmethod

class INotificador(ABC):
    """docstring for INotificador."""

    def __init__(self, arg):
        pass

    @abstractmethod
    def enviar(self, msj):
        pass

class NotificadorSMS(INotificador):
    """docstring for NotificadorSMS."""

    def __init__(self):
        super().__init__()

    def enviar(self, msj):
        print('Mensaje de texto')


class NotificadorCorreo(INotificador):
    """docstring for NotificadorCorreo."""

    def __init__(self):
        super().__init__()

    def enviar(self, msj):
        print('Mensaje de correo electrónico')

class NotificadorFacebook(INotificador):
    """docstring for NotificadorFacebook."""

    def __init__(self):
        super().__init__()

    def enviar(self, msj):
        print('Mensaje de facebook')

class NotificadorEmpresarial(INotificador):
    """docstring for NotificadorEmpresarial."""

    def __init__(self):
        super().__init__()

    def enviar(self, msj):
        print('Mensaje empresarial')
