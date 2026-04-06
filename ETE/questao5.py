idaden = 0
idade = 0
idadem = 0
idademn = 0
n = 0
m = 0

for i in range (10):
    idade = int(input("Digite sua idade, em anos: "))
    sexo = input("Informe seu sexo( H para homem e M para mulheres): ")

    if sexo == "M":
        idadem += idade
        m += 1

    elif sexo == "H":
        idaden += idade
        n += 1

    idademn += idade


print("Media de idade dos homens é: ", idaden/n)
print("Media de idade dos mulheres é: ", idadem/m)
print("Media de idade geral é: ", idademn/10)
