class ListaClientes:
    """
    Classe ListaClientes:
    Classe utilizada para registar os clientes  que se conectão com o servidor do jogo
    :param  clientes: lista de clientes que se conectaram com o servidor
    """
    def __init__(self):
        self.clientes=[]

    def connetar(self,cliente:list):
        """
        adiciona da lista de clientes  caso o endereço do cliente nao se encontre na lista
        :param cliente: identifica o cliente que se conectou ao servidor
        """
        if cliente[1] not in self.clientes:
            self.clientes.append(cliente)

    def disconectar(self,cliente:list):
        """
        remove da lista de clientes  caso o cliente se encontre na lista
        :param cliente: identifica o cliente que desconectou se do servidor
        :return:
        """
        if cliente in self.clientes:
            self.clientes.remove(cliente)

    def listar(self):
        """
        mostra a lista de clientes que estão conectados ao servidor
        :return:retorna a lista de clientes existentes
        """
        return self.clientes
