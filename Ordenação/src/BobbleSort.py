valores = [5, 8, 9, 2, 1]
        
for i in range(len(valores) - 1, 0, -1):
    for j in range(0, i):
        if (valores[j] > valores[i]):
            valores[i], valores[j] = valores[j], valores[i] 

print(valores)