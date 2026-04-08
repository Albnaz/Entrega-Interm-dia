from Servidor.Maquina.lista_clientes import ListaClientes
import socket
from Servidor.Maquina.processaCliente import ProcessaCliente
from Servidor.classes.paredes import Parede
from dados.dados import Dados
from Servidor.classes.jogador import Jogador
from Servidor.classes.contentor import Contentor
from Servidor.classes.geradorobjeto import GeradorObjeto
from Servidor.classes.clientes import Cliente
from Servidor.classes.mapa import Mapa
from Servidor.enums.objetos import Objetos
from Servidor.classes.pacote import Pacote
import Servidor

class Maquina:
    """
    Classe Maquina:
    Classe utilizada para inicializar o mapa  definir onde se  encontram cada componente do mapa e as posicoes iniciais
    dos jogadores.
    param s: permite o servidor conecta-se  a qualquer cliente que tenha a mesma porta do servidor
    :param dados: permite o registo das ações que acontecem no jogo consoante cada interacao entre os clientes e o
    servidor
    :param clientes: guarda os clientes que se conectam ao servidor
    :param mapa:  inicializa o mapa do jogo  tendo  em conta as dimensoes  x e  y recebidass  pelos parametros da
    classe
    :param  jogador1: indentifica o jogador referente ao  primeiro cliente que se conectar ao servidor
    :param  jogador1: indentifica o jogador referente ao  segundo cliente que se conectar ao servidor
    """
    def __init__(self):
        self.s = socket.socket()
        self.dados = Dados()
        self.s.bind(('', Servidor.PORT))
        self.clientes = ListaClientes()
        self.mapa = Mapa(11, 5)
        self.jogador1 = Jogador(1, 2, 2)
        self.jogador2 = Jogador(2, 8, 2)

    def execute(self):
        """
        Funcao utlizada para esperar as conexões dos clientes ao servidor do  jogo e a inserção dos componentes
        necessarios para o jogo  ser inicializado.É criada uma thread que irá receber as interacoes de cada cliente e com
        elas fazer as alteracoes correspondentes no jogo. Caso a lista de clientes nao  tenha exatamente 2 clientes o
        servidor esperará que outro cliente se conecte e quando o mesmo se conectar o servidor irá gerir as operacoes que
        o cliente envia ao servidor.
        """
        self.s.listen(10)
        print("Waiting for clients on port " + str(Servidor.PORT))
        for line in self.mapa.grid:
            line[0] = Contentor()
            line[-1] = Contentor()
            line[5] = Parede()
        for item in range(len(self.mapa.grid[0])):
            self.mapa.grid[0][item] = Parede()
            self.mapa.grid[4][item] = Parede()
        self.mapa.grid[0][5] = "[XXXXX]"
        self.mapa.grid[4][5] = "[XXXXX]"
        geradorQuadrado = GeradorObjeto(tipo=Objetos.QUADRADO)
        geradorTriangulo = GeradorObjeto(tipo=Objetos.TRIANGULO)
        geradorRetangulo = GeradorObjeto(tipo=Objetos.RETANGULO)
        geradorCirculo = GeradorObjeto(tipo=Objetos.CIRCULO)

        pacote1 = Pacote(3)
        pacote2 = Pacote(3)
        self.mapa.insertGenerator(geradorQuadrado, 2, 0)
        self.mapa.insertGenerator(geradorQuadrado, 8, 0)

        self.mapa.insertGenerator(geradorRetangulo, 2, 4)
        self.mapa.insertGenerator(geradorRetangulo, 8, 4)

        self.mapa.insertGenerator(geradorCirculo, 1, 4)
        self.mapa.insertGenerator(geradorCirculo, 9, 4)

        self.mapa.insertGenerator(geradorTriangulo, 1, 0)
        self.mapa.insertGenerator(geradorTriangulo, 9, 0)

        self.mapa.insertPackage(pacote1, 0, 2)
        self.mapa.insertPackage(pacote2, 10, 2)
        self.mapa.insertPlayer(self.jogador1)
        self.mapa.insertPlayer(self.jogador2)
        cliente1 = Cliente("A")
        cliente2 = Cliente("B")
        cliente3 = Cliente("C")


        self.mapa.insertClient(cliente1, 5, 1)
        self.mapa.insertClient(cliente2, 5, 2)
        self.mapa.insertClient(cliente3, 5, 3)

        while True:
            print("On accept...")
            connection, address = self.s.accept()
            if len(self.clientes.clientes) < 2:
                self.clientes.connetar(cliente=[connection, address])
            else:
                print("Número máximo de clientes atingido!")
            print("Client", address, " connected")
            processo_cliente = ProcessaCliente(connection, address, self.dados, self.clientes,self.mapa, self.jogador1, self.jogador2)
            processo_cliente.start()




