D = int(input())
C = int(input())

horas_reais = D*1.5
ticks = horas_reais*3600*20

T = round(ticks/C)

print(T)