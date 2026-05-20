#CENTROAVANTE: EGOÍSMO OU VITÓRIA

##Função
def ordenar(jogadores, desempate): #*Função para organizar do melhor para o pior jogador
    ordenado = dict() #*Dicionário que receberá os valores ordenados
    for posicao in range(len(jogadores)): #*Realiza para cada jogador
        ###Definindo Variáveis
        maior = -1 
        valor = 0
        key_nova = ''
        key_antiga = ''
        time = ''
        nome = ''

        for i in jogadores: #*Para cada jogador roda uma vez | i recebe a chave do primeiro e segue de um em um
            ###Descobre o maior
            if jogadores[i]['gols'] > maior: #*Se fez mais gols
                valor = jogadores[i]
                maior = jogadores[i]['gols']
                key_nova = f"{posicao + 1}"
                key_antiga = i
                time = jogadores[i]['selecao']
                nome = jogadores[i]['jogador']

            elif jogadores[i]['gols'] == maior: #*Se fez gols iguais
                time_atual = jogadores[i]['selecao'] 
                if desempate[str(time_atual)] < desempate[time]: #*Ve a seleção e compara
                    valor = jogadores[i]
                    maior = jogadores[i]['gols']
                    key_nova = f"{posicao + 1}"
                    key_antiga = i
                    time = jogadores[i]['selecao']
                    nome = jogadores[i]['jogador']  
                elif desempate[str(time_atual)] == desempate[time]: #*Se for a mesma nação
                    if jogadores[i]['jogador'] < nome: #*Compara o nome
                        valor = jogadores[i]
                        maior = jogadores[i]['gols']
                        key_nova = f"{posicao + 1}"
                        key_antiga = i
                        time = jogadores[i]['selecao']
                        nome = jogadores[i]['jogador']

        ordenado[key_nova] = valor #*Adiciona o valor no dicionário ordenado
        jogadores.pop(key_antiga) #*Apaga valores ordenados do dicionário já ordenados 

    return ordenado

##INICIO
print("Somente o melhor deve ser lembrado")

jogadores = dict() #*Defini dicionário para organizar os jogadores
jogador = '' #*Define variável
desempate = {"França":1, "Espanha":2, "Argentina":3, "Inglaterra":4, "Portugal":5, "Brasil":6, "Holanda":7, "Marrocos":8, "Bélgica":9, "Alemanha":10, "Croácia":11, "Colômbia":12, "Senegal":13, "México":14, "Estados Unidos":15, "Uruguai":16, "Japão":17, "Suíça":18, "Irã":19, "Turquia":20, "Equador":21, "Áustria":22, "Coreia Do Sul":23, "Australia":24, "Argélia":25, "Egito":26, "Canadá":27, "Noruega":28, "Panamá":29, "Costa Do Marfim":30, "Suécia":31, "Paraguai":32, "Tchéquia":33, "Escócia":34, "Tunísia":35, "Républica Democrática Do Congo":36, "Uzbequistão":37, "Catar":38, "Iraque":39, "Africa Do Sul":40, "Arábia Saudita":41, "Jordânia":42, "Bósnia-Herzgovina":43, "Cabo Verde":44, "Gana":45, "Curaçao":46, "Haiti":47, "Nova Zelândia":48} #*Usado no desempate

while jogador != "FIM": #*Recebe cada Jogador
    jogador = str(input()) #*Nome e Time
    if jogador != "FIM": #*Verifica se continua
        if jogador in jogadores: #*Se já apareceu
            jogadores[jogador]['gols'] += 1 #*Faz mais um gol
        else:#*Se não
            jogadores[jogador] = {'jogador':jogador.split(' - ')[0],'selecao':jogador.split(' - ')[1], 'gols':1} #*Adiciona no dicionário

jogadores_ordenados = ordenar(jogadores, desempate) #*Organiza o dicionário

print(f"O artilheiro foi {jogadores_ordenados['1']['jogador']} com {jogadores_ordenados['1']['gols']} gols")
print(f"Eu poderia falar do {jogadores_ordenados['2']['jogador']} mas ele é somente o primeiro a ser esquecido")
print(f"O {jogadores_ordenados['3']['jogador']} então, nem pensar")
