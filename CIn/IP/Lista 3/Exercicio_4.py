#Missão Lazarus
print("Bem vindos, exploradores! Começaremos à Missão Lazarus!")
#planetas = input()

######DESCARTAR
planetas = "Muller - 8 - ok, Mark - 10 - ok, Pedro - 10 - falha, Marya - 7 - ok, Cleusa - 4 - falha"
######DESCARTAR

    #Fazendo a lista de planetas
lista_candidatos = planetas.split(", ")

for i in range(len(lista_candidatos)):
    lista_candidatos[i] = lista_candidatos[i].split(" - ")

    #Transformando os valores de nível habitacional em nummerico
for j in range(len(lista_candidatos)):
    lista_candidatos[j][1] = int(lista_candidatos[j][1])

#FIM Lazarus
print("Planetas armazenados. Fim da Missão Lazarus.")

#Missão Endurece
print("Hora de escolher os melhores planetas para habitarmos!")

    #Eliminando planetas incapazes
num_planetas_removidos = 0
for k in lista_candidatos:
    if lista_candidatos[lista_candidatos.index(k)][1] < 6 or lista_candidatos[lista_candidatos.index(k)][2] == "falha":
        lista_candidatos.pop(lista_candidatos.index(k))
        num_planetas_removidos += 1
    
    #Ordenando restantes

for l in range(len(lista_candidatos) - 1):
    for m in range(l, len(lista_candidatos) - 1):
        if lista_candidatos[l][1] < lista_candidatos[m+1][1]:
            lista_candidatos[l], lista_candidatos[m+1] = lista_candidatos[m+1], lista_candidatos[l]

#FIM Endurece
if lista_candidatos != []:
    nomes_planetas = 'NAda'
    for n in range(len(lista_candidatos)):
        nomes_planetas += ", " + lista_candidatos[n][0]
    nomes_planetas = nomes_planetas.replace("NAda, ", '')

    print(f"Planetas habitáveis encontrados: {nomes_planetas}.")

else:
    print("Planetas habitáveis encontrados: nenhum.")

print(f"Quantidade de planetas desconsiderados: {num_planetas_removidos}.")