# -*- coding:UTF-8 -*-

class Elemento:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.inicio = None

    def adicionar(self, valor):
        novo = Elemento(valor)
        if self.inicio == None:
            self.inicio = novo
        else:
            elemento = self.inicio
            while elemento.proximo != None:
                elemento = elemento.proximo
            elemento.proximo = novo

    def exibir(self):
        elemento = self.inicio
        print(elemento.valor)
        while elemento.proximo != None:
            elemento = elemento.proximo
            print(elemento.valor)

    def remover(self, valor):
        elemento = self.inicio
        if elemento.valor == valor:
            self.inicio = elemento.proximo
        else:
            while elemento.proximo != None:
                if elemento.proximo.valor == valor:
                    elemento.proximo = elemento.proximo.proximo
                else:
                    elemento = elemento.proximo

class TabelaEspalhamento:
    def __init__(self,n):
        self.tabela = []
        for i in range(0,n):
            self.tabela.append(ListaLigada())

    def espalhamento(self,valor):
        return valor % len(self.tabela)

    def adicionar(self,valor):
        chave = self.espalhamento(valor)
        self.tabela[chave].adicionar(valor)

    def exibir(self):
        for i in range(0,len(self.tabela)):
            print('Chave:',i)
            self.tabela[i].exibir()

    def remover(self,valor):
        chave = self.espalhamento(valor)
        self.tabela[chave].remover(valor)

tabela = TabelaEspalhamento(5)

tabela.adicionar(54)
tabela.adicionar(21)
tabela.adicionar(15)
tabela.adicionar(46)
tabela.adicionar(7)
tabela.adicionar(33)
tabela.adicionar(78)
tabela.adicionar(9)
tabela.adicionar(14)
tabela.adicionar(62)
tabela.adicionar(95)
tabela.adicionar(87)

tabela.exibir()