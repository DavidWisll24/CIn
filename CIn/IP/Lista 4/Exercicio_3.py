#TEM UM ZUMBI no MEU QUINTAL

#FUNÇÕES
def compra(comprado, qtd_sois): #*Função das compras das plantas
    if comprado == "Disparervilha" and qtd_sois >= 50:
        arsenal.append([comprado, 1, 1]) #*Adiciona a planta no Arsenal | [0] -> Planta; [1] -> Vida; [2] -> Dano
        gasto = 50 #* Gasto correspondente a planta
        return gasto #*Retorna o valor gato na compra
    elif comprado == "Noz-Obstáculo" and qtd_sois >= 75:
        arsenal.append([comprado, 2])
        gasto = 75 
        return gasto
    elif comprado == "Gelervilha" and qtd_sois >= 100:
        arsenal.append([comprado, 1, 1])
        gasto = 100
        return gasto
    else:
        return 0

def combate(): #*Função do combate
    ##Ataque Plantas
    i = 0
    
    while qtd_plantas[0] > i: #* Dá dano para cada planta ofensiva
        if arsenal[i][0] == "Gelervilha" or arsenal[i][0] == "Disparervilha":
            zumbi[1] -= 1
            if arsenal[i][0] == "Gelervilha" and zumbi[2] > 1 and (zumbi[0] != "Zumbi do Jornal" or zumbi[1] <= 5 and zumbi[0] == "Zumbi do Jornal"): #*Caso possível, diminui a velocidade do zumbi pelo efeito da Gelervilha
                zumbi[2] -= 1
            elif arsenal[i][0] == "Gelervilha" and zumbi[0] == "Zumbi do Jornal" and zumbi[2] > 2: #*Caso Especial: Velocidade minima do Zumbi do Jornal, após perder o jornal, é 2
                zumbi[2] -= 1
        i += 1

    ##Condição Especial
    if zumbi[0] == "Zumbi do Jornal" and zumbi[1] == 5:
        zumbi[2] += 1

    if zumbi[1] > 0: #*Se o zumbi sobreviver
        passos = 0 #*Quantos passos o zumbi deu na matriz
        planta_encontrada = False #*Verifica se uma planta foi encontrada

        while passos < zumbi[2] and not(planta_encontrada):
            passos += 1

            if arsenal[arsenal.index(zumbi) - 1] !=  []: #*Verifica se para onde o zumbi vai é uma planta
                ##Condição Especial - Zumbi Saltador
                while zumbi[0] == "Zumbi Saltador" and arsenal[arsenal.index(zumbi) - 1][0] == "Noz-Obstáculo":
                    arsenal[arsenal.index(zumbi) - 1] = zumbi
                    arsenal.pop()
                    qtd_plantas[0] -= 1 #*Diminui a quantidade de plantas totais vivas
                    if arsenal.index(zumbi) == 0:
                        derrota = True #*Zumbi venceu
                        return derrota

                planta_encontrada = True #*Encontrou uma planta
                arsenal[arsenal.index(zumbi) - 1][1] -= 1 #*Ataca a planta

                if arsenal[arsenal.index(zumbi) - 1][1] == 0: #*Se a planta morrer
                    qtd_plantas[0] -= 1 #*Diminui a quantidade de plantas totais vivas
                    arsenal[arsenal.index(zumbi) - 1] = zumbi #*O zumbi assume o lugar
                    arsenal.pop()
                    print("NOMNOMNOM!")
            
            elif arsenal[arsenal.index(zumbi) - 1] == []: #* Se não tiver nada
                arsenal[arsenal.index(zumbi) - 1] = zumbi #*Anda normalmente
                arsenal.pop()

            if arsenal.index(zumbi) == 0:
                derrota = True #*Zumbi venceu
                return derrota
    
#INICIANDO A COMPRAS
print("O quintal está sendo invadido! Prepare a melhor linha de defesa possível!")
qtd_sois = int(input()) #*Recebe quantos sois se tem
finalizado = False #*Diz que as compras não acabaram
arsenal = [] #*Local onde é armazenado as plantas compradas para a batalha

while not(finalizado): #*Vai comprando até acabar o estoque de sois ou receber FIM
    nome_planta = str(input()) #*Pede o nome da planta a ser comprada

    if nome_planta == "FIM": #*Input que encerra as compras
        finalizado = True

    else: #*Realiza as compras
        gasto = compra(nome_planta, qtd_sois) #*Retorna a quantidade gasta na compra

        if gasto == 0: #*Quer dizer que não tinha dinheiro pra comprar a planta:
            print("Você não tem sóis suficientes para isso!")
        
        else: #*Se tinha dinheiro
            qtd_sois -= gasto
#FIM das Compras

qtd_plantas = [len(arsenal)]

#Batalha
print("Lá vem o zumbi... espero que suas plantas estejam preparadas!")
while len(arsenal) < 17:
    arsenal.append([]) #*Adaptando o arsenal para ser o campo de batalha

nome_zumbi = str(input()) #*Recebe o tipo de Zumbi que ataca

##Definindo Características do Zumbi
if nome_zumbi == "Zumbi Normal":
    zumbi = ["Zumbi Normal", 10, 2] #* [0] -> nome; [1] -> vida; [2] -> velocidade
    arsenal.append(zumbi)
elif nome_zumbi == "Zumbi Cabeça-de-Cone":
    zumbi = ["Zumbi Cabeça-de-Cone", 14, 2]
    arsenal.append(zumbi)
elif nome_zumbi == "Zumbi do Jornal":
    zumbi = ["Zumbi do Jornal", 10, 2]
    arsenal.append(zumbi)
elif nome_zumbi == "Zumbi Saltador":
    zumbi = ["Zumbi Saltador", 10, 2]
    arsenal.append(zumbi)

derrota = False #*Zumbi venceu

while zumbi[1] > 0 and not(derrota):
    derrota = combate()

if derrota: #*Se o Zumbi nos derrotar
    print("O zumbi chegou à porta! Você perdeu!")

else: #*Se o Zumbi for derrotado
    print("Bom trabalho! Dave Doidão nunca esteve tão feliz...")
