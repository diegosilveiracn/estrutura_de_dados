class No:
    def __init__(self, valor):
        self.valor = valor
        self.balanceamento = 0
        self.ramoEsquerdo = None
        self.ramoDireito = None

    def rotacaoSimplesDireita(self, no):
        aux = no.ramoEsquerdo
        no.ramoEsquerdo = aux.ramoDireito
        aux.ramoDireito = no
        no.balanceamento = 0
        no = aux
        
    def rotacaoSimplesEsquerda(self, no):
        aux = no.ramoDireito
        no.ramoDireito = aux.ramoEsquerdo
        aux.ramoEsquerdo = no
        no.balanceamento = 0
        no = aux