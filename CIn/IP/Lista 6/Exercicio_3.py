#O DIAGNÓSTICO DO CANARINHO

#FUNÇÕES
def ordenar(selecoes_copa): #*Função para organizar do melhor para o pior jogador
    ordenado = dict() #*Dicionário que receberá os valores ordenados
    for posicao in range(len(selecoes_copa)): #*Realiza para cada jogador
        ###Definindo Variáveis
        maior = maior_saldo = -1 
        valor = 0
        key_nova = ''
        key_maior = ''

        for i in selecoes_copa: #*Para cada seleção roda uma vez | i recebe a chave do primeiro e segue de um em um
            ###Descobre o maior
            if selecoes_copa[i]['pontos'] > maior: #*Se fez mais pontos
                valor = selecoes_copa[i]
                maior = selecoes_copa[i]['pontos']
                key_nova = f"{posicao + 1}"
                key_maior = i
                maior_saldo = selecoes_copa[i]['saldo'] 

            elif selecoes_copa[i]['pontos'] == maior: #*Se fez pontos iguais
                saldo_atual = selecoes_copa[i]['saldo'] 
                if saldo_atual > maior_saldo: #*Ve quem tem maior saldo de gols
                    valor = selecoes_copa[i]
                    maior_saldo = saldo_atual
                    maior = selecoes_copa[i]['pontos']
                    key_nova = f"{posicao + 1}"
                    key_maior = i

                elif saldo_atual == maior_saldo: #*Se for a mesma saldo de gols
                    if i < key_maior: #*Compara o nome
                        valor = selecoes_copa[i]
                        maior = selecoes_copa[i]['pontos']
                        maior_saldo = saldo_atual
                        key_nova = f"{posicao + 1}"
                        key_maior = i

        ordenado[key_nova] = (valor, key_maior) #*Adiciona o valor no dicionário ordenado
        selecoes_copa.pop(key_maior) #*Apaga valores ordenados do dicionário já ordenados 

    return ordenado

#INICIO
##Definições iniciais
jogadores_brasileiros = list() #*Cria uma lista para armazenar as tuplas dos jogadores
gols_brasil = dict() #*Guarda cada jogador que pontuou nos jogos
estatisca_brasil = {'pontos':0,'vitorias':0, 'derrotas':0, 'empates':0, 'saldo':0} #*Estátisticas
estatisca_marrocos = {'pontos':0,'vitorias':0, 'derrotas':0, 'empates':0, 'saldo':0} #*Estátisticas
estatisca_haiti = {'pontos':0,'vitorias':0, 'derrotas':0, 'empates':0, 'saldo':0} #*Estátisticas
estatisca_escocia = {'pontos':0,'vitorias':0, 'derrotas':0, 'empates':0, 'saldo':0} #*Estátisticas
selecoes_copa = {'Brasil':estatisca_brasil, 'Marrocos':estatisca_marrocos, 'Escócia':estatisca_escocia, "Haiti":estatisca_haiti} #*Estátisticas
gols_marcados = gols_sofridos = 0 #*Variáveis que armazenam os gols sofridos e marcados pelo BRASIL!

for jogos in range(6): #*Para cada Jogo da Fase de Grupos
    jogo_copa = str(input()).split(" x ") #*Recebe os times que disputaram e seus respectivos gols

    selecao_casa, gols_casa = jogo_copa[0].split()[0], int(jogo_copa[0].split()[1]) #*Organiza em variáveis | Time e gols da casa
    selecao_visita, gols_visita = jogo_copa[1].split()[1], int(jogo_copa[1].split()[0]) #*Organiza em variáveis | Time e gols da visita

    resultado = (selecao_casa, gols_casa, selecao_visita, gols_visita) #*Armazena o resultado

    if resultado[1] > resultado[3]: #*Se a CASA ganhar
        selecoes_copa[resultado[0]]['pontos'] += 3 #*Ganha os pontos da vitória
        selecoes_copa[resultado[0]]['vitorias'] += 1 #*Recebe uma vitória
        selecoes_copa[resultado[0]]['saldo'] += gols_casa - gols_visita #*Contabiliza o saldo de gols

        selecoes_copa[resultado[2]]['pontos'] += 0 #*Ganha os pontos da derrota
        selecoes_copa[resultado[2]]['derrotas'] += 1 #*Recebe uma derrota
        selecoes_copa[resultado[2]]['saldo'] += gols_visita - gols_casa #*Contabiliza o saldo de gols


    elif resultado[1] < resultado[3]: #*Caso o visitante ganhar
        selecoes_copa[resultado[2]]['pontos'] += 3 #*Ganha os pontos da vitória
        selecoes_copa[resultado[2]]['vitorias'] += 1 #*Recebe uma vitória
        selecoes_copa[resultado[2]]['saldo'] += gols_visita - gols_casa #*Contabiliza o saldo de gols

        selecoes_copa[resultado[0]]['pontos'] += 0 #*Ganha os pontos da derrota
        selecoes_copa[resultado[0]]['derrotas'] += 1 #*Recebe uma derrota
        selecoes_copa[resultado[0]]['saldo'] += gols_casa  - gols_visita #*Contabiliza o saldo de gols

    else: #*Se empatarem
        selecoes_copa[resultado[0]]['pontos'] += 1 #*Ganha os pontos pelo empate
        selecoes_copa[resultado[0]]['empates'] += 1 #*Recebe um empate
        selecoes_copa[resultado[0]]['saldo'] += gols_casa  - gols_visita #*Contabiliza o saldo de gols

        selecoes_copa[resultado[2]]['pontos'] += 1 #*Ganha os pontos pelo empate
        selecoes_copa[resultado[2]]['empates'] += 1 #*Recebe um empate
        selecoes_copa[resultado[2]]['saldo'] += gols_visita - gols_casa #*Contabiliza o saldo de gols

    if resultado[0] == "Brasil" or resultado[2] == "Brasil": #*Caso o Brasil tenha jogado
        gols_jogadores = 0 #*Quantidade de gols feito pelos jogadores
        gols_marcados += (gols_visita if "Brasil" == selecao_visita else gols_casa) #*Pega quantos gols o Brasil fez na partida
        gols_sofridos += (gols_casa if "Brasil" == selecao_visita else gols_visita) #*Pega quantos gols o Brasil sofreu na partida

        while gols_jogadores != (gols_visita if "Brasil" == selecao_visita else gols_casa): #*Enquanto o número de gols do Brasil estiver diferente do número de gols dos jogadores
            jogador_gols_feitos = str(input()).rsplit() #*Recebe o jogador que fez o gol e os gols
            jogador, gols_feitos = jogador_gols_feitos[0], int(jogador_gols_feitos[1]) #*Organiza as informações
            jogadores_brasileiros.append((jogador, gols_feitos)) #*Adiciona a tupla do jogador e seus gols a uma lista
            gols_jogadores += gols_feitos #*Adiciona os gol do jogador nos gols totais dos jogadores
            gols_brasil[jogador] = 0 #*Adiciona o jogador no dicionário que verifica os jogadores que marcaram gols

