#Recebendo a seção
num_secao = int(input())

##Os motivos ocultos de thomas e Minho
if num_secao < 9:
    print("Essa seção foi excluída por motivos que não podem ser revelados. Entre no labirinto e corra novamente.")

else:
    #Mapeando o labirinto
    ##Lista dos valores entre a seção inicial (2) e seção final (n) pelo Postulado
    lista_entre_2_2k = [num_entre_2_2k for num_entre_2_2k in range(num_secao*2 + 1) if num_entre_2_2k > 2]

    ##Regra do Crivo (lista sem repetição)
    """
    Comentário que ajuda a entender o processo

    ## Pensando na lógica
    Pelo Crivo de Eurastoteles, 
    a ideia para achar os primos que existem até 2k é eliminar de uma lista
    com todos os termos de 2 até 2k os multipos de outros numeros diferentes de 1(ou seja, números que não são primos)
    Então:
    A lista se inicia em 2, e como multipos
    nada mais é que 2 somado x vezes, dá para aplicar
    essa lógica no código, andando a lista de 2 em 2, ou em p em p para um primo qualquer.
    Acho que um for (i², 2k, i)resolve (o inicial é i² para evitar eliminar o próprio número primo).
    """
    for i in range(2, int((num_secao*2)**0.5) +1):
        for j in range(i*i, 2*num_secao + 1, i):
            if j in lista_entre_2_2k:
                lista_entre_2_2k.remove(j)

    ###Salvando a lista na ordem crescente
    lista_crescente = lista_entre_2_2k.copy()

    #Lista com repetição
    lista_repetição = []
    for a in range(2, num_secao + 1):
        lista_secao_secao = [x for x in range(a*2 + 1) if x > a]

        for i in range(2, int((a*2)**0.5) +1):
            for j in range(i*i, 2*a + 1, i):
                if j in lista_secao_secao:
                    lista_secao_secao.remove(j)
        lista_repetição += lista_secao_secao

    ##Usando Bubble Sort para ordenar em ordem decrescente
    for a in range(len(lista_entre_2_2k) -1):
        for b in range(a, len(lista_entre_2_2k) -1):
            if lista_entre_2_2k[a] < lista_entre_2_2k[b + 1]:
                lista_entre_2_2k[a], lista_entre_2_2k[b+1] = lista_entre_2_2k[b+1], lista_entre_2_2k[a]

    ##Aplicando Fórmula de Saída
    possivel_saida = (lista_entre_2_2k[0] + 1) / 2

    #Criando String dos primos
    primos = str(lista_entre_2_2k[0])
    for primo in range(1, len(lista_entre_2_2k)):
        primos += ' ' + str(lista_entre_2_2k[primo])

    print(primos)

    #Mostrando quantas vezes cada primo apareceu
    for ordem in lista_crescente:
        print(f"O número {ordem} apareceu {lista_repetição.count(ordem)} vezes.")
    print()

    #Prints relacionados a possível saída
    if possivel_saida == num_secao:
        print("Thomas: O cálculo apontou para a seção que você estava! Isso é uma armadilha.\nMinho: O Thomas tem razão.")

    elif (num_secao - possivel_saida) == 1:
        print("Thomas: A decodificação diz que a saída está na seção imediatamente anterior a que você estava.\nMinho: Se isso realmente for válido, então restam 2 opções de saída.")

    elif (num_secao - possivel_saida) > 1:
        print("De todos os cálculos feitos, a única seção que apresentou diferença maior do que 1 foi essa.")