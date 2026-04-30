#A LOBOTOMY CINCORPORATION
#Malkuth, Yesod e Binah
#FUNÇÕES
def manejo_diario(sefirot): #Função que analisa o Sefirá do dia
    if sefirot == "Malkuth":
        resultado_dia = malkuth() #*Chama a função correspondente à Malkuth e recebe o resultado do dia(valor booleano)
    elif sefirot == "Yesod":
        resultado_dia = yesod()  #*Chama a função correspondente à Yesod e recebe o resultado do dia(valor booleano)
    elif sefirot == "Binah":
        resultado_dia = binah()  #*Chama a função correspondente à Binah e recebe o resultado do dia(valor booleano)
    return resultado_dia

def malkuth(): #*Função relacionada com Malkuth - Algoritmo de Ordenação de Nomes
    print("Hoje é o dia da Malkuth!\nMalkuth: Ah, onde estão meus modos! Malkuth se apresentando!\nMalkuth: Estamos responsáveis hoje por organizar por tamanho nossa lista de funcionários do time de controle, vamos entregar com resultados perfeitos!\n")
    
    nomes = str(input()) #*Recebe os nomes

    if nomes == '': #*Caso não tenha nada
        print("Malkuth: Pessoal?! Onde está todo mundo?! Isso é inaceitável!\n")
        dia_concluido = False
        return dia_concluido
                

    else: #*Caso tenha ao menos um nome
        lista_nomes = nomes.split() #*Armazena na variável lista_nomes uma lista com cada nome colocado

        ##Ordenação dos Nomes
        for tamanho_nome in range(len(lista_nomes) - 1): #*Ideia do Bubble Sort | Percorre cada elemento da lista
            for comparado in range(tamanho_nome, len(lista_nomes) - 1): #*Pega cada elemento seguinte ao elemento que está em análise na vez
                if len(lista_nomes[tamanho_nome]) > len(lista_nomes[comparado + 1]): #*Se for menor, troca
                    lista_nomes[tamanho_nome], lista_nomes[comparado + 1] = lista_nomes[comparado + 1], lista_nomes[tamanho_nome]

        #Print de cada nome ordenado
        mostrar_nomes = ''
        for nome in lista_nomes:
            mostrar_nomes += nome + ' '

        print(mostrar_nomes[:len(mostrar_nomes) - 1]) #Printa os nomes ordenados e sem o espaço estra no fim 

        energia_dia = (len(lista_nomes[0]) + len(lista_nomes[-1])) * 20 #*Descobrindo a energia gerada no dia pela formula específica

        print(f"Energia Coletada: {energia_dia} / {energia_necessaria}")

        if energia_dia >= energia_necessaria:
            print("Malkuth: O treino vespertino de hoje foi um sucesso! Estarei esperando vocês no período noturno, pessoal!\n")
            dia_concluido = True
            return dia_concluido
        else:
            print("Malkuth: Ah não.. não conseguimos energia suficiente... amanhã eu dobrarei a carga horária para que a gente possa concluir o expediente com excelência!\n")
            dia_concluido = False
            return dia_concluido

def yesod(): #*Função relacionada com Yesod - Algoritmo de Compressão de Dados
    print("Hoje é dia do Yesod!\nYesod: Você é a cabeça dessa corporação, você deve agir como um exemplo para os outros e fazer certeza que esse dia passe coordialmente seguindo as regras.\nYesod: Hoje estamos com um problema a resolver. Você é um progamador, não é? Hoje recebemos vários caracteres, e você terá de as comprimir para facilitar as informações.\n")

    dados_recebidos = str(input()) + ' ' #*Recebe uma string de dados para ser comprimida | #*Adiciona o ' ' na string para o algoritmo contar o ultimo valor

    ##Algoritmo de Compressão
    aux_compressao = dados_recebidos[0] #*Guarda o valor do dado anterior | Inicialmente possui o valor do primeiro caractere
    num_aparicao = 1 #*Define inicialmente que cada caractere aparece ao menos uma vez
    dados_comprimidos = '' #*Vai armazenar os dados comprimidos
    corrompido = False #*Diz se houve problemas na compressão dos dados
    dado = 0
    while dado < len(dados_recebidos) - 1 and not(corrompido): #* para cada caractere, após o primeiro, executa uma vez
        dado += 1 
        caractere = dados_recebidos[dado] #*Entra do segundo caractere em diante, para já ter parametro de comparação

        if caractere == '&' or dados_recebidos[0] == '&':
            corrompido = True
            dados_comprimidos += ((str(num_aparicao) + aux_compressao if num_aparicao > 1 else aux_compressao) if dados_recebidos[0] != '&' else '')
        elif caractere == aux_compressao: #*Verifica se o dado atual é repetido em consecutivamente
            num_aparicao += 1 #*Soma 1 para cada aparição
        else: #*Se forem dados distintos e não corrompidos
            dados_comprimidos += (str(num_aparicao) + aux_compressao if num_aparicao > 1 else aux_compressao)#*Armazena a forma comprimida de cada dado
            num_aparicao = 1 #* Retorna ao inicial
        
        aux_compressao = caractere #*Atualiza a variável

    if not corrompido: #*Caso ocorra tudo certo
        print(f"Yesod: Aqui está a lista de caracteres comprimidos: '{dados_comprimidos}'\n")
        dia_concluido = True
        return dia_concluido
    else: #*Se os dados dorem corrompidos
        print(f"Yesod: Os caracteres de hoje estavam corrompidas... devemos encerrar o dia mais cedo e investigar.\nYesod: Pelo menos, essas informações ainda estão conosco: '{dados_comprimidos}'\n")
        dia_concluido = False
        return dia_concluido

