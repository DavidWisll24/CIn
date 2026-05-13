#RAPUNZEL E A LENDA DO PIQUINIQUE REAL

#Função Recursiva
def caminho(palavra_chave, coord_x, coord_y, limite, qtd_max_tentativas, vitoria):
    #Se já venceu
    if vitoria:
        return True
    #Se acabar tentativas
    if qtd_max_tentativas <= 0:
        vitoria = False
        return vitoria
    #Se passar da barreira
    if coord_x >= limite or coord_x < 0 or coord_y >= limite or coord_y < 0:
        return 0
    #Se completar a palavra
    if matriz[coord_y][coord_x] == '2':
        vitoria = True 
        return vitoria  
    #Se for um espinho
    if matriz[coord_y][coord_x] == '0':
        vitoria = False
        return vitoria
    #Se já foi visitada
    if matriz_visitados[coord_y][coord_x]:
        return 0
    
    #Código da recursão

    ##Listas que juntas formam o movimento de José no labirinto
    movimentos_cdy = [0, 1, 0, -1]
    movimentos_cdx = [1, 0, -1, 0] 

    if matriz[coord_y][coord_x] not in palavra_chave: #*Se achar uma letra fora da palavra secreta
        qtd_max_tentativas -= 1 #José perde uma tentativa

    matriz_visitados[coord_y][coord_x] = True #*Marca a coordenada como já visitada

    passos_possiveis = 0
    while not vitoria and passos_possiveis < 4: #*Roda uma vez para cada passo possível
        vitoria = caminho(palavra_chave, (coord_x + movimentos_cdx[passos_possiveis]), (coord_y + movimentos_cdy[passos_possiveis]), limite, qtd_max_tentativas, vitoria) #*Recursividade
        passos_possiveis += 1
    
    matriz_visitados[coord_y][coord_x] = False
    return vitoria #*Retorna o resultado final

#INICIO
vitoria = False
print("Eu te amo tanto agora quanto da primeira vez em que eu vi você...")

num_linhas_colunas = int(input()) #*Recebe o tamanho da matriz quadrada
print("O mapa da floresta me parece esquisito, certo Pascal?")

matriz = [[] for i in range(num_linhas_colunas) if 8 >= num_linhas_colunas >= 1] #*Cria a matriz, ainda vazia
matriz_visitados = [[] for i in range(num_linhas_colunas) if 8 >= num_linhas_colunas >= 1] #*Cria a matriz, ainda vazia

print("Minha querida Rapunzel, a palavra-chave é?")
palavra_chave = list(str(input())) #*Recebe a palavra chave de Rapunzel

posicao_jose = [int(coord) for coord in str(input()).split()] #*Recebe a posição inicial de José
print("Vamos por aqui, esse deve ser o local certo para se descer!")

print("Segundo o mapa essas são as informações da floresta:")
for linha in range(len(matriz)): #*Preenche a matriz com cada linha de caracteres
    matriz[linha] = str(input()).split() #*Recebe a linha de caracteres
for visita in range(len(matriz)): #*Preenche a matriz com cada linha de caracteres
    matriz_visitados[visita] = [False for _ in range(num_linhas_colunas)] #*Recebe a linha de caracteres


qtd_max_tentativas = int(input()) #*Recebe a quantidade máxima de vezes que José pode pisar em letras que não pertencem a palavra
print("Eu não tenho todo o tempo do mundo!")

vitoria = caminho(palavra_chave, posicao_jose[0], posicao_jose[1], num_linhas_colunas, qtd_max_tentativas, vitoria)

if vitoria: #*Se concluir o desafio
    print("A CAÇADA TERMINOU! O SOL BRILHA NO HORIZONTE E O PIQUE-NIQUE REAL ESTÁ SERVIDO! JOSÉ FINALMENTE PODE DESCANSAR ENQUANTO PASCAL VIGIA A TORTA DE MAÇÃ.")

else: #*Se ele parar
    print("O SOL SE PÔS NO REINO DE CORONA E AS ÚLTIMAS LANTERNAS SE APAGARAM. JOSÉ BEZERRA VAGOU POR HORAS, MAS O DESTINO FOI CRUEL: ELE NÃO CHEGOU AO PIQUE-NIQUE. ENQUANTO O CAVALO MAXIMUS SE DELICIA COM A ÚLTIMA FATIA DE TORTA DE MAÇÃ, JOSÉ TERÁ QUE SE CONTENTAR EM DIVIDIR UMA FRUTA SILVESTRE AZEDA COM O PASCAL. A CAÇADA FOI UM FRACASSO E A FOME VENCEU DESTA VEZ.")
