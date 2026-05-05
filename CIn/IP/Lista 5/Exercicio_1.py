#A DIVISA JUSTA DA BRANCA DE NEVE

#Função Recursiva
def qtd_macas(dias):
    if dias == 0:
        return 0
    elif dias <= 2:
        soma = 1
        return soma
    else:
        soma = qtd_macas(dias-2) + qtd_macas(dias-1)
        return soma
    
#INICIO
print("Espelho, espelho meu, quantas maçãs a árvore deu?")

#Pedindo o dia da colheita
dia_colheita = int(input())
rendimento_colheita = qtd_macas(dia_colheita) #*Recebe quantas maças foram colhidas

print(f"A árvore rendeu {rendimento_colheita} maçãs no dia {dia_colheita}.")

#Divisão das maças
if rendimento_colheita < 7: #*Caso não tenha o suficiente para alimentar os anões:
  print("Oh não! A colheita não foi suficiente para os sete anões.")
  
else: #*Se for possivel dividir entre os anões
    macas_por_anao = rendimento_colheita // 7 #Cada anão ganha igualmente, sem frações
    macas_bneve = rendimento_colheita % 7 #* Branca de Neve fica com o resto

    print(f"Cada anão receberá {macas_por_anao} maçã(s) e Branca de Neve ficará com a sobra de {macas_bneve} maçã(s).")

    if macas_bneve == 0: #*Ou seja, sobrou nada para ela
        print("A divisão foi perfeita! Nenhuma maçã sobrou para a torta da Branca de Neve.")