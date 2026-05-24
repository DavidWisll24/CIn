#O PARADOXO DE NEYMAR: A LISTA FINAL DO ANCELOTTI 🤨

#Funação
def ordenar(jogadores_candidatos): #*Função para organizar do melhor para o pior jogador
    ordenado = dict() #*Dicionário que receberá os valores ordenados
    for posicao in range(len(jogadores_candidatos)): #*Realiza para cada jogador
        ###Definindo Variáveis
        score_maior = mais_gols = -1.1
        valor = 0
        key_maior = ''

        for i in jogadores_candidatos: #*Para cada seleção roda uma vez | i recebe a chave do primeiro e segue de um em um
            ###Calculando o Ancelloti Score
            gols, ass, dri, lesoes = jogadores_candidatos[i]

            if i == "Neymar":
                score_atual  = (gols * 5) + (ass * 3) + (dri * 1) - (lesoes * 0) + 20
            else:
                score_atual  = (gols * 5) + (ass * 3) + (dri * 1) - (lesoes * 10)
            
            ###Descobre o melhor
            if score_atual > score_maior or score_maior == -1.1: #*Se fez mais Ancelotti Score
                valor = jogadores_candidatos[i]
                score_maior = score_atual
                key_maior = i
                mais_gols = gols

            elif score_atual == score_maior: #*Se fez pontos iguais
                if gols > mais_gols: #*Ve quem tem mais gols
                    valor = jogadores_candidatos[i]
                    score_maior = score_atual
                    key_maior = i
                    mais_gols = gols

                elif gols == mais_gols: #*Se for a mesma saldo de gols
                    if i < key_maior: #*Compara o nome
                        valor = jogadores_candidatos[i]
                        score_maior = score_atual
                        key_maior = i
                        mais_gols = gols

        ordenado[key_maior] = (score_maior,) + valor#*Adiciona o valor no dicionário ordenado
        jogadores_candidatos.pop(key_maior) #*Apaga valores ordenados do dicionário já ordenados 

    return ordenado

#INICIO
jogadores = dict()
print("Conexão CBF e CIn-UFPE estabelecida! Processando os dados da convocação rumo ao Hexa...\n")

vagas = int(input()) #*Diz quantas vagas tem para a copa

if vagas == 0: #*Se não houver vagas
    print("Vixe, zero vagas? Parece que a panela já ta formada e o mister já tem os 26 nomes na cabeça.")

else: #*Se hover vagas
    relatorio = ''
    while relatorio != "A coletiva vai começar": #*Enquanto não começar a coletiva, analisa
        relatorio = str(input()) #*Pede o relatório

        if relatorio != "A coletiva vai começar":
            dados = relatorio.split(" - ") #*Pega os dados da partida
            nome_jogador = dados[0].split(' ', 1)[1] #*Pega o nome do jogador
            gols, assistencias, dribles, lesoes = int(dados[1]), int(dados[2]), int(dados[3]), int(dados[4]) #*Pega os dados do jogador
            
            ##Prints Menino Ney
            if nome_jogador == "Neymar" and lesoes == 0: #*Jogou sem se lesionar
                print("O homem jogou! A esperanca do hexa respira.")
            
            elif nome_jogador == "Neymar" and lesoes == 1: #*Se lesionou no jogo
                print("Neymar machucou... Mas deixa ele recuperar, na Copa ele decide!")

            ##Prints Jogadores
            elif lesoes == 1:
                print(f"Ih, {nome_jogador} foi pro estaleiro. Ancelotti ta preocupado.")

            elif nome_jogador in jogadores:
                print(f"Mais um jogo pra conta de {nome_jogador}.")
            
            else:
                print(f"Vamos ver o que Ancelotti achará de {nome_jogador}.")
            
            if nome_jogador in jogadores: #*Caso esse jogador já tenha jogado
                gols_antigos, assistencias_antigos, dribles_antigos, lesoes_antigos = jogadores[nome_jogador]
                jogadores[nome_jogador] = (gols + gols_antigos, assistencias + assistencias_antigos, dribles + dribles_antigos, lesoes + lesoes_antigos) #*Incrementa os dados
            
            else: #*Caso o jogador não tenha jogado antes 
                jogadores[nome_jogador] = (gols, assistencias, dribles, lesoes) #*Adiciona os dados no banco

        elif jogadores == {}: #*Se não foi analisado nenhum jogador
            print("Ue, a coletiva começou mas ninguém foi analisado? O professor vai convocar os gandulas?")
            relatorio = ''
        
    else:
        jogadores = ordenar(jogadores)
        print("\n--- CONVOCADOS PARA O HEXA ---")

        limite = 0 #*Garante que não vai passar do limite de convocações
        convocados = dict()

        for convado in jogadores: #*Printa os jogadores convocados
            limite += 1
            if limite <= vagas:
                print(f"{limite}. {convado} - {jogadores[convado][0]} pts (G: {jogadores[convado][1]}, A: {jogadores[convado][2]})")
                convocados[convado] = True #*Guarda quem foi convocado

        if "Neymar" in convocados: #*CHAMOU O CRAQUE
            print("Prepara o pagode e a caixa de som, o Ney ta on!")
        
        else: #*Brasil chorou
            print("Eita... Ancelotti bancou a tática e deixou o menino Ney de fora!")
        
        if limite < vagas and "Neymar" not in convocados: #*Caso não tenha enchido, a esperança não morre
            print("Se liga, professor... ainda tem espaço pra o Ney!")

        elif limite < vagas: #*Se chamou o Ney, mas não encheu
            print("A lista não encheu, mas com o camisa 10 lá dentro, Ancelotti já tá com a cabeça no Hexa.")