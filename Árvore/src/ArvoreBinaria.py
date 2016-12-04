class No:
    def __init__(self, valor):
        self.valor = valor
        self.ramoEsquerdo = None
        self.ramoDireito = None
        
class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
        
    def inserir(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.__inserir(valor, self.raiz)  
    
    def __inserir(self, valor, no):
        if no.valor > valor:
            if no.ramoEsquerdo == None:
                no.ramoEsquerdo = No(valor)
            else:
                self.__inserir(valor, no.ramoEsquerdo)
        else:
            if no.ramoDireito == None:
                no.ramoDireito = No(valor)
            else:
                self.__inserir(valor, no.ramoDireito)

                    
arvore = ArvoreBinaria()
        
arvore.inserir(7)
arvore.inserir(4)
arvore.inserir(9)
arvore.inserir(2)
arvore.inserir(5)
arvore.inserir(10)
arvore.inserir(8)
