print("********************************\nBEM VINDO AO SISTEMA DE ENTREGAS\n********************************\n")

entregas = [12, 15, 8, 20, 17, 10, 14]
maior_entregas = sorted(entregas, reverse=True)
quant_dias_baixos = [x for x in entregas if x<10]
dias_altos = []
#Printa os dias e seu desempenho

for i in range(len(entregas)):
    if entregas[i] > 15:
        print(f"Excelente! No {i+1}° dia da semana o desempenho foi alto.")
        dias_altos.append(i+1)
    elif entregas[i] <= 15 and entregas[i] >= 10:
        print(f"Bom. No {i+1}° dia da semana o desempenho foi médio.")
    else:
        print(f"Que lastima. No {i+1}° dia da semana o desempenho das entregas foi BAIXO!")

print(f"Nessa semana tivemos {len(quant_dias_baixos)} dias com baixo desempenho.")
print(f"Essa semana a média de nossas entregas foi {(sum(entregas)/len(entregas)):.4f}!")
print(f"Nossa maior quantidade de entregas em um dia foi {maior_entregas[0]}")
print(f"Os dias de entrega alta foram {dias_altos}")
print(f"O nosso dia de pior desempenho foi {entregas.index(maior_entregas[-1]) + 1}, de index = {entregas.index(maior_entregas[-1])}")