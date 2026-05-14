#A CORRIDA DE KARTS

#Funções Recursivas
def corrida(velocidade_inicial, glitchs, info_pistas, pista_atual):
    #Condições de parada
    if glitchs < 0: #*Se acabarem os glitchs
        venceu_corrida = False
        return venceu_corrida, -1
    if pista_atual == len(info_pistas): #*Verifica se acabou a corrida
        venceu_corrida = True
        return venceu_corrida, 0.0
    
    tipo_pista, tamanho_pista, p1_pista, p2_pista = info_pistas[pista_atual][0], info_pistas[pista_atual][1], info_pistas[pista_atual][2], info_pistas[pista_atual][3] #*Atribui cada característica a uma variável correspondente
    acoes = [10.0, 0.0, -10.0] #*Ações possíveis que devem ser realizadas em cada pista_atual nova | [0] -> Acelerar; [1] -> Manter; [1] -> Frear
    acao = 0 #*Variável da ação utilizada na vez
    venceu_corrida = False
    venceu_uma = False
    min_tempo_gasto = -1

    for acao in range(len(acoes)): #*Vê cada possibilidade futura 
        tempo_gasto = 0
        uso_glitch = False #*Diz se usei o glitch nessa pista
        velocidade_entrada = velocidade_inicial + acoes[acao]
        novo_glitch = glitchs

        if velocidade_entrada <= 0: #*Se o motor morrer
            novo_glitch = glitchs - 1 #*Usa glitch
            velocidade_saida = 10 #*Reinicia a velocidade
            uso_glitch = True

        elif tipo_pista == "Reta": #*Se a pista for Reta
            velocidade_saida = velocidade_entrada #*Mantem velocidade constante
        
        elif tipo_pista == "Curva": #*Se for Curva
            if velocidade_entrada > p1_pista: #**Verifica se houve algum acidente
                novo_glitch = glitchs - 1 #*Usa glitch
                velocidade_entrada = 10 #*Reinicia a velocidade
                uso_glitch = True

            velocidade_saida = velocidade_entrada                
        
        elif tipo_pista == "Subida": #*Se a pista for uma Subida
            velocidade_saida = velocidade_entrada - p1_pista #*Reduz da velocidade a perda
            if velocidade_saida <= 0: #*Se saiu rolando igual uma bola de gude
                novo_glitch = glitchs - 1 #*Usa glitch
                velocidade_saida = 10 #*Reinicia a velocidade
                uso_glitch = True

        elif tipo_pista == "Descida": #*Se a pista for uma decida
            velocidade_saida = velocidade_entrada + p1_pista #*Adiciona o empurrão da gravidade
            if velocidade_saida > p2_pista: #*Se perder o controle
                novo_glitch = glitchs - 1 #*Usa glitch
                velocidade_saida = 10 #*Reinicia a velocidade
                uso_glitch = True

        if uso_glitch: #*Caso tenha usado um glitch
            tempo_gasto += 0 #*Acaba a pista com tempo 0

        else: #*Senão
            tempo_gasto += tamanho_pista/velocidade_entrada #*Analisa o tempo para terminar aquele percurso

        venceu_corrida, prox_tempo_gasto = corrida(velocidade_saida, novo_glitch, info_pistas, pista_atual + 1)
        
        if venceu_corrida:
            venceu_uma = True
            tempo_total = tempo_gasto + prox_tempo_gasto
            if min_tempo_gasto > tempo_total or min_tempo_gasto < 0:
                min_tempo_gasto = tempo_total
        
    
    return venceu_uma, min_tempo_gasto

#INICIO
print("Calibrando a gravidade e o atrito da pista...\n")
condicoes_base = [int(condicao) for condicao in str(input()).split()] #*Cria uma lista com quantas pistas teram [0], a velocidade inicial da Vanellope [1] e a quantidade de glitch [2]
informacoes_pista = [] #*Lista que vai guardar as informações de cada pista_atual

for pistas in range(condicoes_base[0]):
    caracteristicas_pista = str(input()).split()
    informacoes_pista.append([caracteristicas_pista[0]] + [float(valor) for valor in caracteristicas_pista[1:]]) #*Informações da pista_atual | [0] -> Tipo; [1] -> Tamanho; [2] e [3] são os parametros P1 e P2

resultado_corrida, tempo_termino = corrida(condicoes_base[1], condicoes_base[2], informacoes_pista, 0)

if resultado_corrida:
    print(f"A corrida foi um sucesso! Tempo minimo cravado: {tempo_termino:.2f}s.")
else:
    print("Bug fatal! Vanellope capotou e o kart virou pixels.")