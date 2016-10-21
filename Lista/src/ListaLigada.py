# -*- coding:UTF-8 -*-

class Elemento:
    
    def __init__(self,nome):
        self.nome = nome
        self.proximo = None
        
class ListaLigada:
    
    def __init__(self):
        self.inicio = None
        
    def adicionar(self, nome):
        novo = Elemento(nome)
        if self.inicio == None:
            self.inicio = novo
        else:
            elemento = self.inicio
            while elemento.proximo != None:
                elemento = elemento.proximo
            elemento.proximo = novo
            
    def exibir(self):
        elemento = self.inicio
        print(elemento.nome)
        while elemento.proximo != None:
            elemento = elemento.proximo
            print(elemento.nome)
    
    def remover(self, nome):
        elemento = self.inicio
        if elemento.nome == nome:
            self.inicio = elemento.proximo
        else:
            while elemento.proximo != None:
                if elemento.proximo.nome == nome:
                    elemento.proximo = elemento.proximo.proximo
                else:
                    elemento = elemento.proximo

lista = ListaLigada()

lista.adicionar('João')
lista.adicionar('Pedro')
lista.adicionar('Marcos')
lista.adicionar('Lucas')

lista.remover('Pedro')

lista.exibir()