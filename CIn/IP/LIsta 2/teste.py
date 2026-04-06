pilha = ''
a = -1
valve = True
validação = ["[]{[]}", "({[({[])]})", "()({}[[]]", "[][][][][]()", "(){", "[]}", "({)}", "[(])"]

while a < 7:
    pilha = ''
    valve = True
    a += 1
    for i in validação[a]:
        if i == '(' or i == '[' or i == '{':
            pilha += i

        else:
            if pilha == '':
                valve = False
            
            else:
                ultimo = ''

                for j in pilha:
                    ultimo = j

                if ultimo == '(' and i != ')' or ultimo == '[' and i != ']' or ultimo == '{' and i != '}':
                    valve = False 

                else:
                    nova_pilha = ''
                    tamanho = len(pilha)
                    contador = 0

                    for p in pilha:
                        if contador < tamanho - 1:
                            nova_pilha += p

                        contador += 1
                    pilha = nova_pilha

    if pilha != '':
        valve = False

    if valve == True:
        print("Valido")

    else:
        print("Invalido")