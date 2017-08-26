# -*- coding:UTF-8 -*-

class Elemento:
    
    def __init__(self,nome):
        self.nome = nome
        self.proximo = None
        
class ListaCircular:
    
    def __init__(self):
        self.inicio = None
        
    def adicionar(self, nome):
        novo = Elemento(nome)
        if self.inicio == None:
            self.inicio = novo
            novo.proximo = self.inicio
        else:
            elemento = self.inicio
            while elemento.proximo.nome != self.inicio.nome:
                elemento = elemento.proximo
            elemento.proximo = novo
            novo.proximo = self.inicio
    
    def exibir(self):
        elemento = self.inicio
        print(elemento.nome)
        while elemento.proximo.nome != self.inicio.nome:
            elemento = elemento.proximo
            print(elemento.nome)
        print(elemento.proximo.nome)
            
    def remover(self, nome): 
        elemento = self.inicio
    
        if elemento.nome == nome:
            self.inicio = elemento.proximo
    
            while elemento.proximo.nome != nome:
                elemento = elemento.proximo
            elemento.proximo = self.inicio
        else:
            while elemento.proximo.nome != nome:
                elemento = elemento.proximo
            elemento.proximo = elemento.proximo.proximo

lista = ListaCircular()

lista.adicionar('João')
lista.adicionar('Pedro')
lista.adicionar('Marcos')
lista.adicionar('Lucas')

lista.remover('João')

lista.exibir()