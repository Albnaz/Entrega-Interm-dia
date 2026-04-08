from Servidor.classes.jogador import Jogador
from Servidor.enums.direcao import Direcao
from Servidor.classes.contentor import Contentor
from Servidor.classes.geradorobjeto import GeradorObjeto 
from Servidor.classes.pacote import Pacote
from Servidor.classes.clientes import Cliente


def gridgen(gridSizeX:int,gridSizeY:int):
    """
    gridgen()
    função auxiliar da classe Mapa, cria um array 2d com proporções gridSizeX por gridSizeY
    :param: gridSizeX:int - tamanho horizontal
    :param: gridSizeY:int - tamanho vertical
    :return: o array 2d
    """
    grid=[]
    for i in range(gridSizeY):
        grid.append([])
        for j in range(gridSizeX):
            grid[i].append("[ ]")
    return grid

class Mapa:
    """
    Class Mapa
    A classe principal, na qual a maioria da logica do jogo terá base.
    Esta classe possui duas funções principais, manipulando a posição dos jogadores ou fazendo-lhes interagir.
    :param: sizeX:int - tamanho horizontal do mapa
    :param: sizeY:int - tamanho vertical do mapa
    :param: grid - grelha com proporções sizeX por sizeY
    """
    def __init__(self,sizeX:int,sizeY:int):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.grid = gridgen(sizeX,sizeY)

    def insertPlayer(self,jogador:Jogador):
        self.grid[jogador.posy][jogador.posx]=jogador

    def insertContainer(self,contentor:Contentor,x,y):
        self.grid[x][y]=contentor

    def insertGenerator(self,gerador:GeradorObjeto,x,y):
        self.grid[y][x]=gerador
    
    def insertClient(self,cliente:Cliente,x,y):
        self.grid[y][x]=cliente

    def insertPackage(self,pacote:Pacote,x,y):
        self.grid[y][x]=pacote
    

    
    def interact(self,jogador:Jogador):
        """
        interact()
        função encarregada da interaçãa, segue o seguinte processo:
        -O objeto a ser interagido é encontrado dependendo da direção do jogador.
        -A classe do objeto é determinado, com o comportamento do interact sendo determinado com base nesta
        -Se a interação resultante trata-se de um pedido com sucesso, a função retorna true, para fins de
        armazenamento de dados.
        :param: jogaador:Jogador- O jogador a interagir
        :return: bool - Se a interação ganha pontos ou não
        """
        print(jogador.direcao)
        match jogador.getDirecao():
            case Direcao.UP:
                interactingObject = self.grid[jogador.posy-1][jogador.posx]
            case Direcao.DOWN:
                interactingObject = self.grid[jogador.posy+1][jogador.posx]
            case Direcao.LEFT:
                interactingObject = self.grid[jogador.posy][jogador.posx-1]
            case Direcao.RIGHT:
                interactingObject = self.grid[jogador.posy][jogador.posx+1]
        match interactingObject:
            case str():
                print("DEBUG: NADA")
            case Contentor():
                if interactingObject.objeto is not None:
                    if jogador.objeto is None: 
                        jogador.objeto = interactingObject.objeto 
                        interactingObject.objeto = None
                        print(jogador.objeto)
                        print(interactingObject.objeto)
                    else:
                        print("DEBUG: AMBOS POSSUIEM OBJETOS")
                else: 
                    if jogador.objeto is not None:
                        interactingObject.objeto = jogador.objeto
                        jogador.objeto = None
                        print(jogador.objeto)
                        print(interactingObject.objeto)
                    else:
                        print("DEBUG: AMBOS POSSUIEM OBJETOS")

            case GeradorObjeto():
                if jogador.objeto is None: 
                    jogador.objeto = interactingObject.getTipo()

                else:
                    print("DEBUG: JOGADOR JÁ TEM UM OBJETO")
            case Pacote():
                if jogador.objeto is not None:
                    if len(interactingObject.pacote) < interactingObject.maxlen:
                        interactingObject.insertObject(jogador.objeto)
                        jogador.objeto = None
                    else: 
                        print("DEBUG: NÃO CONSEGUE PEGAR")
                else:
                    if len(interactingObject.pacote) < interactingObject.maxlen:
                        jogador.objeto = interactingObject.pacote.pop(-1)
                    else:
                        jogador.objeto = interactingObject.pacote
                        interactingObject.pacote = []

            case Cliente():
                print(interactingObject.getPedido())
                if jogador.objeto is None:
                    print("DEBUG: JOGADOR NÃO TEM OBJETO")
                else:
                    if jogador.objeto==interactingObject.pedido:
                        print("DEBUG: SUCESSO")
                        jogador.pontuacao += 1
                        interactingObject.mudarpedido()
                        jogador.objeto=None
                        return True
                    else:
                        print("DEBUG: PACOTE DIFERENTE DO PEDIDO")
        return False

    def move(self,jogador:Jogador,dir:Direcao):
        """
        move()
        função que controla o movimento dos jogadores. dependendo da direção, o jogador irá mover-se para
        a quadricula adjacente nessa direção.
        :param jogador: o jogador a mover-se
        :param dir: a direção de movimento.
        """
        posx=jogador.posx
        posy=jogador.posy
        match dir:
            case Direcao.UP:
                if  posy>0: 
                    if isinstance(self.grid[jogador.posy-1][jogador.posx] ,str):
                        self.grid[posy][posx]="[ ]"
                        jogador.posy-=1
                        self.grid[jogador.posy][posx]=jogador
                    else:
                        print("DEBUG: COLISÃO")
                else:
                    print("DEBUG: NÃO É POSSIVEL MOVER")
        
            case Direcao.DOWN:
                if posy<self.sizeY-1: 
                    if isinstance(self.grid[jogador.posy+1][jogador.posx] ,str):
                        self.grid[posy][posx]="[ ]"
                        jogador.posy+=1
                        self.grid[jogador.posy][posx]=jogador
                    else:
                        print("DEBUG: COLISÃO")
                else:
                    print("DEBUG: NÃO É POSSIVEL MOVER")
            case Direcao.LEFT:
                if posx>0: 
                    if isinstance(self.grid[jogador.posy][jogador.posx-1] ,str):
                        self.grid[posy][posx]="[ ]"
                        jogador.posx-=1
                        self.grid[posy][jogador.posx]=jogador
                    else:
                        print("DEBUG: COLISÃO")
                else:
                    print("DEBUG: NÃO É POSSIVEL MOVER")
        
            case Direcao.RIGHT:
                print(posx)
                if posx<self.sizeX-1: 
                    if isinstance(self.grid[jogador.posy][jogador.posx+1] ,str):
                        self.grid[posy][posx]="[ ]"
                        jogador.posx+=1
                        self.grid[posy][jogador.posx]=jogador
                    else:
                        print("DEBUG: COLISÃO")
                else:
                    print("DEBUG: NÃO É POSSIVEL MOVER")
        jogador.direcao=dir
    
    def __str__(self):
        string=""
        for line in self.grid:
            string+="\n"
            for object in line:
                string+=str(object)
        return string

    def simplify(self):
        return str(self)