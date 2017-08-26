def merge_sort(lista):
    if len(lista) > 1:
        centro = len(lista) // 2
        sublista_esquerda = lista[:centro]
        sublista_direita = lista[centro:]
        
        merge_sort(sublista_esquerda)
        merge_sort(sublista_direita)
        
        i = j = k = 0
        while i < len(sublista_esquerda) and j < len(sublista_direita):
            if sublista_esquerda[i] < sublista_direita[j]:
                lista[k] = sublista_esquerda[i]
                i += 1
            else:
                lista[k] = sublista_direita[j]
                j += 1
            k += 1
        while i < len(sublista_esquerda):
            lista[k] = sublista_esquerda[i]
            i += 1
            k += 1
        while j < len(sublista_direita):
            lista[k] = sublista_direita[j]
            j += 1
            k += 1

valores = [5, 8, 9, 2, 1]
merge_sort(valores)
print(valores)