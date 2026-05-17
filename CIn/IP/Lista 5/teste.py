"""
while True:
    def recursive(n):
        n = abs(n)
        if n < 10:
            return n
        
        num = n//10
        num2 = n%10
        soma = num2 + recursive(num)

        return soma

    print(recursive(int(input())))
"""
"""
def fib(n, prox=0, term_inicial=0, ter_final=1):
    if n == 0:
        return 0
    
    if prox == (n-1):
        return ter_final
    soma_final = ter_final+term_inicial
    return fib(n, prox + 1, ter_final, soma_final)

print(fib(12))
"""
"""
def fibonacci_generalizada(num, k):
    numeros_fib = [0]
    
    if num == 0:
        return 0
    
    if num < k and num >= 1:
        return 1
    
    for termo in range(1, k):
        numeros_fib.append(1)

    for casos in range(k, num + 1):
        num_fib = sum(numeros_fib[(casos - k):])
        numeros_fib.append(num_fib)

    return numeros_fib[num]
        
print(fibonacci_generalizada(12, 3))    
"""
"""
def fibonacci_generalizada(num, k, numeros_fib):
    if num == 0:
        return 0
    
    if num < k and num >= 1:
        numeros_fib += [1]*(k - 1)
        return 1

    if k <= num:
        fibonacci_generalizada(num-1, k, numeros_fib)
        num_fib = sum((numeros_fib[num-k:]))
        numeros_fib.append(num_fib)

    valor_final = numeros_fib[num]
    return valor_final
        
print(fibonacci_generalizada(12, 3, [0]))    
print(fibonacci_generalizada(13, 3, [0]))"""
"""
def verificador_primo(valor, teste=2):
    if teste > valor**(1/2):
        return True
    if valor % teste == 0:
        return False
    
    
    return verificador_primo(valor, teste + 1)
    
print(verificador_primo(4))"""
"""def repetidor(lista, leitura = 0):
    if leitura == len(lista):
        return 0
    print(4)
    
    repetidor(lista, leitura + 1)
    return 0

repetidor([2, 2, 2, 2, 2])
"""
def listar_inteiros(lista, contador = 0): #*Função para gerar uma lista com os valores numericos recebidos
    if contador == len(lista):
        return lista
    
    lista[contador] = int(lista[contador])
    listar_inteiros(lista, contador + 1)

    return lista
    
print(listar_inteiros(["2", "4"]))