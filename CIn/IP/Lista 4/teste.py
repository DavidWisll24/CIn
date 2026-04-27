"""
for i in range(7,-1,-1):
    print(i)

tentativas = [int(valor_tentativa) for valor_tentativa in str(input()).split(" ")]
print(tentativas)
"""
"""
# etapa 1
def analizar_alvo(nivel_ameaca, status_armado):
    if nivel_ameaca >= 7 and status_armado:
        return 'Elite'
    elif nivel_ameaca >= 7 and not status_armado:
        return 'Executor'
    elif 4 <= nivel_ameaca < 7 and status_armado:
        return 'Veterano'
    elif 4 <= nivel_ameaca < 7 and not status_armado:
        return 'Operador'
    elif nivel_ameaca < 4:
        return 'Iniciante'
# etapa 2
def analisar_tentativas(lista_codigos):
    soma_total = sum(lista_codigos)
    quantidade = len(lista_codigos)
    
    if soma_total % quantidade == 0:
        return True
    else:
        return False
# etapa 3
def calcular_reflexao(ataques_inimigos):
    favoritos = [3, 5]
    refletidos = 0
    for ataque in ataques_inimigos:
        if ataque % 3 == 0 or ataque % 5 == 0:
            refletidos += 1
    return refletidos

print('Entendo… Vamos começar do começo.')
dia_inicial = int(input())
zero_vivo = True
dia_atual = dia_inicial

while dia_atual >= 0 and zero_vivo:
    musica_completa = input()
    musicas = musica_completa.split(' - ')
    autor_musica = musicas[1]

    alvo_input = input()
    partes_alvo = alvo_input.split(' - ')
    nome_alvo = partes_alvo[0]
    nivel_ameaca = int(partes_alvo[1])
    status_armado = partes_alvo[2] == 'sim'

    print(f'\n====== Restam {dia_atual} dias. ======')
    print(f'Escutando: {musica_completa}')

    # verificaçao dj
    if autor_musica == 'DJ Electrohead' and nome_alvo == 'DJ Electrohead':
        print('DJ Electrohead é morto na sua frente. Lhe avisaram para NÃO FALAR com ele.')
    else:
        tentativas_input = input().split()
        lista_codigos = []
        for item in tentativas_input:
            lista_codigos.append(int(item))

        # etapa 1 classificar alvo
        classificacao = analizar_alvo(nivel_ameaca, status_armado)
        print(f'Analisando alvo: {nome_alvo}... Classificação: {classificacao}')
        
        # ETAPA 2: Analisar tentativas
        if analisar_tentativas(lista_codigos):
            print(f'Missão Completa. | Manipulação temporal: {len(lista_codigos)} tentativa(s)')
            
            # etapa 3 ataques refletidos
            ataques_input = input().split()
            ataques_inimigos = []
            for item in ataques_input:
                ataques_inimigos.append(int(item))
            refletidos = calcular_reflexao(ataques_inimigos)
            print(f'Dragão refletiu {refletidos} ataque(s)!')
            
        else:
            print('Missão Fracassou! ZERO não foi capaz de assassinar o alvo e acabou morrendo. Nunca descobrirá o que realmente aconteceu.')
            zero_vivo = False

    dia_atual -= 1

# mensagem de encerramento
if zero_vivo:
    print('\n====== FIM DAS MISSÕES ======')
    print('Parabéns Subject ZERO! Seu trabalho deve ser recompensado. Nova dose do seu remédio esta aqui.')

"""
def clas_alvo(alvo):            #função da classificação de alvo
    parte = alvo.split(' - ')   #transformando em uma lista
    nome = parte[0]
    nivel = int(parte[1])
    armado = parte[2]
    if nivel >= 7 and armado == 'sim':        #aqui iniciam as verificações
        classificacao = 'Elite'
    elif nivel >= 7 and armado == 'nao':
        classificacao = 'Executor'
    elif nivel >= 4 and nivel < 7 and armado == 'sim':
        classificacao = 'Veterano'
    elif nivel >= 4 and nivel < 7 and armado == 'nao':
        classificacao = 'Operador'
    else:
        classificacao = 'Iniciante'
    print(f'Analisando alvo: {nome}... Classificação: {classificacao}')
    return classificacao

def ana_tentativas():           #função da analise de tentativas
    tentativas = input().split(' ')     #transformando em uma lista
    soma = 0                    #definindo a soma e a quantidade de tentativas que vai ser usada para calcular se é divisível
    qtd_tentativas = 0
    for t in tentativas:
        soma += int(t)          #somando o valor que recebe como um inteiro
        qtd_tentativas += 1
    resto = soma % qtd_tentativas       #cálculo se é divisivel
    if resto == 0:
        print(f'Missão Completa. | Manipulação temporal: {qtd_tentativas} tentativa(s)')
        return True             #retorna verdadeiro para continuar
    else:
        print('Missão Fracassou! ZERO não foi capaz de assassinar o alvo e acabou morrendo. Nunca descobrirá o que realmente aconteceu.')
        return False            #retorna falso porque para

def ataques_ref():              #função dos ataques refletidos
    refletidos = 0
    favoritos = [3, 5]
    ataques_inimigos = input().split(' ')       #colocando os ataques inimigos em uma variavel
    for i in ataques_inimigos:
        sobra = int(i) % favoritos[0]           #verificando se é multiplo de 3 (usando divisão com resto 0)
        conta = int(i) % favoritos[1]           #mesma coisa com o 5
        if sobra == 0 or conta == 0:
            refletidos += 1
    print(f'Dragão refletiu {refletidos} ataque(s)!')

print('Entendo… Vamos começar do começo.')
dia_inicial = int(input())
vivo = True

while dia_inicial >= 0 and vivo:         #loop que acontece enquanto houverem dias e ZERO estiver vivo
    musica = input()
    partes = musica.split(' - ')        #separando a lista para pegar a musica e o autor
    musica = partes[0]
    autor = partes[1]
    print(f'\n====== Restam {dia_inicial} dias. ======')
    print(f'Escutando: {musica} - {autor}')

    alvo = input()                      #pedindo o alvo aqui fora para verificar se é o dj

    if autor == 'DJ Electrohead' and 'DJ Electrohead' in alvo:
        print('DJ Electrohead é morto na sua frente. Lhe avisaram para NÃO FALAR com ele.')
    else:                           #se não for o dj, pede a função da classificação do alvo 
        clas_alvo(alvo)
        sucesso = ana_tentativas()      #esse sucesso foi definido no return, se ele for verdadeiro, pede a funçao do ataque
        if sucesso:
            ataques_ref()
        else:
            vivo = False
    
    dia_inicial -= 1

if vivo:            #se terminar vivo
    print('\n====== FIM DAS MISSÕES ======')
    print('Parabéns Subject ZERO! Seu trabalho deve ser recompensado. Nova dose do seu remédio esta aqui.')