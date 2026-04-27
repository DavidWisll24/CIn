#TEM UM ZUMBI no MEU QUINTAL

#FUNÇÕES
def compra(comprado):
    arsenal.append(comprado)
    if comprado == "Disparervilha":
        gasto = 50 #* Gasto correspondente a planta
        return gasto #*Retorna o valor gato na compra
    elif comprado == "Noz-Obstáculo":
        gasto = 75 
        return gasto
    elif comprado == "Gelervilha":
        gasto = 100
        return gasto

#INICIANDO A COMPRAS
qtd_sois = str(input()) #*Recebe quantos sois se tem
finalizado = False #*Diz que as compras não acabaram
arsenal = [] #*Local onde é armazenado as plantas compradas para a batalha

while qtd_sois > 0 and not(finalizado): #*Vai comprando até acabar o estoque de sois ou receber FIM
    nome_planta = str(input) #*Pede o nome da planta a ser comprada

    if nome_planta == "FIM": #*Input que encerra as compras
        finalizado = True

    else:
        pass