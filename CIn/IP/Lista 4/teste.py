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

b = [1, 2, 3, 4]

b.insert(2, b.pop(3))

print(b)
"""

m1 = [
    [3, 4, 5],
    [1, 1, 2],
    [2, 2, 1]
]

m2 = [
    [1, 1, 3],
    [3, 1, 1],
    [2, 1, 2]
]
mr = []
#m_resultante = [
#    [m1[0]['0']*"m2[0][0]" + m1[0]['1']*"m2[1][0]" + m1[0]['2']*"m2[2][0]" , m1[0]['0']*"m2[0][1]" + m1[0]['1']*"m2[1][1]" + m1[0]['2']*"m2[2][1]" , m1[0]['0']*"m2[0][2]" + m1[0]['1']*"m2[1][2]" + m1[0]['2']*"m2[2][2]"]
#    '[m1[1]['0']*"m2[0][0]" + m1[1]['1']*"m2[1][0]" + m1[1]['2']*"m2[2][0]" , m1[1]['0']*"m2[0][1]" + m1[1]['1']*"m2[1][1]" + m1[1]['2']*"m2[2][1]" , m1[1]['0']*"m2[0][2]" + m1[1]['1']*"m2[1][2]" + m1[1]['2']*"m2[2][2]"]'
#    '[m1[2]['0']*"m2[0][0]" + m1[2]['1']*"m2[1][0]" + m1[2]['2']*"m2[2][0]" , m1[2]['0']*"m2[0][1]" + m1[2]['1']*"m2[1][1]" + m1[2]['2']*"m2[2][1]" , m1[2]['0']*"m2[0][2]" + m1[2]['1']*"m2[1][2]" + m1[2]['2']*"m2[2][2]"]'

"""
Para cada elemento eu tenho uma linha inteira percorrendo uma coluna inteira 
e essa mesma linha percorre x colunas até completar a primeira linha da matriz resultante

FOCO: Estrutura que não se repete
"""

for i in range(3):
    lm = []
    for j in range(3):
        e = m1[i][0]*m2[0][j] + m1[i][1]*m2[1][j] + m1[i][2]*m2[2][j]
        lm.append(e)
    mr.append(lm)
    
for b in mr:
    print(b)