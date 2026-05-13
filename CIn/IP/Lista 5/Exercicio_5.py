#A CORRIDA DE KARTS

#Funções Recursivas


#INICIO
condicoes_base = [int(condicao) for condicao in str(input()).split()] #*Cria uma lista com quantas pistas teram [0], a velocidade inicial da Vanellope [1] e a quantidade de glitch [2]
acoes = [10.0, 0, -10.0] #*Ações possíveis que devem ser realizadas em cada pista nova | [0] -> Acelerar; [1] -> Manter; [1] -> Frear