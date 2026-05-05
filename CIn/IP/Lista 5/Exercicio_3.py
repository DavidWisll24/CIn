#A MISSÃO DE RESGATE DA ARIEL

#Função Recursiva
def resgate(caminho, resistencia, obj_gruta): #*Verifica como foi o trajeto de resgate da Ariel
    if resistencia <= 0: #*Se a resistencia dela acabar antes de terminar o trajeto
        print("A correnteza está muito forte... não consigo continuar.")
        missao_sucesso = False
        return missao_sucesso, obj_gruta #*Retorna o resultado da missão e quantos objetos ela achou no caminho
    elif caminho == []: #*Caso sobre resistencia para ela meter o sarrafo na Úsula e salvar o Principe
        missao_sucesso = True
        return missao_sucesso, obj_gruta #*Retorna o resultado da missão e quantos objetos ela achou no caminho
    else: #*Enquanto o caminho não acabar e ela tiver energia
        if caminho[0] == "Linguado": #*Caso encontre o Linguado, seu grande amigo
            print("Obrigada, Linguado! Vamos rápido!")
            resistencia += 2 #*Recupera um pouco de suas energias

        elif caminho[0] == "Polvo": #*Caso encontre os capangas da Úrsula
            print("Cuidado com os servos da bruxa!")
            resistencia -= 2 #*Gasta suas forças para se livrar deles

        elif caminho[0].isnumeric(): #*Caso tenha uma buginganga no caminho
            obj_gruta += int(caminho[0]) #*Guarda na gruta(sempre interresada em coisas diferentes)

        elif caminho[0] == '~':
            nada = "acontece" #NADA ACONTECE

        resistencia -= 1 #*Energia base gasta para percorrer o caminho

        resto_caminho = caminho[1:] #*Retira da lista caminho lugares já visitados

        resultado_missao, total_gruta = resgate(resto_caminho, resistencia, obj_gruta) #*Recebe o resultado da missão e quantos objetos ela achou no caminho

        return resultado_missao, total_gruta #*Retorna o resultado da missão e quantos objetos ela achou no caminho

#INICIO
resistencia = 6 #*Representa a resistencia inicial da Ariel
obj_gruta = 0 #*Representa a quantidade de objetos na gruta

caminho = [elementos for elementos in str(input()).split()] #*Lista que representa o trajeto percorrido por Ariel

resultado_resgate, total_gruta = resgate(caminho, resistencia, obj_gruta) #*Recebe o resultado da missão e quantos objetos ela achou no caminho

if resultado_resgate: #*Se ela conseguiu salvar o principe
    print(f"Eric foi salvo! E Ariel ainda guardou {total_gruta} bugigangas na sua gruta.")

else: #*Caso não...
    print("O príncipe afundou... Úrsula venceu desta vez.")