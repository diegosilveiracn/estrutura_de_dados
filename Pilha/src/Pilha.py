# -*- coding:UTF-8 -*-

class Elemento:
    
    def __init__(self,nome):
        self.nome = nome
        self.proximo = None

class Pilha:

    def __init__(self):
        self.topo = None

    def empilhar(self,nome):
        novo = Elemento(nome)
        if self.topo == None:
            self.topo = novo
        else:
            novo.proximo = self.topo  
            self.topo = novo
            
    def desempilhar(self):
        if self.topo == None:
            return None
        else:
            elemento = self.topo
            self.topo = elemento.proximo
            return elemento.nome
        
pilha = Pilha()
        
pilha.empilhar('João')
pilha.empilhar('Lucas')
pilha.empilhar('Pedro')
pilha.empilhar('Maria')
        
nome = pilha.desempilhar()
        
print(nome)