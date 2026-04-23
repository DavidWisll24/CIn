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

#Status Da Hornet
mask_hornet = 5
carretel = 0

#Status Do Chefe
vida_chefe = 140

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
    
def sistem_battle():
    print()