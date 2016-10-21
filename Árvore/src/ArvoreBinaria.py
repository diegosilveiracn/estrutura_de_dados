class Elemento:
    def __init__(self, valor):
        self.valor = valor
        self.ramoEsquerdo = None
        self.ramoDireito = None
        
class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
        
    def inserir(self, valor):
        if self.raiz == None:
            self.raiz = Elemento(valor)
        else:
            self.__inserir(valor, self.raiz)  
    
    def __inserir(self, valor, elemento):
        if elemento.valor > valor:
            if elemento.ramoEsquerdo == None:
                elemento.ramoEsquerdo = Elemento(valor)
            else:
                self.__inserir(valor, elemento.ramoEsquerdo)
        else:
            if elemento.ramoDireito == None:
                elemento.ramoDireito = Elemento(valor)
            else:
                self.__inserir(valor, elemento.ramoDireito)

                    
arvore = ArvoreBinaria()
        
arvore.inserir(7)
arvore.inserir(4)
arvore.inserir(9)
arvore.inserir(2)
arvore.inserir(5)
arvore.inserir(10)
arvore.inserir(8)
