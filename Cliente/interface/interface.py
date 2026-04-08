import socket
import json
import Cliente
import os

class Interface:
    """
    Classe  Interface:
    Classe utilizada com o objetivo do cliente poder  interagir  com o servidor.Ao executar a funcao  execute o cliente
    poderá mandar  uma mensagem que ira alterar o estado de componentes do servidor.
    param  connection: permite a comunicação  com o servidor via rede.
    """
    def __init__(self):
        self.connection = socket.socket()
        self.connection.connect((Cliente.SERVER_ADDRESS,Cliente.PORT))

    # ----- enviar e receber strings, inteiros e objetos----- #
    def receive_str(self,connect, n_bytes: int) -> str:
        """
        :param n_bytes: The number of bytes to read from the current connection
        :return: The next string read from the current connection
        """
        data = connect.recv(n_bytes)
        return data.decode()

    def send_str(self,connect, value: str) -> None:
        try:
            connect.send(value.encode())
        except Exception as e:
            print("O servidor fechou!")
            os._exit(0)

    def send_int(self,connect:socket.socket, value: int, n_bytes: int) -> None:

        connect.send(value.to_bytes(n_bytes, byteorder="big", signed=True))

    def receive_int(self,connect: socket.socket, n_bytes: int) -> int:

        data = connect.recv(n_bytes)
        return int.from_bytes(data, byteorder='big', signed=True)

    def receive_object(self, connection):
        try:
            size = self.receive_int(connection, Cliente.INT_SIZE)
            data = b""
            while len(data) < size:
                print(len(data))
                packet = connection.recv(size - len(data))
                if not packet:
                    raise ConnectionError("Ligação perdida")
                data += packet
            return json.loads(data.decode('utf-8'))
        except (MemoryError):
            return "a"
        except (json.decoder.JSONDecodeError):
            print("O servidor fechou!")
            os._exit(0)

    def send_object(self, connection, obj):
        data = json.dumps(obj).encode('utf-8')
        size = len(data)
        self.send_int(connection, size, Cliente.INT_SIZE)
        connection.sendall(data)  # sendall garante envio completo

    def execute(self):
            """
            A funcao permite enviar mensagens que serão interpretadas pelo  servidor e por cada interacao  o servidor
            irá retornar o resultado  da  mensagem  enviada pelo  cliente
            """
            print("O jogo vai comecar!!")
            res = ""

            while res != ".":
                recieve = self.receive_object(self.connection)
                print(recieve)
                print("W: ↑ | A: ← | S: ↓ | D: → | E: Interagir\n")
                res: str = input()

                if res =="w":
                    self.send_str(self.connection, Cliente.UP)
                elif res =="s":
                    self.send_str(self.connection, Cliente.DOWN)
                elif res =="a":
                    self.send_str(self.connection, Cliente.LEFT)
                elif res =="d":
                    self.send_str(self.connection, Cliente.RIGHT)
                elif res =="e":
                    self.send_str(self.connection, Cliente.INTERACT)
                else:
                    continue
            self.send_str(self.connection, Cliente.END_OP)
            self.connection.close()

