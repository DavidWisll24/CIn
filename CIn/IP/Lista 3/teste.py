"""
lista = [4, 25, 8, 9, 1, 7, 24, 11, 12, 74, 2, 6, 7, 9, 74, 47]

for i in range(len(lista) - 1):
    for j in range(i, len(lista) - 1):
        if lista[i] > lista[j+1]:
            lista[i], lista[j+1] = lista[j+1], lista[i]

print(lista)
"""
"""
while True:
    lista_repetição = []
    valor = int(input())
    for a in range(2, valor + 1):
        lista = [x for x in range(a*2 + 1) if x > a]

        for i in range(2, int((a*2)**0.5) +1):
            for j in range(i*i, 2*a + 1, i):
                if j in lista:
                    lista.remove(j)
        lista_repetição += lista
    print(lista_repetição)
"""
"""
while True:
    valor = int(input())

    potencia = 0
    binario = ''

    while valor//(2**(potencia+1)) != 0:
        potencia += 1

    for i in range(0, potencia + 1, 1):
        if valor >= 2**(potencia-i):
            binario += "1"
            valor = valor - 2**(potencia-i)
        else:
            binario += "0"

    print(binario)

"""
"""
i = int(input())
j = int(input())
matriz = []
for a in range(i):
    n = input()
    lista = n.split(" - ")
    for b in range(len(lista)):
        lista[b] = float(lista[b])
    matriz.append(lista)

for c in matriz:
    print(c)

matriz_mapeada = matriz.copy()
for c in matriz_mapeada:
    for d in range(len(c)):
        matriz_mapeada[matriz_mapeada.index(c)][d] = '.'

print(matriz_mapeada)
"""
"""
mapeada = False
i_linhas_matriz = int(input())
j_colunas_matriz = int(input())
matriz_frequencia = []

for a in range(i_linhas_matriz):
    frequencias_recebidas = input()
    linha_frequencia = frequencias_recebidas.split(" - ")
    for b in range(len(linha_frequencia)):
        linha_frequencia[b] = float(linha_frequencia[b])
    matriz_frequencia.append(linha_frequencia)

##Gerando matriz mapeada por Doc
###Definindo matriz auxiliar para ão estourar os valores do index
matriz_frequencia_analise = [[0]+elemento+[0] for elemento in matriz_frequencia]
matriz_frequencia_analise.append([0]*(j_colunas_matriz + 2))
matriz_frequencia_analise.insert(0, [0]*(j_colunas_matriz + 2))

###Definindo cada posição com não visitada
matriz_mapeada = matriz_frequencia.copy()
for c in matriz_mapeada:
    for d in range(len(c)):
        matriz_mapeada[matriz_mapeada.index(c)][d] = '.'

###Verificando a visinhaça
elemento = 1
coluna = 1


while not mapeada:
    if (matriz_frequencia_analise[elemento][coluna] > matriz_frequencia_analise[elemento][coluna - 1]
        and matriz_frequencia_analise[elemento][coluna] > matriz_frequencia_analise[elemento][coluna + 1]
        and matriz_frequencia_analise[elemento][coluna] > matriz_frequencia_analise[elemento + 1][coluna]
        and matriz_frequencia_analise[elemento][coluna] > matriz_frequencia_analise[elemento - 1][coluna]
    ):
        matriz_mapeada[elemento-1][coluna-1] = 'X'
        mapeada = True

    else:
        freq_proximas = [matriz_frequencia_analise[elemento][coluna + 1], matriz_frequencia_analise[elemento][coluna - 1], matriz_frequencia_analise[elemento + 1][coluna], matriz_frequencia_analise[elemento - 1][coluna]]

        for bubble in range(len(freq_proximas) - 1):
            for sort in range(bubble, len(freq_proximas) - 1):
                if freq_proximas[bubble] < freq_proximas[sort + 1]:
                    freq_proximas[bubble], freq_proximas[sort + 1] = freq_proximas[sort + 1], freq_proximas[bubble]

        if freq_proximas[0] == matriz_frequencia_analise[elemento][coluna + 1]:
            matriz_mapeada[elemento-1][coluna-1] = '>'
            elemento = elemento
            coluna = coluna + 1
        elif freq_proximas[0] == matriz_frequencia_analise[elemento][coluna - 1]:
            matriz_mapeada[elemento-1][coluna-1] = '<'
            elemento = elemento
            coluna = coluna - 1
        elif freq_proximas[0] == matriz_frequencia_analise[elemento + 1][coluna]:
            matriz_mapeada[elemento-1][coluna-1] = 'v'
            elemento = elemento + 1
            coluna = coluna
        elif freq_proximas[0] == matriz_frequencia_analise[elemento - 1][coluna]:
            matriz_mapeada[elemento-1][coluna-1] = '^'
            elemento = elemento - 1
            coluna = coluna

for hhh in matriz_mapeada:
    print(hhh)
"""
"""
estado_inicial = input()
    
##Verificando quantos vezes os bits mudaram
potencia = 0
binario_antigo = estado_inicial
mudancas = 0

while int(binario_antigo, 2) < 88:
    ###Variáveis
    binario_atual = ''
    potencia = 0
    valor_decimal = int(binario_antigo, 2) + 1

    while valor_decimal//(2**(potencia+1)) != 0:
        potencia += 1

    for i in range(0, potencia + 1, 1):
        if valor_decimal >= 2**(potencia-i):
            binario_atual += "1"
            valor_decimal = valor_decimal - 2**(potencia-i)
        else:
            binario_atual += "0"
    
    if len(binario_atual) < 7:
        binario_atual = '0'*(7 - len(binario_atual)) + binario_atual
    
    for new, old in zip(binario_atual, binario_antigo):
        if new != old:
            mudancas += 1

    binario_antigo = binario_atual
    print(binario_antigo, int(binario_antigo, 2))

print(mudancas)
"""
"""
matriz_mapeada = [[1, 2, 3, 4], [4, 3, 2, 1], [1, 2, 3, 4], [4, 3, 2, 1]]
for linha_print in matriz_mapeada:
    elemento = ""
    for coluna_print in range(len(linha_print)):
        elemento += str(matriz_mapeada[matriz_mapeada.index(linha_print)][coluna_print])
    print(elemento)

m = [i for i in input().split()]
print(m)
"""
"""
s_p_e_c_i_a_l = [int(atributo) for atributo in str(input()).split("-")] 

intervalo_erro = False
while not intervalo_erro:
    num_atributo_ok = 0 
    for intervalo in s_p_e_c_i_a_l: #*percorre cada valor na lista s.p.e.c.i.a.l
        if intervalo < 1 or intervalo > 10: #*Se não estiver no intervalo
            s_p_e_c_i_a_l = [int(atributo) for atributo in str(input()).split("-")] #*Pedindo novamente os valores
        else: #Se estiver no intervalo
            num_atributo_ok += 1 #*Pra cada atributo no intervalo, soma 1

    if num_atributo_ok == len(s_p_e_c_i_a_l): #*Se o números de atributos ok for igual ao número de atributos, tá tudo certo
        intervalo_erro = True
"""
"""
alpha = [letra for letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"]
coordenadas = [1]
matriz = [["b", 'c', 'd'], ["a", "a"]]
print(''.join([palavra_horizontal for palavra_horizontal in matriz[coordenadas[0]] if palavra_horizontal in alpha]))
"""
m = ['aba']

if 'a' in m:
    print("ok")