#A LOBOTOMY CINCORPORATION
#Malkuth, Yesod e Binah
#FUNÇÕES
def manejo_diario(sefirot): #Função que analisa o Sefirá do dia
    if sefirot == "Malkuth":
        malkuth() #*Chama a função correspondente à Malkuth
    elif sefirot == "Yesod":
        yesod()  #*Chama a função correspondente à Yesod
    elif sefirot == "Binah":
        binah()  #*Chama a função correspondente à Binah

def malkuth(): #*Função relacionada com Malkuth - Algoritmo de Ordenação de Nomes
    nomes = str(input()) #*Recebe os nomes

    if nomes == '': #*Caso não tenha nada
        dia_concluido = True
        return dia_concluido
                

    else: #*Caso tenha ao menos um nome
        lista_nomes = nomes.split() #*Armazena na variável lista_nomes uma lista com cada nome colocado

        ##Ordenação dos Nomes
        for tamanho_nome in range(len(lista_nomes) - 1): #*Ideia do Bubble Sort | Percorre cada elemento da lista
            for comparado in range(tamanho_nome, len(lista_nomes) - 1): #*Pega cada elemento seguinte ao elemento que está em análise na vez
                if len(lista_nomes[tamanho_nome]) < len(lista_nomes[comparado + 1]): #*Se for menor, troca
                    lista_nomes[tamanho_nome], lista_nomes[comparado + 1] = lista_nomes[comparado + 1], lista_nomes[tamanho_nome]

        energia_dia = (len(lista_nomes[0]) + len(lista_nomes[-1])) * 20 #*Descobrindo a energia gerada no dia pela formula específica

        if energia_dia >= energia_necessária:
            dia_concluido = True
            return dia_concluido
        else:
            dia_concluido = False
            return dia_concluido

def yesod(): #*Função relacionada com Yesod - Algoritmo de Compressão de Dados
    dados_recebidos = str(input()) + ' ' #*Recebe uma string de dados para ser comprimida | #*Adiciona o ' ' na string para o algoritmo contar o ultimo valor

    ##Algoritmo de Compressão
    aux_compressao = dados_recebidos[0] #*Guarda o valor do dado anterior | Inicialmente possui o valor do primeiro caractere
    num_aparicao = 1 #*Define inicialmente que cada caractere aparece ao menos uma vez
    dados_comprimidos = '' #*Vai armazenar os dados comprimidos
    corrompido = False #*Diz se houve problemas na compressão dos dados
    dado = 0
    while dado < len(dados_recebidos) - 1: #* para cada caractere, após o primeiro, executa uma vez
        dado += 1 
        caractere = dados_recebidos[dado] #*Entra do segundo caractere em diante, para já ter parametro de comparação

        if caractere == '&':
            corrompido = True
        elif caractere == aux_compressao: #*Verifica se o dado atual é repetido em consecutivamente
            num_aparicao += 1 #*Soma 1 para cada aparição
        else: #*Se forem dados distintos e não corrompidos
            dados_comprimidos += (str(num_aparicao) + aux_compressao if num_aparicao > 1 else aux_compressao)#*Armazena a forma comprimida de cada dado
            num_aparicao = 1 #* Retorna ao inicial
        
        aux_compressao = caractere #*Atualiza a variável

    if not corrompido: #*Caso ocorra tudo certo
        dia_concluido = True
        return dia_concluido
    else: #*Se os dados dorem corrompidos
        dia_concluido = False
        return dia_concluido

def binah(): #*Função relacionada com Binah - Algoritmo de Multiplicação de Matrizes
    pass

energia_necessária = 100 #*Energia base bara concluir o primeiro dia

#Dias de coleta
qtd_dias = int(input())

for dia in range(qtd_dias):    
    sefirot = str(input()) #* Recebe o Sefirá do Dia

    manejo_diario(sefirot) #* Vai ativar a função do sefirot correspondente

    energia_necessária += 40 #*Aumenta o nível de energia necessário para concluir o prôximo dia