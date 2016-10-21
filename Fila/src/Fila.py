# -*- coding:UTF-8 -*-

class Elemento:
    
    def __init__(self,nome):
        self.nome = nome
        self.proximo = None
        
class Fila:

    def __init__(self):
        self.inicio = None
        
    def enfileirar(self,nome):
        novo = Elemento(nome)
        if self.inicio == None:
            self.inicio = novo
        else:
            elemento = self.inicio
            while elemento.proximo != None:
                elemento = elemento.proximo
            elemento.proximo = novo
        
    def desenfileirar(self):
        if self.inicio == None:
            return None
        else:
            elemento = self.inicio
            self.inicio = elemento.proximo
            return elemento.nome
           
fila = Fila()
        
fila.enfileirar('João')
fila.enfileirar('Pedro')
fila.enfileirar('Lucas')
fila.enfileirar('Maria')
        
nome = fila.desenfileirar()

print(nome)