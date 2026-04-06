dinheiro_inicial = int(input())
modelo = ""
compra = ""
custo = 0
quantidade_compras = 0
custo_full = 0

print(f"A família possui {dinheiro_inicial} ainda, talvez ele fique tranquilo hoje")

while dinheiro_inicial > 0:
    compra = input()
    if compra == "Amauri":
        print("Sabia que vocês estão loucos, hora de encerrar essa loucura!")
        dinheiro_inicial = 0
    else:
        custo = int(input())
        aux = dinheiro_inicial
        
        if custo <= dinheiro_inicial:
            dinheiro_inicial -= custo
            custo_full += custo
            quantidade_compras += 1
            if compra.lower() == "carro":
              modelo = input()
            
            if custo > 500000:
                print(f"Enlouqueceram de vez {custo} reais num(a) {compra}")
            elif custo < 1000:
                print(f'Será que se acalmaram?! {compra} por "somente" {custo} reais')
            else:
                print(f"Gastaram {custo} reais para comprar um(a) {compra}")
                    
            if compra.lower() == "carro":        
              if modelo.lower() == "chevette":
                  print("chevette : Relembrando as origens será?")
              elif modelo.lower() == "jeep":
                  print("jeep : Será que ele tá se preparando para outra aventura que não irá?")
              elif modelo.lower() == "bmw":
                    print("bmw : Já to vendo o facebook dele cheio de foto me marcando 🙁")        
                
        if custo > aux or dinheiro_inicial == 0:
            print("Enlouqueceram? Vocês estão falidos")
            dinheiro_inicial = 0

print(f"{quantidade_compras} - {custo_full} reais")