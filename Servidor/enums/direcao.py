from enum import Enum

class Direcao(Enum):
    """
    Direções que o jogador pode olhar para e andar
    """
    UP=0
    DOWN=1
    RIGHT=2
    LEFT=3