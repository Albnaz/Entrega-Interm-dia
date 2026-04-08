import random as rand
from Servidor.enums.objetos import Objetos

def randomizar(ordersize: int):
    """
    randomizar()
    função auxiliar da classe Cliente, cria uma lista de objetos com len ordersize
    :param: ordersize: int - numero de objetos por pedido.
    :return: a lista usada para o pedido
    """
    lista=[]
    objetos=[Objetos.QUADRADO,Objetos.TRIANGULO,Objetos.RETANGULO,Objetos.CIRCULO]
    for  i in range(ordersize):
        lista.append(objetos[rand.randint(0,len(objetos)-1)])
    return lista 

class Cliente:
    """
    Classe Cliente:
    Classe representando os pedidos que o jogador tem de realizar durante a partida.
    Representado como o seu ID e os seus objetos do pedido na representação do mapa no terminal.
    :param: ID: string - identificador do cliente.
    :param: pedido: list - pedido atual do cliente, o qual é mostrado ao cliente no mapa.
    """
    def __init__(self,ID: str):
        self.ID=ID
        self.pedido=randomizar(3)

    def getId(self):
        return self.ID
    
    def getPedido(self):
        return self.pedido
    
    def mudarpedido(self):
        self.pedido=randomizar(3)

    def __str__(self):
        string="["+str(self.ID)+":"
        for i in self.pedido:
            string+=i.value
        string+="]"
        return string
