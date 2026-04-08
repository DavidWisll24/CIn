#Missão Lazarus
print("Bem vindos, exploradores! Começaremos à Missão Lazarus!")
#planetas = input()

######DESCARTAR
planetas = "Muller - 8 - ok, Mark - 3 - ok, Pedro - 10 - falha, Marya - 7 - ok, Cleusa - 4 - falha"
######DESCARTAR

lista_candidatos = planetas.split(", ")

for i in range(len(lista_candidatos)):
    lista_candidatos[i] = lista_candidatos[i].split(" - ")

    #Transformando os valores de nível habitacional em nummerico
for j in range(len(lista_candidatos)):
    lista_candidatos[j][1] = int(lista_candidatos[j][1])

#Missão Endurece
    #Eliminando planetas incapazes
for k in range(len(lista_candidatos)):
    if lista_candidatos[j][1] < 6 or lista_candidatos[j][2] == "falha":
        lista_candidatos.pop(j)
    
    #Ordenando restantes
