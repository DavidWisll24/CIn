#QUESTÃO EXTRA
print("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK\n")

#Variáveis
alpha = [letra for letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"]
num_linhas = int(input())
num_colunas = int(input())
matriz = []
sortudo = False
caractere = ''

##Pegando palavras de cada L linha com C caracteres
for _ in range(num_linhas):
    new_linha = str(input())[:num_colunas]#*Recebendo linhas num_linha vezes e limitando cada linha recebida a ter num_coluna caracteres
    matriz.append(list(new_linha))

nome = str(input())
print(f"USER {nome} LOGGED IN SUCCESSFULLY\n")
s_p_e_c_i_a_l = [int(atributo) for atributo in str(input()).split("-")]#*Lista representando cada atributo | [0] -> Strength, [1] -> Perception, [2] -> Endurance, [3] -> Charisma, [4] -> Intelligence, [5] -> Agility, [6] -> Luck
frase_secreta = str(input()).split()#*Lista de cada palavra que compoe a frase secreta
palavras_encontradas = []#*Variável para colocar as palavras encontradas na frase secreta

#Prints e Condições especiais a partir do Nome
if "Lucy" in nome:
    print("NORM: Minha irmãzona nunca mais foi a mesma depois que saiu do Vault... Será que ela ainda lembra como mexer em computadores ou a radiação derreteu o cérebro dela de vez?\n")
if "Maximus" in nome:
    print("NORM: Ah, então é o Maximus... Só porque chega com uma armadura brilhando ele acha que pode ficar com minha irmã? Vamos ver se por dentro dessa lata existe cérebro.\n")
    s_p_e_c_i_a_l[4] = s_p_e_c_i_a_l[4] - 2
if "Ghoul" in nome or "Necrótico" in nome or "Cooper" in nome:
    print("NORM: Cooper Howard, o astro de cinema, virou isso aí? A Wasteland não perdoa ninguém... nem celebridade.\n")
if "Norm" in nome:
    print("NORM: Teste? Pra mim? Por favor. Eu já sou a mente mais brilhante do Vault 33.\n")
else: #*Se o nome não possuir Norm dentro dele, o codigo continua

    #Prints e Condições especiais a partir dos Atributos
    ##Validação dos Atributos
    intervalo_erro = False
    while not intervalo_erro:
        num_atributo_ok = 0 
        for intervalo in s_p_e_c_i_a_l: #*percorre cada valor na lista s.p.e.c.i.a.l
            if intervalo < 1 or intervalo > 10: #*Se não estiver no intervalo
                s_p_e_c_i_a_l = [int(atributo) for atributo in str(input()).split("-")] #*Pedindo novamente os valores
            else: #Se estiver no intervalo
                num_atributo_ok += 1 #*Pra cada atributo no intervalo, soma 1

        if num_atributo_ok == 7: #*Se o números de atributos ok for igual ao número de atributos(7), tá tudo certo
            intervalo_erro = True
    
    ##Mensagens de atributos extremos
    if s_p_e_c_i_a_l[0] == 10: #*Força(Strength) Máxima
        print("NORM: Meu Deus, você quebrou o terminal na base da porrada?! Se derrotar um Deathclaw no soco for hobby, melhor eu te dar uma Nuka-Cola gelada agora mesmo...\n")
    elif s_p_e_c_i_a_l[1] == 10: #*Percepção(Perception) Máxima
        print("NORM: Peraí... você tá arrombando a máquina de Nuka-Colas com uma chave de fenda e uma presilha? NÃO! ASSIM NÃO VALE!")
    elif s_p_e_c_i_a_l[3] == 10: #*Carisma(Charisma) Máximo
        print("NORM: Uau, esse nível de carisma é trapaça social. Você nem precisava desse teste, né? Toma uma Nuka-Cola Quantum, estrela do Vault.")
    elif s_p_e_c_i_a_l[4] == 10: #*Inteligência(Intelligence) Máxima
        print("NORM: Alguém tão inteligente quanto eu? Finalmente uma conversa à altura. O teste não faz jus à sua cabeça, então pega uma Nuka-Cola Quantum e vamos planejar como usar o G.E.C.K. na superfície.")
    else:
        if s_p_e_c_i_a_l[6] == 10: #*Sorte(Luck) Máxima
            print("NORM: Com essa sorte absurda, eu só vou fingir surpresa quando a máquina se abrir sozinha pra você.\n")
            sortudo = True #*Variável que vai definir o fim do programa no primeiro acerto
        
        #Tentando o Hacking
        maxnum_tentativas = (len(frase_secreta)) * (s_p_e_c_i_a_l[4] // 2)
        qtd_tentativas = 0
        achou_todas = False
        sortudo_win = False

        print(f"Palavras encontradas: {', '.join(palavras_encontradas)}\nTentativas: {qtd_tentativas}/{maxnum_tentativas}.\n")
        for print_linha in matriz: #*Entra na linha
            print_matriz = '' #*Usada para printar cada linha da matriz
            for print_element in print_linha: #*entra em cada elemento
                if print_matriz == '':
                    print_matriz += print_element
                else:
                    print_matriz += 'ㅤ' + print_element
            print(print_matriz)
        print()
        print()
    
        while not achou_todas and maxnum_tentativas != qtd_tentativas:
            palavra_rodada = '' #*Recebe a palavra encontrada na rodada

            ##Condição Sortudo
            if len(palavras_encontradas) > 0 and sortudo:
                print("NORM: Ah, sortudo(a) miserável!! Não acredito que você acertou de primeira... Toma uma Nuka-Cola Quantum antes que eu mude de ideia!")
                achou_todas = True
            
            else:  #*Caso não seja sortudo ou não tenha acertado ainda 
                    
                tentativa = str(input()) #*Pedindo tentativa da vez
                qtd_tentativas += 1
                print(f"Nova tentativa: Coordenada {tentativa}\n")

                ##Validando coordenadas da tentativa
                coordenadas = [int(coord) for coord in tentativa.split('-')]
                
                if coordenadas[0] < num_linhas and coordenadas[1] < num_colunas:
                    ###Pegando o caractere válido
                    caractere = matriz[coordenadas[0]][coordenadas[1]]

                    ###Procurando na matriz qual a palavra encontrada
                    if (matriz[coordenadas[0]][coordenadas[1] -1] in alpha or matriz[coordenadas[0]][coordenadas[1] + 1] in alpha) if (coordenadas[1] < num_colunas - 1) else (matriz[coordenadas[0]][coordenadas[1] -1] in alpha): #*Se tiver mais alguma letra naquela linha, então a palavra é horizontal | Operador ternario para ganrantir que o index não estoure
                        prox_coluna = -1
                        primeira_letra_encontrada_linha = False
                        while prox_coluna != (num_colunas -1):
                            prox_coluna += 1
                            if matriz[coordenadas[0]][prox_coluna] in alpha:
                                palavra_rodada += matriz[coordenadas[0]][prox_coluna]#*Descobre a palavra na horizontal pegando cada letra presente na linha
                                matriz[coordenadas[0]][prox_coluna] = '*'
                                primeira_letra_encontrada = True
                            elif primeira_letra_encontrada_linha and matriz[coordenadas[0]][prox_coluna] not in alpha:
                                prox_coluna = (num_colunas - 1)
                    
                        palavras_encontradas.append(palavra_rodada)

                    elif (matriz[coordenadas[0] - 1][coordenadas[1]] in alpha or matriz[coordenadas[0] + 1][coordenadas[1]] in alpha) if (coordenadas[0] < num_linhas - 1) else (matriz[coordenadas[0] - 1][coordenadas[1]] in alpha): #*Se tiver mais alguma letra naquela coluna, então a palavra é vertical | Operador ternario para ganrantir que o index não estoure
                        prox_linha = -1
                        primeira_letra_encontrada_coluna = False
                        while prox_linha != (num_linhas -1):
                            prox_linha += 1
                            if matriz[prox_linha][coordenadas[1]] in alpha:
                                palavra_rodada += matriz[prox_linha][coordenadas[1]]#*Descobre a palavra na vertical pegando cada letra presente na coluna
                                matriz[prox_linha][coordenadas[1]] = '*'
                                primeira_letra_encontrada_coluna = True
                            elif primeira_letra_encontrada_coluna and (matriz[prox_linha][coordenadas[1]] not in alpha):
                                prox_linha = (num_linhas - 1)
                            
                        palavras_encontradas.append(palavra_rodada)
                    
                    else: #*Se a palavra for apenas uma Letra
                        if caractere in alpha:
                            palavra_rodada = caractere
                            matriz[coordenadas[0]][coordenadas[1]] = '*'
                            palavras_encontradas.append(palavra_rodada)

                ###Verificando palavra descoberta
                if caractere == '*': #*Caso já tenha sido encontrada
                    print("NORM: Essa palavra você já encontrou, gênio. Mira em outra coordenada.\n")
                elif coordenadas[0] >= num_linhas or coordenadas[1] >= num_colunas or (caractere not in alpha): #*Caso não seja válida
                    print("NORM: Coordenada inválida. O terminal é avançado demais ou você só digitou no susto?\n")
                else: #*Caso seja palavra nova
                    print(f"NORM: Boa! A coordenada {tentativa} pegou o caractere {caractere} da palavra {palavra_rodada}.\n")

                ##Printando Matriz alterada
                print(f"Palavras encontradas: {', '.join(palavras_encontradas)}\nTentativas: {qtd_tentativas}/{maxnum_tentativas}.\n")
                for print_linha in matriz: #*Entra na linha
                    print_matriz = '' #*Usada para printar cada linha da matriz
                    for print_element in print_linha: #*entra em cada elemento
                        if print_matriz == '':
                            print_matriz += print_element
                        else:
                            print_matriz += 'ㅤ' + print_element
                    print(print_matriz)
                print()
                print()

                
                ##Condições de Vitória e Derrota normal
                if len(palavras_encontradas) == len(frase_secreta):
                    print(f"NORM: Parabéns, {nome}! Você encontrou todas as palavras secretas. Considerando tudo, foi até elegante. Sua Nuka-Cola geladinha está garantida!")
                    achou_todas = True
                elif qtd_tentativas == maxnum_tentativas:
                    print("NORM: Meu desafio continua supremo! Em breve eu supero até os sistemas de segurança de Robert House... e você ainda vai pedir revanche.")