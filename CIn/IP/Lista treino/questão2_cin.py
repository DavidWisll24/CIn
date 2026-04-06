X = int(input())
Z = int(input())

H = float(((X-34)**2 + (Z-220)**2)**(1/2))
K = float(((X-0)**2 + (Z-0)**2)**(1/2))
S = float(((X-140)**2 + (Z-456)**2)**(1/2))

print("Distancia para Hogsmeade:", H)
print("Distancia para Kakarico:", K)
print("Distancia para Solitude:", S)