#Definindo as variáveis
itens_essenciais = ["Capacitor de Fluxo", "Válvula de Vácuo", "Fragmento do Ponto-Zero"]
itens_raros = ["Escopeta Lendária", "Vira-Vira", "Peixinho-Dourado Mítico"]
lixo = ["Lata Enferrujada", "Bota Velha", "Cogumelo Mordido"]
inventário = []
quantidade = []
item = ''
pontos = 0
falhou = True
mapeada = False

#FASE 1
print("FASE 1:\nMarty McFly: Vamos buscar os Recursos que o Doc pediu.")

##Coletando
while item != "Fim Da Coleta!":
    item = input()

    if item != "Fim Da Coleta!":
        ###Os prints
        if item in itens_essenciais and item not in inventário:
            print("Marty McFly: Boa Embananado, estávamos precisando disso.")
        elif item in itens_essenciais and item in inventário:
            print("Marty McFly: Por via das dúvidas, vamos levar mais.")
        elif item in itens_raros:
            print("Marty McFly: Não podemos deixar uma raridade dessas pra trás né?!")
        
        ###Só coleta se não for lixo
        if item not in lixo:
            if item not in inventário:
                inventário.append(item)
                quantidade.append(1)
            else:
                ###Incrementando a quantidade pela posição do item correspondente
                quantidade[inventário.index(item)] += 1
        else:
            print("Marty McFly: Pra que eu preciso disso? Só vai encher meu inventário.")

##FIM da Coleta
print("Marty McFly: Nossa coleta termina aqui.")

##Ordenando por bubble sort
for i in range(len(quantidade) - 1):
    for j in range(i, len(quantidade) - 1):
        if quantidade[i] < quantidade[j+1]:
            quantidade[i], quantidade[j+1] = quantidade[j+1], quantidade[i]
            inventário[i], inventário[j+1] = inventário[j+1], inventário[i]

##Somando Pontos
for k in inventário:
    if k in itens_essenciais:
        pontos += 30*quantidade[inventário.index(k)]
    elif k in itens_raros:
        pontos += 10*quantidade[inventário.index(k)]
    else:
        pontos -= 5*quantidade[inventário.index(k)]

    ###Pondo os pontos entre 0 e 100
    if pontos < 0:
        pontos = 0
    elif pontos > 100:
        pontos = 100

    ###Verificando se tem algum  item essencial
    if k in itens_essenciais:
        falhou = False

##Próxima FASE?
if falhou:
    print("Marty McFly: Infelizmente não encontramos nenhum dos objetivos, não poderemos continuar com a missão.")
elif pontos < 30:
    print(f"PONTUAÇÃO DA COLETA = {pontos}")
    print("Marty McFly: Pontuação Insuficiente, não poderemos continuar com a missão.")
else:
    print(f"PONTUAÇÃO DA COLETA = {pontos}")
