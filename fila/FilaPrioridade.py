# -*- coding:UTF-8 -*-

class Elemento:
    
    def __init__(self,nome,prioridade):
        self.nome = nome
        self.prioridade = prioridade
        self.proximo = None
        
class FilaPrioridade:

    def __init__(self):
        self.inicio = None
    
    def enfileirar(self,nome,prioridade):
        novo = Elemento(nome,prioridade)
        if self.inicio == None:
            self.inicio = novo
        elif self.inicio.prioridade < novo.prioridade:
            novo.proximo = self.inicio
            self.inicio = novo
        else:
            elemento = self.inicio
            while (elemento.proximo != None and 
                   elemento.proximo.prioridade > novo.prioridade):
                elemento = elemento.proximo
            novo.proximo = elemento.proximo
            elemento.proximo = novo
        
    def desenfileirar(self):
        if self.inicio == None:
            return None
        else:
            elemento = self.inicio
            self.inicio = elemento.proximo
            return elemento.nome
           
fila = FilaPrioridade()
        
fila.enfileirar('João', 1)
fila.enfileirar('Pedro', 5)
fila.enfileirar('Lucas', 2)
fila.enfileirar('Maria', 0)
        
nome = fila.desenfileirar()

print(nome)
