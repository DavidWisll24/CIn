#Variáveis
itens_caminhão = ''
continuar = True
pedidos_carol = input()
lista_carol = pedidos_carol.split(', ')
faltando_carol = lista_carol.copy()
lista_caminhao = []

#PRINT INICIAL
print("Pedido recebido! Vamos alocar os itens nos caminhões disponíveis.")

#Recebendo as informações dos itens nos caminhões
while continuar:
    itens_caminhão = input()

    if itens_caminhão == '--':
        continuar = False
    else:
        atual_caminhao = itens_caminhão.split(', ')
        lista_caminhao.append(atual_caminhao)

#Analisando cada caminhão
for i in range(len(lista_caminhao)):
    #Criando listas para verificar itens conseguidos e os faltantes 
    itens_tragos = [a for a in lista_caminhao[i] if a in lista_carol]
    
    for v in itens_tragos:
        if v in faltando_carol:
            faltando_carol.remove(v)

    #Verificando itens da lista de carol
    if len(itens_tragos) > 0:
        print(f"Ótimo, esse caminhão trouxe {itens_tragos}!")
    elif len(itens_tragos) == 0:
        print("Não encontramos nada que a Carol pediu nesse caminhão.")
    
    if len(faltando_carol) > 0:
        print(f"Ainda precisamos de {faltando_carol}.")

#PRINT FINAL
if len(faltando_carol) == 0:
    print("Conseguimos! A Carol ficará muito feliz :)")

else:
    print("Não conseguimos reunir todos os itens que a Carol precisa :(")