print("Avenida Brasil: A Vingança de Nina!")

#Definindo variáveis
quant_pendrive = int(input())
senha = ''
tentativas = ''
chance = 0
senha_atual = ''
sucess_quat_pendrive = 0

#Tentando acessar o pendrive
for i in range(quant_pendrive):
    #Zerando váriaveis
    tentativas = senha_atual = senha = ''
    chance = 0
    
    print(f"Descriptografando pendrive {i+1} de {quant_pendrive}...")
    senha =  input()
    
    #Criptografando a senha
    for j in senha:
        if j.isalpha():
            chance += 1
            senha_atual += "_"
        else:
            senha_atual += " "

    #Definindo quantidade de chances
    chance = chance * 2
    
    #Tentando decobrir a senha
    while (chance) > 0:
        #Pedindo uma letra
        letra = input()
        
        #Executando prints pedidos
        if letra in senha and letra not in tentativas:
            print("Nina: Boa, Tufão! Menos uma mentira da Carminha.")
            
            #Sistema estilo "jogo da forca"
            senha_teste = ''

            for l, a in zip(senha, senha_atual):
                if l == letra:
                    senha_teste += letra
                elif a != "_":
                    senha_teste += a
                elif l.isalpha():
                    senha_teste += "_"
                else:
                    senha_teste += " "

            senha_atual = senha_teste

        elif letra not in senha and letra not in tentativas:
            print("Carminha: Você é um idiota, Tufão! Isso não faz sentido.")
            
        elif letra in tentativas:
            print("Max: Ele já tentou isso, Carminha...")

        print(f"Senha: {senha_atual}")

        tentativas += letra
        chance -= 1

        #Condição de parada
        if senha_atual == senha:
            chance = -1
            sucess_quat_pendrive += 1

    if chance == -1:
        print(f"Tufão: Agora eu sei de toda a verdade! O pendrive {i + 1} está aberto.")

    elif chance == 0:
        print(f"Carminha: Consegui! As fotos do pendrive {i + 1} estão a salvo comigo.")

print(f"Conseguimos abrir {sucess_quat_pendrive} de {quant_pendrive} pendrives!")

porcent = (sucess_quat_pendrive / quant_pendrive)
if sucess_quat_pendrive == 0:
    print("Tufão continuará sendo enganado para sempre...")

elif 0.0 < porcent <= 0.5:
    print("Tufão descobriu algumas coisas, mas Carminha ainda tem poder.")

elif 0.5 < porcent < 1:
    print("A casa caiu para a Carminha! Quase todas as provas foram recuperadas.")

elif porcent == 1:
    print("Justiça por Rita! Todas as provas estão nas mãos de Tufão.")