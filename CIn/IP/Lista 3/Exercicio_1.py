#Verificando quantos ocorrências vão surgir
num_ocorrencias = int(input())

print("Édipo: Inicializando sistema de embarque. Tripulantes atuais: Zaphod Beeblebrox, Ford Prefect, Arthur Dent, Marvin")

#Definindo os primeiros tripulantes
tripulantes = ["Zaphod Beeblebrox", "Ford Prefect", "Arthur Dent", "Marvin"]

for _ in range(num_ocorrencias):
    #Qual o evento dá vez
    ocorencia = input()

    #Transformando string em uma lista
    evento = ocorencia.split()

    if "mover" in evento:
        atual_tripulante = " ".join(evento[1:-1:1])
    else:
        atual_tripulante = " ".join(evento[1::1])
    
    #Ordenando a tripulação
    if evento[0] == 'embarcar':
        tripulantes.append(atual_tripulante)

    elif evento[0] == 'mover':
        if evento[1] in tripulantes:
            tripulantes.insert(int(evento[-1]), tripulantes.pop(tripulantes.index(atual_tripulante)))

    elif evento[0] == 'remover':
        if atual_tripulante in tripulantes:
            tripulantes.remove(atual_tripulante)

    elif evento[0] == 'priorizar':
        if atual_tripulante in tripulantes:
            tripulantes.insert(0, tripulantes.pop(tripulantes.index(atual_tripulante)))

    #Prints especiais
    if ( (evento[0] == "mover" and "Zaphod Beeblebrox" in ocorencia and evento[-1] == "0") 
        or (evento[0] == "priorizar" and "Zaphod Beeblebrox" in ocorencia)
    ):
        print("EU SOU O PRESIDENTE DA GALAXIA! Primeiro lugar é pouco!")

    elif ( (evento[0] == "mover" and "Ford Prefect" in ocorencia and evento[-1] == "0") 
        or (evento[0] == "priorizar" and "Ford Prefect" in ocorencia)
    ):
        print("Sou um escritor do Guia! Mereço destaque!")

    elif evento[0] == "remover" and "Marvin" in ocorencia:
        print("Ninguem se importa comigo mesmo. Tchau")

    elif evento[0] == "remover" and "Arthur Dent" in ocorencia:
        print("Eu só queria poder tomar chá... vou descer no próximo planeta")

    elif evento[0] == "embarcar" and "Trillian" in ocorencia:
        print("Finalmente alguém sensata a bordo! Bem-vinda, Trillian!")

#FIM do programa
if len(tripulantes) >= 3:
    print(f"Édipo: Graças à improbabilidade, os novos comandantes são: {tripulantes[0]}, {tripulantes[1]} e {tripulantes[2]}.")

    if tripulantes[3::1] != []:
        print("Convocando tripulantes:")
        for convocado in tripulantes[3::1]:
            print(f"- {convocado}")

elif len(tripulantes) >= 2 and len(tripulantes) != 0:
    print("Convocando tripulantes:")
    for convocado in tripulantes:
        print(f"- {convocado}")

else:
    print("Édipo: Graças à improbabilidade, os novos comandantes são: ninguém... a nave está vazia!")