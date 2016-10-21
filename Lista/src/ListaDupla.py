# -*- coding:UTF-8 -*-

class Elemento:
    
    def __init__(self,nome):
        self.anterior = None
        self.nome = nome
        self.proximo = None
        

class ListaDuplamenteLigada:
    
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
            novo.anterior = elemento
            
    def exibir(self):
        elemento = self.inicio
        print(elemento.nome)
        while elemento.proximo != None:
            elemento = elemento.proximo
            print(elemento.nome)
            
        while elemento.anterior != None:
            elemento = elemento.anterior
            print(elemento.nome)
            
    def remover(self, nome):
        elemento = self.inicio
        if elemento.nome == nome:
            self.inicio = elemento.proximo
            self.inicio.anterior = None
        else:
            while elemento != None:
                if elemento.nome == nome:
                    if elemento.proximo != None:
                        elemento.anterior.proximo = elemento.proximo
                        elemento.proximo.anterior = elemento.anterior
                    else:
                        elemento.anterior.proximo = None
                elemento = elemento.proximo
                            
lista = ListaDuplamenteLigada()

lista.adicionar('João')
lista.adicionar('Pedro')
lista.adicionar('Marcos')
lista.adicionar('Lucas')

lista.remover('Pedro')

lista.exibir()