#FASE 2
    print()
    print("FASE 2:\nDoc Brown: De onde estão vindo esses sinais de rádio-frequência dimensional? Eles formam uma matriz perfeita!")
    ##Gerando matriz de frequencia
    i_linhas_matriz = int(input())
    j_colunas_matriz = int(input())
    matriz_frequencia = []

    for a in range(i_linhas_matriz):
        frequencias_recebidas = input()
        linha_frequencia = frequencias_recebidas.split(" - ")
        for b in range(len(linha_frequencia)):
            linha_frequencia[b] = float(linha_frequencia[b])
        matriz_frequencia.append(linha_frequencia)

    ##Gerando matriz mapeada por Doc
    ###Definindo matriz auxiliar para ão estourar os valores do index
    matriz_frequencia_analise = [[0]+linha+[0] for linha in matriz_frequencia]
    matriz_frequencia_analise.append([0]*(j_colunas_matriz + 2))
    matriz_frequencia_analise.insert(0, [0]*(j_colunas_matriz + 2))

    ###Definindo cada posição com não visitada
    matriz_mapeada = matriz_frequencia.copy()
    for c in matriz_mapeada:
        for d in range(len(c)):
            matriz_mapeada[matriz_mapeada.index(c)][d] = '.'

    ###Verificando a visinhaça
    linha = 1
    coluna = 1
    quant_movimentos = 0

    while not mapeada:
        ####Vejo se os vizinhos são todos menores
        if (matriz_frequencia_analise[linha][coluna] > matriz_frequencia_analise[linha][coluna - 1]
            and matriz_frequencia_analise[linha][coluna] > matriz_frequencia_analise[linha][coluna + 1]
            and matriz_frequencia_analise[linha][coluna] > matriz_frequencia_analise[linha + 1][coluna]
            and matriz_frequencia_analise[linha][coluna] > matriz_frequencia_analise[linha - 1][coluna]
        ):
            matriz_mapeada[linha-1][coluna-1] = 'X'
            mapeada = True

        else:
            quant_movimentos += 1
            
            ####Vendo o maior vizinho
            freq_proximas = [matriz_frequencia_analise[linha][coluna + 1], matriz_frequencia_analise[linha][coluna - 1], matriz_frequencia_analise[linha + 1][coluna], matriz_frequencia_analise[linha - 1][coluna]]

            for bubble in range(len(freq_proximas) - 1):
                for sort in range(bubble, len(freq_proximas) - 1):
                    if freq_proximas[bubble] < freq_proximas[sort + 1]:
                        freq_proximas[bubble], freq_proximas[sort + 1] = freq_proximas[sort + 1], freq_proximas[bubble]

            ####Adequando o movimento de acordo com a coordenada do maior vizinho
            if freq_proximas[0] == matriz_frequencia_analise[linha][coluna + 1]:
                matriz_mapeada[linha-1][coluna-1] = '>'
                linha = linha
                coluna = coluna + 1
            elif freq_proximas[0] == matriz_frequencia_analise[linha][coluna - 1]:
                matriz_mapeada[linha-1][coluna-1] = '<'
                linha = linha
                coluna = coluna - 1
            elif freq_proximas[0] == matriz_frequencia_analise[linha + 1][coluna]:
                matriz_mapeada[linha-1][coluna-1] = 'v'
                linha = linha + 1
                coluna = coluna
            elif freq_proximas[0] == matriz_frequencia_analise[linha - 1][coluna]:
                matriz_mapeada[linha-1][coluna-1] = '^'
                linha = linha - 1
                coluna = coluna

    ###Printando matriz mapeada
    for linha_print in matriz_mapeada:
        elemento = ''
        for coluna_print in range(len(linha_print)):
            elemento += str(matriz_mapeada[matriz_mapeada.index(linha_print)][coluna_print])
        print(elemento)
    
    print(f"Doc Brown: Os sinais vêm da posição [{linha - 1}][{coluna - 1}]!")
    print(f"Localização triangulada com sucesso após {quant_movimentos} movimentos pela grade dimensional.")

    #FASE 3
    print()
    print("FASE 3:\nDoc Brown: Está quase tudo pronto para voltarmos para casa!")

    estado_inicial = input()
    
    ##Verificando quantos vezes os bits mudaram
    potencia = 0
    binario_antigo = estado_inicial
    mudancas = 0

    ###Algoritmo de conversão binario caseiro
    while int(binario_antigo, 2) < 88:
        ####Variáveis
        binario_atual = ''
        potencia = 0
        valor_decimal = int(binario_antigo, 2) + 1

        ####Vendo até que potencia de 2 vai
        while valor_decimal//(2**(potencia+1)) != 0:
            potencia += 1
        
        ####Conversão
        for i in range(0, potencia + 1, 1):
            if valor_decimal >= 2**(potencia-i):
                binario_atual += "1"
                valor_decimal = valor_decimal - 2**(potencia-i)
            else:
                binario_atual += "0"
        
        ####Padronização
        if len(binario_atual) < 7:
            binario_atual = '0'*(7 - len(binario_atual)) + binario_atual
        
        ####Vendo quantos bits mudaram
        for new, old in zip(binario_atual, binario_antigo):
            if new != old:
                mudancas += 1

        binario_antigo = binario_atual

    ##Prints Finais
    print(f"SISTEMA SINCRONIZADO!\nDoc Brown: Marty, para acelerarmos de {int(estado_inicial, 2)} até 88 mph, o Capacitor teve que realizar {mudancas} trocas de estado nos bits de processamento!")
    print("--- #1 VICTORY ROYALE: Bem-Vindos a 1985! ---")