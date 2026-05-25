#BRAZIL X MARROCOS: O PRIMEIRO PASSOPRO HEXAF🏆!

#FUNÇÃO
def melhor_partida(candidatos, j_bra, j_marr): #*Função para decidir o melhor da partida
    maior_pontuacao = -999 #*Define a variável e recebe um valor que garante a primeira troca
    nome_melhor = '' #*Define a variável

    for jogador in candidatos: #*testa cada jogador
        gols = ass = ca = cv = 0 #*Usada para receber os válores correspondentes 
        if 'gols' in candidatos[jogador]: #*Se fez gol
            gols = candidatos[jogador]['gols']

        if  'ass' in candidatos[jogador]: #*Se fez assistencia
            ass = candidatos[jogador]['ass']

        if 'amarelo' in candidatos[jogador]: #*Se tomou c amarelo
            ca = candidatos[jogador]['amarelo']

        if 'vermelho' in candidatos[jogador]: #*Se tomou c vermelho
            cv = candidatos[jogador]['vermelho']

        if ca < 2: #*Condição dos dois amarelos
            pontos = (gols * 8) + (ass * 5) - (ca * 2) - (cv * 5) #*Calculando pontos
        else:
            pontos = (gols * 8) + (ass * 5) - (cv * 5)

        if pontos > maior_pontuacao: #*Vê o melhor pelos pontos
            maior_pontuacao = pontos
            nome_melhor = jogador
        elif pontos == maior_pontuacao: #*Se empatar
            if jogador < nome_melhor: #*Vê o melhor pelo nome
                maior_pontuacao = pontos
                nome_melhor = jogador

    ###Verifica a seleção
    if nome_melhor in j_bra: 
        selecao = "Brasil"
    elif nome_melhor in j_marr:
        selecao = "Marrocos"

    return (nome_melhor, selecao)


#Definições iniciais
convocacao_brasil = { #*Jogadores válidos do Brasil
    'Alisson': {},
    'Ederson': {},
    'Bento': {},
    'Alex Sandro': {},
    'Danilo': {},
    'Douglas Santos': {},
    'Wesley': {},
    'Marquinhos': {},
    'Gabriel Magalhães': {},
    'Bremer': {},
    'Léo Pereira': {},
    'Andrey Santos': {},
    'Bruno Guimarães': {},
    'Casemiro': {},
    'Danilo Santos': {},
    'Fabinho': {},
    'Joelinton': {},
    'Endrick': {},
    'Igor Thiago': {},
    'Gabriel Martinelli': {},
    'João Pedro': {},
    'Neymar': {},
    'Luiz Henrique': {},
    'Matheus Cunha': {},
    'Raphinha': {},
    'Vinícius Júnior': {}
}
#*Jogadores convocados no Brasil
jogadores_brasileiros = ('Alisson', 'Ederson', 'Bento', 'Alex Sandro', 'Danilo', 'Douglas Santos', 'Wesley', 'Marquinhos', 'Gabriel Magalhães', 'Bremer', 'Léo Pereira', 'Andrey Santos', 'Bruno Guimarães', 'Casemiro', 'Danilo Santos', 'Fabinho', 'Joelinton', 'Endrick', 'Igor Thiago', 'Gabriel Martinelli', 'João Pedro', 'Neymar', 'Luiz Henrique', 'Matheus Cunha','Raphinha', 'Vinícius Júnior')

