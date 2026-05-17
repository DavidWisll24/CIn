#OS PRESSÁGIOS DA FLORESTA ANCESTRAL DE MERIDA

#Funções Recursivas
def special_fatorial(num): #*Função do Ritual para o Antigo Sinal
    if num <= 1: #*Caso Base
        return 1
    
    if num % 2 == 0:
        resultado = num * special_fatorial(num // 2 ) #*Divisão inteira para  garantir a variável como int, sabendo que todo num par / 2 resulta em um inteiro
        return resultado

    ##Se o número não for menor ou igual a 1 e não for par, ele cai na condição de ser impar, mas por legibilidade, então vou omitir um terceiro if
    resultado = num + special_fatorial(num - 1)
    return resultado

def soma_digitos(num_soma): #*Função que soma os digitos do valor recebido
    num_soma = abs(num_soma) #*Garante números positivos para a soma

    if num_soma < 10: #*Se tiver só um digito
        return num_soma
    
    final_num_soma = num_soma % 10 #*Pega o último digito do número
    resto_num_soma = num_soma // 10 #*Pega o resto do número

    soma = final_num_soma + soma_digitos(resto_num_soma) #*Soma cada digito

    return soma

def fibonacci_generalizada(num, memorias, numeros_fib): #*Construção do Eco | numeros_fib é uma váriavel auxiliar que sempre recebe [0], sendo utilizada para garantir eficiencia da recursão
    if num == 0: #*Caso Base
        return 0
    
    if num < memorias and num >= 1: #*Constroi a lista de termos até k-1
        numeros_fib += [1]*(memorias - 1)
        return 1

    if memorias <= num: #*Termos maiores ou igual a k
        fibonacci_generalizada(num-1, memorias, numeros_fib) #*Monta a lista
        num_fib = sum((numeros_fib[num-memorias:])) #*Gera os termos de Fib maior/igual que k
        numeros_fib.append(num_fib) #*Adiciona cada termo seguinte da sequencia de Fibonacci

    valor_final = numeros_fib[num]
    return valor_final

def verificador_primo(valor, teste=2): #*Verifica se o número recebido é primo
    if valor < 2: #*O menor primo é 2
        return False
    if teste > valor**(1/2): #*Se nenhum número menor que a raiz quadrada dele dividir ele, ele é primo
        return True
    if valor % teste == 0: #*Se for divisivel por alguem antes da raiz quadrada dele mesmo, não é primo
        return False
    
    return verificador_primo(valor, teste + 1)
    
def repetidor(lista, leitura = 0): #*Usado para ativar a decodificação para cada n termo
    if leitura == len(lista):
        return 0
    decodificacao(lista[leitura])

    repetidor(lista, leitura + 1)
    return 0

def decodificacao(numero): #*Função para descobrir o código secreto da floresta
    sinal_antigo = special_fatorial(numero) % 500 #*Recebe o valor dosinal antigo

    indice_presagio = soma_digitos(sinal_antigo) % 500 #*Descobre o indice do pressagio

    if indice_presagio < 2: #*Arrumando o valor do indice, se necessário
        indice_presagio = 2

    memorias_passado = soma_digitos(indice_presagio) % 500 #*Revela a quantidade de memorias do passado

    if memorias_passado < 2: #*Arrumando o valor das memorias, se necessário
        memorias_passado = 2

    eco_luzes = (fibonacci_generalizada(indice_presagio, memorias_passado, [0])) % 500 #*Pega o valor do eco das luzes

    valor_presagio = sinal_antigo + eco_luzes #*Recebe o valor do significado do pressagio

    significado_pressagio = verificador_primo(valor_presagio) #*Usado para verificar o significado do pressagio

    if significado_pressagio: #*Verifica o que o pressagio diz
        resultado = "SEGURO"
    else:
        resultado = 'PERIGOSO'

    print(f"Numero {numero:03} | Sinal = {sinal_antigo:03} | Indice = {indice_presagio:03} | Memorias = {memorias_passado:03} | Eco das Luzes = {eco_luzes:03} | Julgamento: {resultado}")

def listar_inteiros(lista, contador = 0): #*Função para gerar uma lista com os valores numericos recebidos
    if contador == len(lista):
        return lista
    
    lista[contador] = int(lista[contador])
    listar_inteiros(lista, contador + 1)
    
    return lista

#INICIO
numeros = str(input()) #*Recebe os números que serão analisados
lista_numeros = listar_inteiros(numeros[1:-1].split(", "))

repetidor(lista_numeros)