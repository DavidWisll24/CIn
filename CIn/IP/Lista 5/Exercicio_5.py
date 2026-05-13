#A CORRIDA DE KARTS

#Funções Recursivas
def corrida(velocidade_atual, qtd_glitch, qtd_pistas):
    if velocidade_atual <= 0 and qtd_glitch <= 0:
        return False
    elif qtd_pistas <= 0:
        return True
    else:
        configuracao_pista = [caracteristica for caracteristica in (input()).split()] #*Recebe as caracteristicas daquela pista | [0] -> Tipo; [1] -> Tamanho; [2] -> Parametro 1; [3] -> Parametro 2
        for converte in range(len(configuracao_pista) - 1): #*Converte os parametro e o tamanho para float
            configuracao_pista[converte + 1] = float(configuracao_pista[converte + 1])

        if velocidade_atual <= 0: #*Caso ela já comece com 0 de velocidade
            qtd_glitch -= 1
            qtd_pistas -= 1
            velocidade_saida = 10.0
        elif configuracao_pista[0] == "Reta":
            pass
            
def backtrack(velocidade_atual, tipo, tamanho, param1, param2):
    tempos = []
    if tipo == "Reta":
        for acao in acoes:
            tempo_total = (velocidade_atual + acao) / tamanho
            tempos.append(tempo_total)
        tempo_min = min(tempo_total)
        return tempo_min
    


#INICIO
condicoes_base = [int(condicao) for condicao in str(input()).split()] #*Cria uma lista com quantas pistas teram [0], a velocidade inicial da Vanellope [1] e a quantidade de glitch [2]
acoes = [10.0, 0, -10.0] #*Ações possíveis que devem ser realizadas em cada pista nova | [0] -> Acelerar; [1] -> Manter; [1] -> Frear