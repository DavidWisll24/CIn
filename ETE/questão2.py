inicial = 0
novo = 0

for i in range(5):
    inicial = float(input("Digite um valor: "))

    if novo < inicial:
        novo = inicial

    
print("O maior valor digitado foi: ", novo )