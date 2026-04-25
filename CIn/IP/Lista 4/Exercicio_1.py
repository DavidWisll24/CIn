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
        sistem_carretel[0] += 2 #* Pondo no carretel
        sistem_carretel[1] += 2 #* Pondo no tatal de seda feita
        return dano_hornet
    elif action == "Ataque de Seda":
        if sistem_carretel[0] >= 3:
            dano_hornet = 20
            sistem_carretel[0] -= 3 #* Tirando do carretel
            sistem_carretel[2] += 3 #* Somando na seda gasta
            return dano_hornet
        else:
            return 0
    elif action == "Vincular":
        if sistem_carretel[0] == 8:
            vida_curada = 3
            sistem_carretel[0] -= 8 #* Tirando do carretel
            sistem_carretel[2] += 8 #* Somando na seda gasta
            return vida_curada
        else:
            return 0
        
def actions_boss(reaction): #* Função do Chefe
    if reaction == "Acerto":
        dano_chefe = 1
        return dano_chefe
    elif reaction == "Acerto Duplo":
        dano_chefe = 2
        return dano_chefe
    elif reaction == "Errou":
        return 0
    
def sistem_battle(acao, vida_chefe): #* Função Combate
    ##Status Da Hornet
    
    ##Averiguando ação
    if acao == "Ferrão":
        dano_causado = actions_hornet(acao) #*Pegando os valores da função

        vida_chefe -= dano_causado #*Causando dano no chefe
        if sistem_carretel[0] > 8: #*Garante que não passe de 8 sedas
            sistem_carretel[0] = 8

    elif acao == "Ataque de Seda":
        dano_causado = actions_hornet(acao)
        vida_chefe -= dano_causado

    elif acao == "Vincular":
        mascaras_recuperadas = actions_hornet(acao)
        aux = mask_hornet[0]
        mask_hornet[0] += mascaras_recuperadas #* Curando
        if mask_hornet[0] > 5:
            mask_hornet[0] = 5
        mask_hornet[1] += mask_hornet[0] - aux #* Vendo quantas máscaras foram geradas

    elif acao == "Acerto":
        dano_sofrido = actions_boss(acao)
        
        mask_hornet[0] -= dano_sofrido
    
    elif acao == "Acerto Duplo":
        dano_sofrido = actions_boss(acao)
        
        mask_hornet[0] -= dano_sofrido
    elif acao == "Errou":
        actions_boss(acao)

    seda_desperdicada = sistem_carretel[1] - sistem_carretel[2]

    return seda_desperdicada, vida_chefe

#Combate
batalha = True
hornet_win = False
##Status Da Hornet
mask_hornet = [5, 0] #* [0] Máscaras da Hornet; [1] Máscaras recuperadas
sistem_carretel = [0, 0, 0] #* [0] é o carretel de seda; [1] é total de seda geradas; [2] total de seda gasta
seda_desperdicada = 0
##Status Do Chefe
vida_chefe = 140
while batalha:
    acao_hornet = str(input())
    seda_desperdicada, vida_chefe = sistem_battle(acao_hornet, vida_chefe)
    
    if vida_chefe > 0:
        acao_boss = str(input())
        seda_desperdicada, vida_chefe = sistem_battle(acao_boss, vida_chefe)

    if mask_hornet[0] <= 0: #*Hornet Perde
        batalha = False
        
    if vida_chefe <= 0: #*Hornet Ganha
        batalha = False
        hornet_win = True

if hornet_win:
    print(f"RESULTADOS DA BATALHA\nMáscaras restantes: {mask_hornet[0]}\nMáscaras recuperadas: {mask_hornet[1]}\nSeda restante: {sistem_carretel[0]}\nSeda desperdiçada: {seda_desperdicada}\n\nHornet: Não cairei tão fácil.")
else:
    print(f"Hornet: Hm?\nVida Restante: {vida_chefe}")