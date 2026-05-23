#COPA DO MUNDO: A FASE MAIS FORTE

#INICIO
num_selecoes = int(input()) #*Numero de seleções que serão analisadas
selecoes = {} #*Dicionário que guarda cada seleção e seus dados
pontos_fase = {'fase de grupos':0, 'oitavas':0, 'quartas':0, 'semifinal':0, 'final':0}
times_fase = {'fase de grupos':0, 'oitavas':0, 'quartas':0, 'semifinal':0, 'final':0}
medias = {}

##Fase coleta de dados
for i in range(num_selecoes): #*Para cada seleção
   selecao = {} #*Dicionário que guardará os dados daquela seleção individual
   nome = str(input()) #*Nome da seleção

   fase_pontos = ''
   while fase_pontos != '*': #*Receber dados indefinidamente, até receber *
       fase_pontos = str(input())#* Recebe o nome da fase e sua pontuação no formato "nome da fase pontuação"
       if fase_pontos != '*':
           
           fase_atual = ''
           for string in fase_pontos.split()[0:-1]:
                if string == fase_pontos.split()[-2]:
                    fase_atual += string  
                else:
                    fase_atual += string + ' '

           pontos = int(fase_pontos.split()[-1])
           selecao[fase_atual] = int(pontos) #*Adiciona a fase e os pontos


   selecoes[nome] = selecao #*Joga os dados conseguidos no dicionário principal

##Fase de descobrir a média
for valor_chave in selecoes:
    valores = selecoes[valor_chave]
    for key_fase in valores:
        if key_fase == "fase de grupos":
            times_fase['fase de grupos'] += 1
            pontos_fase['fase de grupos'] += valores['fase de grupos']

        elif key_fase == "oitavas":
            times_fase['oitavas'] += 1
            pontos_fase['oitavas'] += valores['oitavas']
        
        elif key_fase == "quartas":
            times_fase['quartas'] += 1
            pontos_fase['quartas'] += valores['quartas']

        elif key_fase == "semifinal":
            times_fase['semifinal'] += 1
            pontos_fase['semifinal'] += valores['semifinal']
        
        elif key_fase == "final":
            times_fase['final'] += 1
            pontos_fase['final'] += valores['final']
        
for key in times_fase:
    if times_fase[key] > 1:
        medias[key] = pontos_fase[key] / times_fase[key]

#Fase da comparação
maior = 0
fase_maior = ''
for chave in medias:
    valor = medias[chave]
    if valor > maior:
        fase_maior = chave
        maior = valor

print(fase_maior)

for fase in times_fase:
    if times_fase[fase] > 0:
        print()
        print(fase)
        for time in selecoes:
            if fase in selecoes[time]:
                print(f"{time} - {selecoes[time][fase]}")
