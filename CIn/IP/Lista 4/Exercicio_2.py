#RESTAM ZERO DIAS

#Definindo variáveis
caracteristicas_alvo = [] #* Lista que contem as caractéristicas do alvo
tentativas = [] #* Lista que contem cada tentativa ads linhas do tempo alternativas do Zero
ataques_inimigos = [] #* Lista com cada golpe do inimogo
perfect = True #* Vai me dizer se Zero completou todas as missões, sem falha e define o fim do programa

#FUNÇÔES
def classificacao(): #*Função que classifica os inimigos
    if caracteristicas_alvo[1] >= 7 and caracteristicas_alvo[2] == "sim": #*Verifica nível de ameaça e se está armado
        classificado = "Elite" #*Classifica de acordo
        return classificado #*Retorna a classificação
    elif caracteristicas_alvo[1] >= 7 and caracteristicas_alvo[2] == "nao": #* Repete o processo para cada classificação
        classificado = "Executor"
        return classificado
    elif caracteristicas_alvo[1] >= 4 and caracteristicas_alvo[1] < 7 and caracteristicas_alvo[2] == "sim":
        classificado = "Veterano"
        return classificado
    elif caracteristicas_alvo[1] >= 4 and caracteristicas_alvo[1] < 7 and caracteristicas_alvo[2] == "nao":
        classificado = "Operador"
        return classificado
    elif caracteristicas_alvo[1] < 4:
        classificado = "Iniciante"
        return classificado

def analise_tentativa(): #*Função que verifica cada tentativa do Zero
    resto_divisão = sum(tentativas) % len(tentativas) #* Pega o resto da divisão para verificar se a condição é valida

    if resto_divisão == 0: #* A Missão foi um sucesso
        return True
    
    else: #* Fracassou
        return False
    
def ataques_refletidos(qtd_refletidos): #*Função que verifica se os ataques foram refletidos
    for ataque in ataques_inimigos:
        if ataque % 3 == 0 or ataque % 5 == 0:
            qtd_refletidos += 1
    return qtd_refletidos

#Vamos Começar
print("Entendo… Vamos começar do começo.")

refletidos = 0 #*Definindo variável

dia_inicial = int(input()) #*Pega a quantidade de dias até completar as missões

while dia_inicial >= 0 and perfect: #*Executa cada dia
    ##Recbendo as entradas diarias
    musica = str(input()).split(" - ") #* Musica passa a ser uma lista, na qual o elemento [0] é o nome da música e [1] o seu autor

    ##Print diario
    print(f"\n====== Restam {dia_inicial} dias. ======\nEscutando: {musica[0]} - {musica[1]}")

    ##ETAPA 1
    alvo = str(input()) #* Fornece o alvo e suas caractéristicas
    caracteristicas_alvo = alvo.split(" - ") #* [0] - Nome do alvo;  [1] - Nível de ameaça; [2] - Se está armado
    caracteristicas_alvo[1] = int(caracteristicas_alvo[1]) #* Transforma o nv de ameaça de str para int

    ##CASO ESPECIAL
    if caracteristicas_alvo[0] == "DJ Electrohead" and musica[1] == "DJ Electrohead": #*COMPARA o alvo e o altor da musica
        print("DJ Electrohead é morto na sua frente. Lhe avisaram para NÃO FALAR com ele.")

    else:
        classe = classificacao() #* Classifica o alvo e retorna sua classsificação

        print(f"Analisando alvo: {caracteristicas_alvo[0]}... Classificação: {classe}") #*Print da classificação


        ##ETAPA 2
        tentativas = [int(valor_tentativa) for valor_tentativa in str(input()).split(" ")] #* Faz a lista já com valores inteiros das tentativas de Zero

        missao_concluida = analise_tentativa() #* Verifica o sucesso da mssão e retorna se foi concluida

        if missao_concluida:
            print(f"Missão Completa. | Manipulação temporal: {len(tentativas)} tentativa(s)")

            ##ETAPA 3
            qtd_refletidos = 0
            ataques_inimigos = [int(valor_ataque) for valor_ataque in str(input()).split(" ")] #* Faz a lista já com valores inteiros dos ataques do inimigo

            refletidos = ataques_refletidos(qtd_refletidos) #*Execua a função e retorna a quantidade de ataques refletidos

            print(f"Dragão refletiu {refletidos} ataque(s)!")

        else:
            print("Missão Fracassou! ZERO não foi capaz de assassinar o alvo e acabou morrendo. Nunca descobrirá o que realmente aconteceu.")
            perfect = False #* Fracassou em uma missão

    dia_inicial -= 1

#FIM
if perfect:
    print("\n====== FIM DAS MISSÕES ======\nParabéns Subject ZERO! Seu trabalho deve ser recompensado. Nova dose do seu remédio esta aqui.")