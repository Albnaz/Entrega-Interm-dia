import threading
import time
class Dados:
    """
    Classe Dados:

    Classe utilizada para registar as acoes dos jogadores e as suas pontuações
    :param opercaoes:
    """
    def __init__(self):
        self.operacoes = {}
        self.lock = threading.Lock()
    def registar_oper(self, id:int,oper: str, variavel: str, result: str, client:tuple,timestamp: float = None):
        if timestamp is None:
            timestamp = time.time()
        registo = [id,oper,variavel, result, client, timestamp]
        with self.lock:
            if oper not in self.operacoes:
                self.operacoes[oper] = []
            self.operacoes[oper].append(registo)
    def get_operacoes(self, oper=None):
            """
            Executa a cópia do dicionário de forma a ser seguro.
            :param oper:
            :return:
            """

            with self.lock:
                if oper:
                    return self.operacoes.get(oper, [])[:]

            return {k: v[:] for k, v in self.operacoes.items()}
