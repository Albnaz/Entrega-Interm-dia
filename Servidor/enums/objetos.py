from enum import Enum
class Objetos(Enum):
    """
       Objetos gerados pelos geradores, colocados nos pacotes e entregados aos clientes.
    """
    def __str__(self):
        return self.value
    CIRCULO = "◦"
    TRIANGULO = "▵"
    QUADRADO = "▫"
    RETANGULO="▪"
    