podio_selecoes = ordenar(selecoes_copa) #*Recebe a ordem das seleções

print("------- Grupo C -------")
print(f"1º | {podio_selecoes['1'][1]} | {podio_selecoes['1'][0]['pontos']} | {podio_selecoes['1'][0]['vitorias']} | {podio_selecoes['1'][0]['derrotas']} | {podio_selecoes['1'][0]['empates']} | {podio_selecoes['1'][0]['saldo']}")
print(f"2º | {podio_selecoes['2'][1]} | {podio_selecoes['2'][0]['pontos']} | {podio_selecoes['2'][0]['vitorias']} | {podio_selecoes['2'][0]['derrotas']} | {podio_selecoes['2'][0]['empates']} | {podio_selecoes['2'][0]['saldo']}")
print(f"3º | {podio_selecoes['3'][1]} | {podio_selecoes['3'][0]['pontos']} | {podio_selecoes['3'][0]['vitorias']} | {podio_selecoes['3'][0]['derrotas']} | {podio_selecoes['3'][0]['empates']} | {podio_selecoes['3'][0]['saldo']}")
print(f"4º | {podio_selecoes['4'][1]} | {podio_selecoes['4'][0]['pontos']} | {podio_selecoes['4'][0]['vitorias']} | {podio_selecoes['4'][0]['derrotas']} | {podio_selecoes['4'][0]['empates']} | {podio_selecoes['4'][0]['saldo']}")

posicao_tabela = 0 #*Variável que representa a posição do Brasil na tabela

for posicao in podio_selecoes: #*Para cada posição no pódio
    if 'Brasil' in podio_selecoes[posicao]: #*Verifica a posição do Brasil no pódio
        posicao_tabela = int(posicao) #*Armazena a posição do Brasil na tabela

print("\n-- Desempenho Brasileiro --")
print(f"Posição: {posicao_tabela}")
print(f"Gols Marcados: {gols_marcados}")
print(f"Gols Sofridos: {gols_sofridos}")

utilizados = [] #*Lista que vai evitar repetições
for artilheiro_nome in jogadores_brasileiros: #*Pega cada jogador que fez gol | Possível artilheiro
    if artilheiro_nome[0] not in utilizados: #*Se não foi verificado ainda
        for artilheiros in jogadores_brasileiros: #*Pega cada possível artilheiro, novamente
            if artilheiro_nome[0] in artilheiros[0]: #*Para cada vez que o artilheiro aparecer na lista
                gols_brasil[artilheiro_nome[0]] += artilheiros[1] #*Soma os gols dele e armazena na lista de gols do Brasil

    utilizados.append(artilheiro_nome[0]) #*Diz que já foi verificado

for key in gols_brasil: #*Pega cada jogador que marcou e printa
    print(f"{key}: {gols_brasil[key]}")

melhor_da_partida = '' #*Guarda o nome do artilheiro
gols_do_melhor = -1 #*Guarda os gols feitos pelo melhor

for best in gols_brasil: #*Analisa quem foi o melhor
    if gols_brasil[best] > gols_do_melhor: #*Analisa quem fez mais gols e salva o nome e a qtd de gols
        melhor_da_partida = best
        gols_do_melhor = gols_brasil[best]

if gols_brasil != {}: #*Se houve gol do Brasil
    print(f"Artilheiro: {melhor_da_partida}")