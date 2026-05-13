#A CORRIDA DE KARTS

#Funções Recursivas
def corrida(velocidade_inicial, glitchs, info_pistas, pista_atual, venceu_corrida):
    #Condições de parada
    if venceu_corrida:
        return True
    if glitchs[0] < 0: #*Se acabarem os glitchs
        venceu_corrida = False
        return venceu_corrida
    if pista_atual > 0: #*Só verifica depois da primeira pista
        if velocidade_inicial <= 0: #*Se o motor morrer ou o carro descer a ladeira
            glitchs[0] = glitchs[0] - 1
            return 0
        if velocidade_inicial > info_pistas[pista_atual - 1][3] and info_pistas[pista_atual - 1][0] == "Descida": #*Se a velocidade ultrapassou o limite da descida
            glitchs[0] = glitchs[0] - 1
            return 0
        if velocidade_inicial > info_pistas[pista_atual - 1][2] and info_pistas[pista_atual - 1][0] == "Curva": #*Se a velocidade ultrapassou o limite de atrito
            glitchs[0] = glitchs[0] - 1
            return 0
    if pista_atual == len(info_pistas): #*Verifica se acabou a corrida
        venceu_corrida = True
        return venceu_corrida
    
    acoes = [10.0, 0.0, -10.0] #*Ações possíveis que devem ser realizadas em cada pista_atual nova | [0] -> Acelerar; [1] -> Manter; [1] -> Frear
    for acao in range(len(acoes)): #*Vê cada possibilidade futura   
        velocidade_entrada = velocidade_inicial + acoes[acao]

        if info_pistas[pista_atual][0] == "Reta" or info_pistas[pista_atual][0] == "Curva":
            velocidade_saida = velocidade_entrada
        elif info_pistas[pista_atual][0] == "Subida":
            velocidade_saida = velocidade_entrada - info_pistas[pista_atual][2]
        elif info_pistas[pista_atual][0] == "Descida":
            velocidade_saida = velocidade_entrada + info_pistas[pista_atual][2]
        
        venceu_corrida = corrida(velocidade_saida, glitchs, info_pistas, pista_atual + 1, venceu_corrida)
        tempo_gasto[acao] += info_pistas[pista_atual][1]/velocidade_entrada

    tempo_termino[0] = min(tempo_gasto)
    
    return venceu_corrida

#INICIO
print("Calibrando a gravidade e o atrito da pista...\n")
tempo_gasto = [0, 0, 0]
tempo_termino = [0]
condicoes_base = [int(condicao) for condicao in str(input()).split()] #*Cria uma lista com quantas pistas teram [0], a velocidade inicial da Vanellope [1] e a quantidade de glitch [2]
informacoes_pista = [] #*Lista que vai guardar as informações de cada pista_atual

for pistas in range(condicoes_base[0]):
    info_pista = str(input()).split()
    informacoes_pista.append([info_pista[0]] + [float(valor) for valor in info_pista[1:]]) #*Informações da pista_atual | [0] -> Tipo; [1] -> Tamanho; [2] e [3] são os parametros P1 e P2

resultado_corrida = corrida(condicoes_base[1], [condicoes_base[2]], informacoes_pista, 0, False)

if resultado_corrida:
    print(f"A corrida foi um sucesso! Tempo minimo cravado: {tempo_termino}s.")
else:
    print("Bug fatal! Vanellope capotou e o kart virou pixels.")

### MUDAR MUITA COISAS