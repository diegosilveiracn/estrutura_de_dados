def quick_sort(lista):
    sort(lista, 0, len(lista) - 1)

def sort(lista, index_inicio, index_fim):
    index_corte = partition(lista, index_inicio, index_fim)
    
    if index_inicio < index_corte - 1:
        sort(lista, index_inicio, index_corte - 1)
    if index_corte < index_fim:
        sort(lista, index_corte, index_fim)

def partition(lista, index_inicio, index_fim):
    pivo = lista[(index_inicio + index_fim) // 2]
    i = index_inicio
    j = index_fim

    while i <= j:
        while lista[i] < pivo:
            i += 1

        while lista[j] > pivo:
            j -= 1

        if i <= j:    
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
            j -= 1

    return i

valores = [5, 8, 9, 2, 1]
quick_sort(valores)
print(valores)