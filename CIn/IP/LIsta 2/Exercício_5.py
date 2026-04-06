print("Radar de Fofocas de Copacabana iniciado!")

#Variáveis 
num_rodadas = int(input())
num_fofocas = 0
fofoca = all_fofocas = palavra_proibida = all_tentativa = tentativa = aux_o = aux_t = ''
ocorrencia = repeticao = 0

#Início das rodadas
for i in range(num_rodadas):
    #Restaurando variáveis
    fofoca = all_fofocas = palavra_proibida = ''
    num_fofocas = int(input())
    pontos = 15
    tentativa = all_tentativa = ''

    #Rodada atual
    print(f"Rodada {i+1}/{num_rodadas}")
    print(f"Fofocas registradas: {num_fofocas}")
    print('Pontuação inicial: 15')

    #Recebendo as fofocas
    for f in range(num_fofocas):
        fofoca = input()
        all_fofocas += (fofoca + " ")

    #Palavra proibida
    palavra_proibida = input()

    #Investigação
    while tentativa != "fim":
        tentativa = input()

        #Redefinindo variáveis
        ocorrencia = repeticao = 0

        #Acabou?
        if tentativa == 'fim':
            print(f"Rodada encerrada! Pontuação final: {pontos}")
        
        else:
            #Algoritmo para verificar repetição e ocorrencia
            for t in all_tentativa:
                if t.isalpha():
                    aux_t += t
                elif t == " ":
                    if aux_t == tentativa:
                        repeticao = 1
                    aux_t = ''

            for o in all_fofocas:
                if o.isalpha():
                    aux_o += o
                elif o == " ":
                    if aux_o == tentativa:
                        ocorrencia += 1
                    aux_o= ''

            #Prints da investigação
            if repeticao >= 1:
                print(f"Você já investigou '{tentativa}'. Tente outra.")

            elif tentativa == palavra_proibida:
                pontos -= 5
                print(f"Armadilha da Sueli! '{tentativa}' era proibida! -5 pontos")
                print(f"Pontuação atual: {pontos}")

            elif ocorrencia > 0:
                pontos += 2*ocorrencia
                print(f"Investigação bem sucedida! '{tentativa}' apareceu {ocorrencia} vez(es).")
                print(f"Pontuação atual: {pontos}")

            elif ocorrencia <= 0:
                pontos -= 1
                print(f"Nada encontrado sobre '{tentativa}'. -1 ponto")
                print(f"Pontuação atual: {pontos}")

            #Armazenando tentativas passadas
            all_tentativa += (tentativa + ' ')

            #Acabando os pontos
            if pontos <= 0:
                tentativa = 'fim'
                print("Você ficou sem pontos! Sueli venceu essa rodada")

#Tô mandando os côdigos duas vezes pra adicionar os comentários que eu esqueci