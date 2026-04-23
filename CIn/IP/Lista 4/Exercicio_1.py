#PERIGOS DE FIARLONGO

chefe = (input()) #* Recebendo nome do Chefe que será enfrentado

#Prints Em Relação ao Chefe Enfrentado
if chefe == "Tessela": #* Print Tessela
    print("Tessela: Ha Ha Ha! Parece que a aranha retornou.\n")
elif chefe == "Grande Mãe Seda":
    print("Hornet: Monarca, seu reino de tirania acaba aqui!\n")
elif chefe == "A Última Juíza":
    print("Hornet: Não posso recuar agora, a cidadela está logo ali.\n")
else:
    print(f"Hornet: {chefe}, levante sua lâmina!\n")

#Funções Para A Batalha
def actions_hornet(action): #* Função Hornet 
    if action == "Ferrão":
        dano_hornet = 10
        seda = 2
        return dano_hornet, seda
    elif action == "Ataque de Seda":
        dano_hornet = 10
        seda = -3
        return dano_hornet, seda
    elif action == "Vincular":
        vida_curada = 3
        seda = -8
        return vida_curada, seda
    
def actions_boss(reaction): #* Função do Chefe
    if reaction == "Acerto":
        dano_chefe = 1
        return dano_chefe
    elif reaction == "Duplo Acerto":
        dano_chefe = 2
        return dano_chefe
    elif reaction == "Errou":
        esquiva = True
        return esquiva
    
def sistem_battle(acao, mascaras_recuperadas, mask_hornet, carretel, seda_recuperada, seda_desperdicada, vida_chefe, total_sedas_recuperadas, total_sedas_utilizadas): #* Função Combate
    ##Status Da Hornet
    
    ##Averiguando ação
    if acao == "Ferrão":
        dano_causado, seda_recuperada = actions_hornet(acao) #*Pegando os valores da função

        vida_chefe -= dano_causado #*Causando dano no chefe
        carretel += seda_recuperada #*Pegando seda
        if carretel > 8: #*Garante que não passe de 8 sedas
            carretel = 8

        total_sedas_recuperadas += seda_recuperada #*Armazena o total de sedas geradas

    elif acao == "Ataque de Seda":
        dano_causado, seda_usada = actions_hornet(acao)

        if carretel >= 3: #*Se tiver Seda o Suficiente
            carretel += seda_usada
            total_sedas_utilizadas += seda_usada
            vida_chefe -= dano_causado

    elif acao == "Vincular":
        mascaras_recuperadas, seda_usada = actions_hornet(acao)

        if carretel == 8:
            carretel = 0
            total_sedas_utilizadas += 8
            mask_hornet += mascaras_recuperadas
            if mask_hornet > 5:
                mask_hornet = 5

    elif acao == "Acerto":
        dano_sofrido = actions_boss(acao)
        
        mask_hornet -= dano_sofrido
    
    elif acao == "Duplo Acerto":
        dano_sofrido = actions_boss(acao)
        
        mask_hornet -= dano_sofrido
    elif acao == "Errou":
        actions_boss(acao)

    seda_desperdicada = total_sedas_recuperadas - total_sedas_utilizadas

    return mask_hornet, mascaras_recuperadas, carretel, seda_desperdicada, vida_chefe, total_sedas_utilizadas, total_sedas_recuperadas

#Combate
batalha = True
hornet_win = False
##Status Da Hornet
mask_hornet = 5
carretel = 0
seda_recuperada = seda_desperdicada = mascaras_recuperadas = 0
total_sedas_recuperadas = total_sedas_utilizadas = 0
##Status Do Chefe
vida_chefe = 140
while batalha:
    acao_hornet = str(input())
    mask_hornet, mascaras_recuperadas, carretel, seda_desperdicada, vida_chefe, total_sedas_utilizadas, total_sedas_recuperadas = sistem_battle(acao_hornet, mascaras_recuperadas, mask_hornet, carretel, seda_recuperada, seda_desperdicada, vida_chefe, total_sedas_recuperadas, total_sedas_utilizadas)
    
    if vida_chefe > 0:
        acao_boss = str(input())
        mask_hornet, mascaras_recuperadas, carretel, seda_desperdicada, vida_chefe, total_sedas_utilizadas, total_sedas_recuperadas = sistem_battle(acao_boss, mascaras_recuperadas, mask_hornet, carretel, seda_recuperada, seda_desperdicada, vida_chefe, total_sedas_recuperadas, total_sedas_utilizadas)

    if mask_hornet <= 0: #*Hornet Perde
        batalha = False
        
    if vida_chefe <= 0: #*Hornet Ganha
        batalha = False
        hornet_win = True

if hornet_win:
    print(f"RESULTADOS DA BATALHA\nMáscaras restantes: {mask_hornet}\nMáscaras recuperadas: {mascaras_recuperadas}\nSeda restante: {carretel}\nSeda desperdiçada: {seda_desperdicada}\n\nHornet: Não cairei tão fácil.")
else:
    print(f"Hornet: Hm?\nVida Restante: {vida_chefe}")