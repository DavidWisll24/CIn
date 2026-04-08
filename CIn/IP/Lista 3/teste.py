"""
lista = [4, 25, 8, 9, 1, 7, 24, 11, 12, 74, 2, 6, 7, 9, 74, 47]

for i in range(len(lista) - 1):
    for j in range(i, len(lista) - 1):
        if lista[i] > lista[j+1]:
            lista[i], lista[j+1] = lista[j+1], lista[i]

print(lista)
"""
lista_candidatos = [["ababa", "baba"], ["vdvd", "cmcmc"], ["g"]]

nomes_planetas = 'nada'
for n in range(len(lista_candidatos)):
    nomes_planetas += ", " + lista_candidatos[n][0]
nomes_planetas = nomes_planetas.replace("nada, ", '')
print(nomes_planetas)