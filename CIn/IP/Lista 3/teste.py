"""
lista = [4, 25, 8, 9, 1, 7, 24, 11, 12, 74, 2, 6, 7, 9, 74, 47]

for i in range(len(lista) - 1):
    for j in range(i, len(lista) - 1):
        if lista[i] > lista[j+1]:
            lista[i], lista[j+1] = lista[j+1], lista[i]

print(lista)
"""
while True:
    lista_repetição = []
    valor = int(input())
    for a in range(2, valor + 1):
        lista = [x for x in range(a*2 + 1) if x > a]

        for i in range(2, int((a*2)**0.5) +1):
            for j in range(i*i, 2*a + 1, i):
                if j in lista:
                    lista.remove(j)
        lista_repetição += lista
    print(lista_repetição)
