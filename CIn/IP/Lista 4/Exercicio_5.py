#DBCIn x DBIp

#FUNÇÕES
def geradores(): #*Atualiza os geradores feitos
    qtd_geradores = tempo // 100
    geradores_feitos[0] = qtd_geradores 

def distancia_inimigo(): #*Define a distancia maior entre o assassino e os sobreviventes
    distacia_1 = abs(coordenadas[0] - 0) + abs(coordenadas[1] - 8)
    distacia_2 = abs(coordenadas[0] - 0) + abs(coordenadas[1] - 0)
    distacia_3 = abs(coordenadas[0] - 8) + abs(coordenadas[1] - 8)
    distacia_4 = abs(coordenadas[0] - 8) + abs(coordenadas[1] - 0)
    distacia = max(distacia_1, distacia_2, distacia_3, distacia_4)

    if distacia == distacia_1 == distacia_2 == distacia_3 == distacia_4:
        coordenadas_inimigo = [0, 0]
    elif distacia == distacia_1:
        coordenadas_inimigo = [0, 8]
    elif distacia == distacia_2:
        coordenadas_inimigo = [0, 0]
    elif distacia == distacia_3:
        coordenadas_inimigo = [8, 8]
    elif distacia == distacia_4:
        coordenadas_inimigo = [8, 0]
    
    return distacia, coordenadas_inimigo

def por_no_mapa(): #Garante que o personagem não sai do mapa
    if coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][1] > 8:
        coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][1] -= 1
    elif coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][1] < 0:
        coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][1] += 1

    if coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][0] > 8:
        coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][0] -= 1
    elif coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][0] < 0:
        coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][0] += 1

def estruturas(nome_mapa): #*Define no mapa as posições das estruturas do jogo
    if nome_mapa == "MacMillan": #*Posição das estruturas no mapa MacMillan
        mapa[5][1] = "Shack"
        mapa[3][7] = "Jungle"
        mapa[1][5] = "LT"
    elif nome_mapa == "Autohaven": #*Posição das estruturas no mapa Autohaven
        mapa[1][6] = "Shack"
        mapa[2][2] = "Jungle"
        mapa[6][3] = "LT"
    else: #*Posição das estruturas em um mapa qualquer
        mapa[6][7] = "Shack"
        mapa[2][2] = "Jungle"
        mapa[7][1] = "LT"

def percurso(sobrevivente): #*Função do percurso
    acao = 0
    tempo_recuperado = 0

    while acao < len(caminho):
        novo_percurso(acao, sobrevivente)
        coordenada_x = coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][1]
        coordenada_y = coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][0]

        ##Caso tente sair do mapa
        if coordenada_x < 0 or coordenada_x > 8 or coordenada_y < 0 or coordenada_y > 8:
            print("❌ Travou na parede! Deixou fácil pro killer!")
            por_no_mapa()
            enganchos[sobreviventes_validos.index(sobrevivente)] += 1
            ganchos[0] += 1
            return tempo_recuperado
        
        else: #*Caso não
            estrutura = mapa[coordenada_y][coordenada_x]
            
            if estrutura == "Shack":
                print("🏃 Usou a Shack!")
                tempo_recuperado += 40
                mapa[coordenada_x][coordenada_y] = "Mato"

            elif estrutura == "Jungle":
                print("🏃 Usou a Jungle!")
                tempo_recuperado += 25
                mapa[coordenada_x][coordenada_y] = "Mato"

            elif estrutura == "LT":
                print("🏃 Usou a LT!")
                tempo_recuperado += 20
            
            elif estrutura == "Mato":
                print("🌿 Correu pelo mapa.")
                tempo_recuperado += 5

        acao += 1

    enganchos[sobreviventes_validos.index(sobrevivente)] += 1
    ganchos[0] += 1
    return tempo_recuperado

def novo_percurso(acao, sobrevivente): #*Função que calcula cada nova posição durante o percurso
    if caminho[acao] == 'd':
        coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][1] += 1 #*Move para a direita o personagem por meio de sua coordenada, ligada ao seu nome
    elif caminho[acao] == 'e':
        coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][1] -= 1 #*Move para a esquerda o personagem por meio de sua coordenada, ligada ao seu nome
    elif caminho[acao] == 'c':
        coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][0] -= 1 #*Move para cima o personagem por meio de sua coordenada, ligada ao seu nome
    elif caminho[acao] == 'b':
        coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][0] += 1 #*Move para baixo o personagem por meio de sua coordenada, ligada ao seu nome
    elif caminho[acao] == "d1":
        coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][1] -= 1 #*Move para a diagonal superior esquerda o personagem por meio de sua coordenada, ligada ao seu nome
        coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][0] -= 1
    elif caminho[acao] == "d2":
        coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][1] += 1 #*Move para a diagonal superior direita o personagem por meio de sua coordenada, ligada ao seu nome
        coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][0] -= 1
    elif caminho[acao] == "d3":
        coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][1] -= 1 #*Move para a diagonal inferior esquerda o personagem por meio de sua coordenada, ligada ao seu nome
        coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][0] += 1
    elif caminho[acao] == "d4":
        coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][1] += 1 #*Move para a diagonal inferior direita o personagem por meio de sua coordenada, ligada ao seu nome
        coordenadas_personagens[sobreviventes_validos.index(sobrevivente)][0] += 1

