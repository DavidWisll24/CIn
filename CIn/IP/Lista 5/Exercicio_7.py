#LABIIRINTO DE JAFAR

#Função Recursiva
def caminho(matriz, coord_x, coord_y, limite_y, limite_x, pisadas):
    #Se passar do limite
    if coord_x >= limite_x or coord_x < 0 or coord_y >= limite_y or coord_y < 0:
        return 0
    #Se achar a saida
    if matriz[coord_y][coord_x] == 'S':
        return 1  
    #Se for uma Parede Mágica Intransponível
    if matriz[coord_y][coord_x] == '|':
        return 0
    if matriz[coord_y][coord_x] == ',': #*Se achar um tapete espinhoso
        pisadas += 1 #Jasmine pisa no espinhos, mas segue com forças
    #Se for o terceiro espinho
    if pisadas >= 3:
        return 0
    #Se já foi visitada
    if matriz_visitados[coord_y][coord_x]:
        return 0
    

    ##Listas que juntas são vetores de movimentação da Jasmine no labirinto
    movimentos_cdy = [0, 0, 1, -1]
    movimentos_cdx = [1, -1, 0, 0] 
    caminhos_possiveis = 0 #*Por enquanto, Jasmine não sabe quantos caminhos possíveis de saida existem

    matriz_visitados[coord_y][coord_x] = True #*Marca a coordenada como já visitada

    for passos_possiveis in range(4): #*Roda uma vez para cada passo possível
        caminhos_possiveis += caminho(matriz, (coord_x + movimentos_cdx[passos_possiveis]), (coord_y + movimentos_cdy[passos_possiveis]), limite_y, limite_x, pisadas) #*Recursividade

    matriz_visitados[coord_y][coord_x] = False

    return caminhos_possiveis #*Retorna o quantas saidas tem no labirinto

#INICIO
posicao_inicial = [0, 0] #*Onde será armaznado a posição de Jasmine
pisadas = 0 #*Mostra quantas vezes ela pisou no espinho

num_linhas = int(input()) #*Recebe o número de linhas da matriz
num_colunas = int(input()) #*Recebe quantas colunas a matriz tem

matriz = [] #*Cria a matriz, ainda vazia
matriz_visitados = [] #*Cria a matriz de já pisados, ainda vazia

for linha in range(num_linhas): #*Preenche a matriz com cada linha de caracteres
    linha_matriz = str(input())
    matriz.append(list(linha_matriz[:num_colunas])) #*Recebe a linha de caracteres

for visita_linha in range(num_linhas): #*Preenche a matriz com False no tamanho da matriz original
    linha_visitados = [False for _ in range(num_colunas)]
    matriz_visitados.append(linha_visitados)

for i in matriz: #*Acessa cada linha da matriz
    for j in i: #*Acessa cada elemento da linha
        if j == "J":
            posicao_inicial = [i.index(j), matriz.index(i)]

total_caminhos = caminho(matriz, posicao_inicial[0], posicao_inicial[1], num_linhas, num_colunas, pisadas)

print(f"Existem {total_caminhos} maneira(s) de sair do labirinto!")

if total_caminhos <= 0: #*Se não houver saida para Jasmine
    print("Pelo visto Jafar conseguiu tudo que ele sempre quis, Jasmine ficara calada para sempre, ouvi dizer que ele vai espandir o reino até Ababwa")

elif total_caminhos == 1: #*Se houver apenas 1 caminho possível
    print("Ufa! Jasmine consegue escapar, mas agora precisam tirar Jafar do poder, é melhor pedirem ajuda ao gênio!")

else: #*Se houver mais de um caminho
    print("Ninguém me cala! Jasmine derruba Jafar sozinha sem a ajuda de ninguém.")