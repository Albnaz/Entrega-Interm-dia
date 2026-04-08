class Contentor:
    """
    Classe Contentor:
    Classe que representa contentores, um elemento de grelha que contém objetos adicionais.
    O jogador pode usar estes pra guardar objetos adicionais para encher pacotes posteriores mais rapidamente.
    São representados como "[⛶]" quando vazios, contendo o seu objeto quando um é colocado
    """
    def __init__(self):
        self.objeto = None

    def __str__(self):
        if self.objeto == None:
            return "[⛶]"
        elif len(str(self.objeto)) > 3:
            return "[◫]"
        else:
            return "["+str(self.objeto)+"]"