#INICIO
print("DBCin x DBIp, que a melhor equipe vença! 🏆")

#Formando o Mapa
mapa = [["Mato" for x in range(9)] for y in range(9)]

#Definindo Variáveis
assasinos_validos = ["Spirit", "Singularidade", "Huntress"] #*Nomes de assasinos válidos
assassino = '' #*Variável que vai armazenar o nome do assassino
sobreviventes_validos = ["Kate", "Dwight", "Ada", "Vee"] #*Nomes dos sobreviventes válidos
tempo = 0 #*Tempo para fazer os geradores
geradores_feitos = [0] #*Armazena a quantidade de geradores feitos
ganchos = [0] #*Armazena a qtd total de ganchos da partida
mortos = [] #*Armazena o personagens mortos

#Pede o assassino da vez
while assassino not in assasinos_validos: #*Enquanto o nome estiver invalido
    assassino = str(input()) #*Pede um novo nome

    if assassino in assasinos_validos: #*Se o assassino for válido
        print("Killer de acordo com o previsto! Boa partida!")

    else: #*Caso não seja
        print("Killer não previsto! Jogo será atrasado, até que a outra equipe escolha um válido!")

#Pede o mapa da vez
nome_mapa = str(input()) #*Pergunta qual mapa vai ser usado
estruturas(nome_mapa) #*Define o local de cada estrutura nesse mapa

#Pede as coordenadas iniciais dos sobreviventes
coordenadas = [int(pontos) for pontos in str(input()).split(',')] #*Define a coordenada inicial dos sobreviventes | [0] -> y; [1] -> x
coordenadas_personagens = [coordenadas for x in range(4)] #* Matriz que armazena a coordenada de cada personagem | [0] -> Kate; [1] -> Dwight; [2] -> Ada; [3] -> Vee
enganchos = [0 for n in range(4)] #*Para cada personagem, tem a quantidade de vezes que foi enganchado | [0] -> Kate; [1] -> Dwight; [2] -> Ada; [3] -> Vee

##Com base naas coordenadas definidas, define o ponto inicial do assassino e o tempo de vantagem
distancia, coordenadas_assasino = distancia_inimigo()
tempo += 60 + (distancia * 10) #* adiciona no tempo o tempo de vantagem
print(f"O(A) {assassino} nasceu na posição {coordenadas_assasino}.\nA vossa vantagem inicial de distância é de {distancia} espaços!")

#COMEÇÕ de Cada Rodada(chase)
while len(sobreviventes_validos) != 0 and geradores_feitos[0] < 5:
    sobrevivente = '' #*Variável que vai armazenar o nome do sobrevivente da vez

    #Pede o sobrevivente que vai andar
    while sobrevivente not in sobreviventes_validos: #*Enquanto o nome estiver invalido
        print(f"--- STATUS: {geradores_feitos[0]}/5 Geradores | {ganchos[0]}/12 Ganchos ---")
        sobrevivente = str(input()) #*Pede um novo

        if sobrevivente in mortos: #*Caso tenha morrido
            print(f"⚠️ O/A {sobrevivente} já tem 2 ganchos!\nEsse personagem não está previsto na sua equipe ou já tem 2 ganchos.")

        elif sobrevivente not in sobreviventes_validos: #*Caso não seja válido
            print("⚠️ Personagem não pertence à equipe!\nEsse personagem não está previsto na sua equipe ou já tem 2 ganchos.")

    #Pede o percurso que ele vai fazer
    caminho = str(input()).split(", ")

    #Executa o percurso e retorna o tempo ganho nele
    tempo_ganho = percurso(sobrevivente)
    tempo += tempo_ganho

    #Eliminando sobreviventes mortos
    index_sobrevivente = sobreviventes_validos.index(sobrevivente)
    if enganchos[index_sobrevivente] >= 2:
        mortos.append(sobreviventes_validos[index_sobrevivente])
        sobreviventes_validos.pop(index_sobrevivente)
        enganchos.pop(index_sobrevivente)
        coordenadas_personagens.pop(index_sobrevivente)

    geradores()

    #Print final da Chase
    print(f"Fim da Chase! O/A {sobrevivente} ganhou {tempo_ganho} segundos.\nO {assassino} alcançou o/a {sobrevivente} e colocou-o no gancho.")

#FINAL
print("\n=============================================")

if geradores_feitos[0] == 5: #*Caso os geradores tenham sido finalizados
    print("🎉 VITÓRIA DA EQUIPE! Fizeram os 5 geradores antes de um de vcs morrer!")

else:
    print(f"💀 DERROTA! O assassino conseguiu {ganchos[0]} ganchos antes dos geradores terminarem!")