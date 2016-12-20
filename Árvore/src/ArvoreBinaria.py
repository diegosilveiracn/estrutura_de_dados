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
    
    def remover(self, valor):
        self.__remover(None, self.raiz, valor)
    
    def __remover(self, no_pai, no, valor):
        if no != None:
            if no.valor != valor:
                if no.valor > valor:
                    self.__remover(self, no, no.ramoEsquerdo, valor)
                else:
                    self.__remover(self, no, no.ramoDireito, valor)
            else:
                # Remover nó folha
                if no.ramoEsquerdo == None and no.ramoDireito == None:
                    if no.valor == self.raiz.valor:
                        self.raiz = None
                    elif no_pai.ramoDireito.valor == no.valor:
                        no_pai.ramoDireito = None
                    else:
                        no_pai.ramoEsquerdo = None
                # Remover nó com uma subárvore
                elif no.ramoEsquerdo == None or no.ramoDireito == None:
                    if no.ramoEsquerdo == None:
                        if no.valor == self.raiz.valor:
                            self.raiz = no.ramoDireito
                        elif no_pai.ramoEsquerdo.valor == no.valor:
                            no_pai.ramoEsquerdo = no.ramoDireito
                        else:
                            no_pai.ramoDireito = no.ramoDireito
                    else:
                        if no.valor == self.raiz.valor:
                            self.raiz = no.ramoEsquerdo
                        elif no_pai.ramoEsquerdo == no.valor:
                            no_pai.ramoEsquerdo = no.ramoEsquerdo
                        else: 
                            no_pai.ramoDireito = no.ramoEsquerdo
                # Remover nó com duas subárvores
                else:
                    nodo = no.ramoEsquerdo
                    anterior = no
                    
                    while nodo.ramoDireito != None:
                        anterior = nodo
                        nodo = nodo.ramoDireito
                    
                    if nodo.ramoEsquerdo == None:
                        anterior.ramoDireito = None # É uma folha
                    else:
                        anterior.ramoDireito = nodo.ramoEsquerdo
                        
                    if no.valor == self.raiz.valor:
                        self.raiz = nodo
                        nodo.ramoEsquerdo = no.ramoEsquerdo
                        nodo.ramoDireito = no.ramoDireito
                    elif no_pai.ramoEsquerdo.valor == no.valor:
                        no_pai.ramoEsquerdo = nodo
                    else:
                        no_pai.ramoDireito = nodo     
                    
arvore = ArvoreBinaria()
        
arvore.inserir(7)
arvore.inserir(4)
arvore.inserir(9)
arvore.inserir(2)
arvore.inserir(5)
arvore.inserir(10)
arvore.inserir(8)