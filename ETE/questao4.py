valor = 0
quantidade = 0

for i in range(10):
    valor = float(input("Digite um valor:"))

    if valor > 10 and valor < 50:
        quantidade += 1

print("Você digitou", quantidade,  "valores entre 10 e 50.")