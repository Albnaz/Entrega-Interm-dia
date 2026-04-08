class Parede:
    """
    Classe Parede:
    Classe utilizada para delimitar o mapa, impedindo que o jogador interaja com partes do mapa que possivelmente
    causariam erros. Representada como "[X]" na representação do mapa no terminal.
    """

    def __init__(self):
        pass
    def __str__(self):
        return "[X]"
    