convocacao_marrocos = { #*Jogadores válidos do Marrocos
    'Bounou': {},
    'Munir Mohamedi': {},
    'El Mehdi Benabid': {},
    'Hakimi': {},
    'Mazraoui': {},
    'Aguerd': {},
    'Chadi Riad': {},
    'Yahya Attiat-Allah': {},
    'Abdelkabir Abqar': {},
    'Achraf Dari': {},
    'Ayoub El Amloud': {},
    'Amrabat': {},
    'Ounahi': {},
    'Brahim Díaz': {},
    'Bilal El Khannouss': {},
    'Ismael Saibari': {},
    'Amir Richardson': {},
    'Oussama El Azzouzi': {},
    'Amine Harit': {},
    'Ziyech': {},
    'Amine Adli': {},
    'En-Nesyri': {},
    'Ezzalzouli': {},
    'Soufiane Rahimi': {},
    'Ilias Akhomach': {},
    'Ayoub El Kaabi': {}
}
#*Jogadores convocados no Marrocos
jogadores_marroquinos = ('Bounou', 'Munir Mohamedi', 'El Mehdi Benabid', 'Hakimi', 'Mazraoui', 'Aguerd', 'Chadi Riad', 'Yahya Attiat-Allah', 'Abdelkabir Abqar', 'Achraf Dari', 'Ayoub El Amloud', 'Amrabat', 'Ounahi', 'Brahim Díaz', 'Bilal El Khannouss', 'Ismael Saibari', 'Amir Richardson', 'Oussama El Azzouzi', 'Amine Harit', 'Ziyech', 'Amine Adli', 'En-Nesyri', 'Ezzalzouli', 'Soufiane Rahimi', 'Ilias Akhomach', 'Ayoub El Kaabi')

#INICIO
##Diz quem já realizou essa ação
jogadores_gols = list() 
jogadores_assistencia = list()
jogadores_cart_a = list()

##Jogadores inutilizaveis em jogo
expulsos = dict()
substituidos = dict()

##Quantidade de substituições
sub_marrocos = 0
sub_brasil = 0

##Guarda cada comentário da partida
comentario = list()

##Guarda quantos gols cada pais fez
gols_brasil = gols_marrocos = 0

#FASE 1

##MARROCOS
esquema_marrocos = "4-3-3"
campo_marrocos = ["Bounou", "Hakimi", "Mazraoui", "Aguerd", "Chadi Riad", "Amrabat", "Ounahi", "Brahim Díaz", "Ziyech", "Amine Adli", "En-Nesyri"]
for jogador_campo_mar in campo_marrocos: #*Define jogadores que entraram em campo
            convocacao_marrocos[jogador_campo_mar]['entrou'] = True 
        
##BRASIL
esquema = str(input()).split('-') #*Recebe o esquema

if len(esquema) != 3: #*Se a formação não estiver no formato a-b-c
    print("Esquema inválido!") #*Dá errado

elif int(esquema[0]) < 1 or int(esquema[1]) < 1 or int(esquema[2]) < 1: #*Se forem números inválidos
    print("Esquema inválido!") #*Dá errado

elif (int(esquema[0]) + int(esquema[1]) + int(esquema[2])) != 10: #*Se a soma de jogadores não der 10
    print("Esquema inválido!") #*Dá errado

