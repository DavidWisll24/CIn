lista = '([)]'
validade = True


pilha = ''
for i in lista:
    if i == '(' or i == '[' or i == '{':
        pilha += i
    
    elif i == ')' or i == '}' or i == ']':
        if pilha == '':
            validade = False
        
        else:
            ultimo = ''

            for a in pilha:
                ultimo = a

            if ultimo == '(' and i == ')' or ultimo == '{' and i == '}' or ultimo == '[' and i == ']':
                nova_pilha = ''
                tamanho = len(pilha)
                novo_tamanho = 0

                for j in pilha:
                    if novo_tamanho != tamanho - 1:
                        nova_pilha += j
                    novo_tamanho += 1

                pilha = nova_pilha

            else:
                validade = False

if len(pilha) > 0:
    validade = False

print("Valido" if validade == True else "Invalido")