def binah(): #*Função relacionada com Binah - Algoritmo de Multiplicação de Matrizes
    print("Hoje é o dia da Binah.\nBinah: ...Você chegou.\nBinah: Você já deve saber o que fazer. Espero um bom resultado vindo de você.\n")

    linha1_matriz1, linha2_matriz1, linha3_matriz1 = [int(elemento_l1) for elemento_l1 in str(input()).split()], [int(elemento_l1) for elemento_l1 in str(input()).split()], [int(elemento_l2) for elemento_l2 in str(input()).split()] #*Recebe cada linha da matriz 1 e converte direto para uma lista de inteiros
    matriz_1 =  [linha1_matriz1, linha2_matriz1, linha3_matriz1] #*Criando a matriz 1

    linha1_matriz2, linha2_matriz2, linha3_matriz2 = [int(elemento_l1) for elemento_l1 in str(input()).split()], [int(elemento_l1) for elemento_l1 in str(input()).split()], [int(elemento_l2) for elemento_l2 in str(input()).split()] #*Recebe cada linha da matriz 2 e converte direto para uma lista de inteiros
    matriz_2 =  [linha1_matriz2, linha2_matriz2, linha3_matriz2] #*Criando a matriz 1

    matriz_resultante = [] #*Variável que armazenará a matriz resultante da multiplicação

    for i in range(3): #*Range 3 porque são matrizes 3x3
        linha_matriz_resultante = [] #*Vai armazenar temporariamente a linha da matriz
        for j in range(3):
            elemento = matriz_1[i][0]*matriz_2[0][j] + matriz_1[i][1]*matriz_2[1][j] + matriz_1[i][2]*matriz_2[2][j] #*Calcula elemento por elemento da matriz
            linha_matriz_resultante.append(elemento) #*Adiciona o elemento na linha
        matriz_resultante.append(linha_matriz_resultante) #*Após completa, adiciona a linha na matriz
    
    energia_dia = matriz_resultante[0][0] + matriz_resultante[1][1] + matriz_resultante[2][2] #*Calcula a energia do dia pela soma da diagonal da matriz resultante

    #Print da Matriz Resultante
    for linha in matriz_resultante:
        print(linha)
    print()
    print(f"Energia Coletada: {energia_dia} / {energia_necessaria}")

    if energia_dia >= energia_necessaria:
        print("Binah: O expediente foi concluído. Não cometa os mesmos erros amanhã.\n")
        dia_concluido = True
        return dia_concluido
    else:
        print("Binah: É realmente uma sensação única te ver falhando...\n")
        dia_concluido = False
        return dia_concluido

#Inicio
print("Hoje é o dia da Lobotomy CinCorporation!\n")

#Os Sefirás
sefira = ["Malkuth", "Yesod", "Binah"]

#Dias de coleta
qtd_dias = int(input())
relatorio_final = [] #*Lista que vai receber valores booleanos para cada dia, dizendo se foi falho ou não
energia_necessaria = 100 #*Energia base para concluir o primeiro dia

for dia in range(qtd_dias): #*Executa cada dia que ocorreu
    print(f"Angela: Hoje é o dia {dia + 1} de {qtd_dias}. Espero mais um expediente concluído com excelência.")

    sefirot = str(input()) #* Recebe o Sefirá do Dia

    if sefirot not in sefira: #*Não é um Sefirá válido
        print("Angela: Essa sefirot não está disponível hoje.\n")
        relatorio_final.append(False) #*Falha automaticamente o dia

    else: #*É um Sefirá válido
        resultado_dia = manejo_diario(sefirot) #* Vai ativar a função do sefirot correspondente e pegar o valor que informa o estado do dia(falha ou concluido com sucesso)
        relatorio_final.append(resultado_dia) #*Recebe se o dia falhou ou não

    energia_necessaria += 40 #*Aumenta o nível de energia necessário para concluir o prôximo dia

#PRINTS FINAIS
print("Angela: O relatório dessa semana está pronto.")

for dia_concluido in range(len(relatorio_final)): #*Para cada dia no relatorio, executa uma vez e vê a validade
    if relatorio_final[dia_concluido]: #*Dia sucesso
        print(f"Dia {dia_concluido + 1} | Status: Energia necessária adquirida.")
    else: #*Dia falho
        print(f"Dia {dia_concluido + 1} | Status: Energia necessária não adquirida.")