else: #*Se estiver nos conformes
    esquema[0], esquema[1], esquema[2] = int(esquema[0]), int(esquema[1]), int(esquema[2])
    em_campo = list() #*Lista que armazena jogadores em campo do Brasil

    goleiro = str(input()) #*Recebe o goleiro
    em_campo.append(goleiro) #*Adiciona ele na lista

    defesa = ''
    for defe in range(esquema[0]): #*Para cada jogador na defesa, adiciona no campo
        defensor = str(input())
        em_campo.append(defensor)
        defesa += ' ' + defensor + ','
    
    meio_campo = ''
    for meio in range(esquema[1]): #*Para cada jogador no meio campo, adiciona no campo
        m_campista = str(input())
        em_campo.append(m_campista)
        meio_campo += ' ' + m_campista + ','

    atacantes = ''
    for ataque in range(esquema[2]): #*Para cada jogador no ataque, adiciona no campo
        atacante = str(input())
        em_campo.append(atacante)
        atacantes += ' ' + atacante + ','

    validade_convocacao = True #*Usada para validar a escalação
    
    for jogador in em_campo: #*Verifica cada jogador
        if jogador not in convocacao_brasil: #*Se não foi convocado
            validade_convocacao = False #*Escalação inválida

    if not validade_convocacao: #*Se não for válida a convocação
        print("Elenco inválido. Simulação Cancelada!")
    
    else: #*Se for
        for jogador_campo in em_campo: #*Os titulares entram em campo
            convocacao_brasil[jogador_campo]['entrou'] = True 
        
        print(f"O Brasil vem a campo com o goleiro {goleiro}.")
        print(f"A defesa é composta por{defesa[:-1]}.")
        print(f"O meio de campo vem com{meio_campo[:-1]}.")
        print(f"E no ataque temos{atacantes[:-1]}.")

        #FASE 2
        continuar = True #*Define a continuidade do jogo
        tempo_antigo = 0 #*Onde será armazenado o tempo anterior marcado na ação
        primeiro_input = False #*Diz se os prints finais ocorrerão

        ##PARTIDA
        while continuar:
            tempo_atual = str(input()) #*Recebe o tempo atual de jogo
            
            if not tempo_atual.isnumeric(): #*Se não for numerico, pula pro final
                continuar = False
                if not primeiro_input: #*Se esse foi o primeiro input, acaba aqui
                    print("Entrada inválida. O jogo não foi iniciado!")
            
            elif int(tempo_atual) > 90 or int(tempo_atual) < 1: #*Se for um tempo fora do limite permitido
                continuar = False
                if not primeiro_input: #*Se esse foi o primeiro input, acaba aqui
                    print("Entrada inválida. O jogo não foi iniciado!")
            
            elif int(tempo_atual) < tempo_antigo: #*Se tentarem romper a barreira do espaço tempo
                continuar = False
                if not primeiro_input: #*Se esse foi o primeiro input, acaba aqui
                    print("Entrada inválida. O jogo não foi iniciado!")
            
            else: #*Se for válido
                ###AÇÕES
                acoes_validas = ['gol', 'cartão amarelo', 'cartão vermelho', 'substituição'] #*Diz quais ações podem ser tomadas
                primeiro_input = True #*Se entrou aqui, o primeiro input é válido
                acao = str(input()) #*Recebe a ação

                if acao.lower() not in acoes_validas: #*Verifica válidade
                    continuar = False
                    primeiro_input = False
                    print("Ação inválida! Simulação Cancelada")
                
                else: #*Se válida
                    jogador_acao = str(input()) #*Recebe quem realizou/sofreu
                    tempo_antigo = int(tempo_atual) #*Tempo que ocorreu

                    ###Válidação
                    validade_acao = False #*Usada para validar a ação
                    campo_inteiro = (em_campo + campo_marrocos) #*Pega o campo inteiro
                
                    if jogador_acao in campo_inteiro: #*Se está no campo
                        validade_acao = True #*Ação válida
                
                    if not validade_acao: #*Se o jogador não for válido
                        if jogador_acao in jogadores_brasileiros or jogador_acao in jogadores_marroquinos: #*Está no time?
                            print(f"{jogador_acao} não está em campo! Simulação Cancelada")
                        else: #*Se não estiver
                            print("Jogador inválido. Simulação Cancelada")
                        
                        continuar = False #*Para o código
                        primeiro_input = False #*Sem direito a prints finais

                    else: #*Se for um jogador válido
                        ##GOL
                        if acao.lower() =="gol":
                            if jogador_acao in convocacao_brasil: #*Vê se é brasileiro
                                gols_brasil += 1 #*Brasil marca um gol

                                ##Jogador recebe um gol na conta
                                if jogador_acao not in jogadores_gols:    
                                    convocacao_brasil[jogador_acao]['gols'] = 1
                                    jogadores_gols.append(jogador_acao)

                                else:
                                    convocacao_brasil[jogador_acao]['gols'] += 1
                            
                            elif jogador_acao in convocacao_marrocos: #*Vê se é marroquino
                                gols_marrocos += 1 #*Marrocos faz um gol

                                ##Jogador recebe um gol na conta
                                if jogador_acao not in jogadores_gols:
                                    convocacao_marrocos[jogador_acao]['gols'] = 1
                                else:
                                    convocacao_marrocos[jogador_acao]['gols'] += 1
                            
                            assistencia = str(input()) #*Houve assistência?

                            if assistencia.lower() == "sim":
                                jogador_ass = str(input()) #*Pede quem fez

                                if jogador_ass in convocacao_brasil: #*Se for brasileiro
                                    #*Adiciona uma assistencia para a conta
                                    if jogador_ass not in jogadores_assistencia:
                                        convocacao_brasil[jogador_ass]['ass'] = 1
                                        jogadores_assistencia.append(jogador_ass)
                                    else:
                                        convocacao_brasil[jogador_ass]['ass'] += 1
                                    
                                elif jogador_ass in convocacao_marrocos: #*Se for do Marrocos
                                    #*Adiciona uma assistencia para a conta
                                    if jogador_ass not in jogadores_assistencia:
                                        convocacao_marrocos[jogador_ass]['ass'] = 1
                                        jogadores_assistencia.append(jogador_ass)
                                    else:
                                        convocacao_marrocos[jogador_ass]['ass'] += 1
                                
                                comentario.append(('gca', tempo_atual,  jogador_acao, jogador_ass)) #*Guarda o comentário do gol
                                
                            elif assistencia.lower() == 'não':
                                comentario.append(('gs', tempo_atual,  jogador_acao)) #*Guarda o comentário do gol

                            else: #*se for inválido, acaba tudo
                                continuar = False
                                primeiro_input = False
                                print("Entrada inválida!")

                        ##Cartão Amarelo
                        elif acao.lower() == "cartão amarelo": 
                            if jogador_acao in convocacao_brasil: #*Se for brasileiro
                                if jogador_acao not in jogadores_cart_a: #*Se for a primeira vez, recebe um cartão
                                    convocacao_brasil[jogador_acao]['amarelo'] = 1 #*Adiciona um vermelho
                                    jogadores_cart_a.append(jogador_acao)

                                else: #*Se for a segunda, é EXPULSO com vermelho
                                    convocacao_brasil[jogador_acao]['amarelo'] += 1 #*Adiciona um amarelo
                                    convocacao_brasil[jogador_acao]['vermelho'] = 1 #*Adiciona um vermelho
                                    expulsos[jogador_acao] = convocacao_brasil[jogador_acao] #*Adiciona aos expulsos
                                    convocacao_brasil.pop(jogador_acao) #*Tira do time
                                    em_campo.remove(jogador_acao) #*Tira do time


                            if jogador_acao in convocacao_marrocos: #*Se for do Marrocos
                                if jogador_acao not in jogadores_cart_a: #*Se for a primeira vez, recebe um cartão
                                    convocacao_marrocos[jogador_acao]['amarelo'] = 1
                                    jogadores_cart_a.append(jogador_acao)

                                else: #*Se for a segunda, é EXPULSO com vermelho
                                    convocacao_marrocos[jogador_acao]['amarelo'] += 1
                                    convocacao_marrocos[jogador_acao]['vermelho'] = 1
                                    expulsos[jogador_acao] = convocacao_marrocos[jogador_acao]
                                    convocacao_marrocos.pop(jogador_acao)
                                    campo_marrocos.remove(jogador_acao)

                            comentario.append(('ca', tempo_atual,  jogador_acao)) #*Guarda o comentário do cartão amarelo
                            
                            if jogador_acao in expulsos: #*Se for expulso
                                comentario.append(('cv', tempo_atual,  jogador_acao)) #*Guarda o comentário do cartão vermelho

                        ##Cartão Vermelho
                        elif acao.lower() == "cartão vermelho":
                            if jogador_acao in convocacao_brasil: #*Se for brasileiro
                                convocacao_brasil[jogador_acao]['vermelho'] = 1 #*Adiciona um vermelho
                                expulsos[jogador_acao] = convocacao_brasil[jogador_acao] #*Adiciona aos expulsos
                                convocacao_brasil.pop(jogador_acao) #*Tira do time 
                                em_campo.remove(jogador_acao) #*Tira do campo

                            if jogador_acao in convocacao_marrocos: #*Se for do Marrocos
                                convocacao_marrocos[jogador_acao]['vermelho'] = 1
                                expulsos[jogador_acao] = convocacao_marrocos[jogador_acao]
                                convocacao_marrocos.pop(jogador_acao)
                                campo_marrocos.remove(jogador_acao)

                            comentario.append(('cv', tempo_atual,  jogador_acao)) #*Guarda o comentário do cartão vermelho

                        ##Substituição  
                        elif acao.lower() == "substituição":
                            jogador_novo = str(input()) #*Jogador que vai entrar
                            
                            if jogador_acao in em_campo: #*Se o jogador estiver no campo pelo Brasil
                                em_campo.remove(jogador_acao) #*Sai de campo
                                substituidos[jogador_acao] = convocacao_brasil[jogador_acao] #*Entra na lista de substituidos
                                convocacao_brasil.pop(jogador_acao) #*Fica inútil
                            
                            elif jogador_acao in campo_marrocos: #*Se o jogador estiver no campo pelo Marrocos
                                campo_marrocos.remove(jogador_acao)
                                substituidos[jogador_acao] = convocacao_marrocos[jogador_acao]
                                convocacao_marrocos.pop(jogador_acao)

                            if jogador_novo in convocacao_marrocos and sub_marrocos < 5: #*Se for válida a substituição
                                #Entra no campo
                                campo_marrocos.append(jogador_novo)
                                convocacao_marrocos[jogador_novo]['entrou'] = True

                                sub_marrocos += 1 #*Adiciona uma substituição para o Marrocos

                            elif jogador_novo in convocacao_brasil and sub_brasil < 5: #*Se for válida a substituição
                                #*Entra no campo
                                em_campo.append(jogador_novo)
                                convocacao_brasil[jogador_novo]['entrou'] = True

                                sub_brasil += 1 #*Adiciona uma substituição para o Brasil

                            else: #*Se a substituição for inválida
                                ##Para tudo
                                continuar = False
                                primeiro_input = False
                                print("A substituição não pôde ser concluída! Simulação Cancelada")
                            
                            comentario.append(('sub', tempo_atual, jogador_novo,jogador_acao))

        #FASE 3
        if primeiro_input: #*Se der tudo certo para o final
            print(f"\nFim de jogo! Brasil {gols_brasil}x{gols_marrocos} Marrocos.")

            for evento in comentario: #*Para cada evento que ocorreu no jogo
                if evento[0] == 'gca': #*Se for gol com assistência
                    print(f"{evento[1]}'⚽ {evento[2]}; 🅰️ {evento[3]}")
                
                elif evento[0] == 'gs': #*Se for gol sem assistência
                    print(f"{evento[1]}'⚽ {evento[2]}")
                
                elif evento[0] == 'ca': #*Se for cartão amarelo
                    print(f"{evento[1]}'🟨 {evento[2]}")

                elif evento[0] == 'cv': #*Se for cartão vermelho
                    print(f"{evento[1]}'🟥 {evento[2]}")

                elif evento[0] == 'sub': #*Se for substituição
                    print(f"{evento[1]}'⬆️ {evento[2]} ⬇️ {evento[3]}")
                
            ##PEGANDO OS CANDIDATOS
            candidatos = {} #*Recebe cada candidato válido
            ###Brasil
            for i in convocacao_brasil:
                if convocacao_brasil[i] != {}: #*Se o jogador fez algo na partida
                    candidatos[i] = convocacao_brasil[i] #*É candidato

            ###Marrocos
            for j in convocacao_marrocos:
                if convocacao_marrocos[j] != {}:
                    candidatos[j] = convocacao_marrocos[j]

            ###Pega os expulsos
            for k in expulsos:
                candidatos[k] = expulsos[k]

            ###Pega os substituidos
            for l in substituidos:
                candidatos[l] = substituidos[l]

            ##PEGA O MELHOR DA PARTIDA
            melhor, selecao = melhor_partida(candidatos, jogadores_brasileiros, jogadores_marroquinos)

            print(f"🏆 O melhor em campo foi {melhor}, do {selecao}.\n")

            #PRINTS ESPECIAIS
            if (gols_brasil - gols_marrocos) >= 3:
                print("QUE GOLEADA! O INÍCIO DO SONHO DO HEXA!!!")
            
            elif (gols_brasil - gols_marrocos) > 0:
                print("Boa vitória! Essa Copa é nossa, Brasil!")
            
            elif (gols_marrocos - gols_brasil) >= 3:
                print("Era melhor nem ter vindo pra essa Copa…")

            elif (gols_marrocos - gols_brasil) > 0:
                print("Foco, Brasil! Vamos nos recuperar dessa!")
            
            elif gols_brasil == 0 and gols_marrocos == 0:
                print("Zzzzzzzzzzzzz…")
            
            else:
                print("Jogo difícil, mas podia ser melhor!")
        