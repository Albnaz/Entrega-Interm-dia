class GeradorObjeto:
    """
    Classe GeradorObjeto:
    Classe utilizada para gerir  os  objetos que o jogador  vai  obter para  concluir os pedidos dos clientes.É
    representado   pelo objeto que gera.

    param tipo: identifica o tipo do  objeto gerido
    """
    def __init__(self,tipo):
        self.tipo=tipo
    
    def getTipo(self):
        return self.tipo

    def __str__(self):
        return "["+str(self.tipo)+"]"

    