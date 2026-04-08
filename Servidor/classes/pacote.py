class Pacote:
    """
    Classe Pacote:
    Classe utilizada com o objetivo de guardar os objetos que o jogador precisa para completar os pedidos dos
    clientes . Enquanto o jogador  ainda  não depositou quaisqueres objetos, o pacote é representado  como "[◼]".
    Numa situação intermédia, é representado como "[◧]". Já se a quantidade de items for igual à capacidade máxima,
    é representado  por "[◫]".
    :param len - serve para limitar a capacidade do  pacote
    """
    def __init__(self,len):
        self.maxlen= len
        self.pacote=[]

    def insertObject(self,object):
        """
        Insere o objeto do jogador na lista pacote
        :param object: objeto  ue é recebido ao jogador interagir com o pacote
        """
        self.pacote.append(object)

    def __str__(self):
        if len(self.pacote)==0:
            return"[◼]"
        elif len(self.pacote) == self.maxlen:
            return "[◫]"
        else:
            return "[◧]"