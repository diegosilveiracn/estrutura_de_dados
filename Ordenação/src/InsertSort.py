valores = [5, 8, 9, 2, 1]

for i in range(1,len(valores)):
    aux = valores[i]
    j = i
    while (j > 0) and (aux < valores[j -1]):
        valores[j] = valores[j - 1] 
        j -= 1
    valores[j] = aux
    
print(valores)