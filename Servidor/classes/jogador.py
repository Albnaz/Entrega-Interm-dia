from Servidor.enums.direcao import Direcao
class Jogador:
    """
    Classe Jogador:
    Classe utilizada para representar  o jogador. Representado no mapa com o seu ID.
    :param: pID - identificador do jogador no mapa
    :param: direcao - direcao que o jogador está a olhar
    :param:  posx - cordenada no eixo horizontal do jogador
    :param: posy - cordenada no eixo vertical do jogador
    :param: pontuacao - pontuacao do jogador
    """
    def __init__(self,pID,posx,posy):
        self.pID= pID
        self.direcao = Direcao.DOWN
        self.objeto = None
        self.posx = posx
        self.posy = posy
        self.pontuacao= 0
    
    def getPosX(self):
        return self.posx
    
    def getPosY(self):
        return self.posy
    
    def getDirecao(self):
        return self.direcao
    def __str__(self):
        return "["+str(self.pID)+"]"