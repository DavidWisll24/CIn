"""

totalpendrives=int(input())
senhaoriginal=""
chutedocara=""
memoriazinha=""
tentivas=0
contadorzinho2=0
contadorzinho=0
x=True

print("Avenida Brasil: A Vingança de Nina!")

for numeropendrive in range(1,totalpendrives+1):
    
    print(f"Descriptografando pendrive {numeropendrive} de {totalpendrives}...")
    senhaoriginal=input()
    
    
    ####abaixo escondendo a exibicao
    for letra in senhaoriginal:
        if letra != " ":
            contadorzinho+=1
    
    exibicaosenha=""
    tentivas=contadorzinho*2
    contadorzinho=0
    x=True
    memoriazinha=""
    
    while x:
        chutedocara=input()
        tentivas-=1
        exibicaosenha=""
        ###abaixo criando uma var para guardar os chutes
        if chutedocara in memoriazinha:
            print("Max: Ele já tentou isso, Carminha...")
        else:
            memoriazinha+=chutedocara
            if chutedocara in senhaoriginal:
                print("Nina: Boa, Tufão! Menos uma mentira da Carminha.")
            else:
                print("Carminha: Você é um idiota, Tufão! Isso não faz sentido.")

        ###Descobrindo o que foi coberto
        for letraoriginal in senhaoriginal:
            if letraoriginal == " ":
                exibicaosenha+=" "
            
            elif letraoriginal in memoriazinha:
                exibicaosenha+=letraoriginal
            else:
                exibicaosenha+="_"
        
        print(f"Senha: {exibicaosenha}")
          
        if "_" not in exibicaosenha:          
            print(f"Tufão: Agora eu sei de toda a verdade! O pendrive {numeropendrive} está aberto.")
            x=False
            contadorzinho2+=1
        elif tentivas<=0:
            print(f"Carminha: Consegui! As fotos do pendrive {numeropendrive} estão a salvo comigo.")
            x=False

porcentagem = (contadorzinho2 / totalpendrives) * 100
print(f"Conseguimos abrir {contadorzinho2} de {totalpendrives} pendrives!")

if porcentagem == 0:
    print("Tufão continuará sendo enganado para sempre...")
elif porcentagem <= 50:
    print("Tufão descobriu algumas coisas, mas Carminha ainda tem poder.")
elif porcentagem < 100:
    print("A casa caiu para a Carminha! Quase todas as provas foram recuperadas.")
else:
    print("Justiça por Rita! Todas as provas estão nas mãos de Tufão.")



print('Radar de Fofocas de Copacabana iniciado!')
qtd_rodadas = int(input())

for n in range(1, qtd_rodadas + 1, 1):
  todas_fofocas = '-'
  pontuação = 15
  jogo_ativo = True
  qtd_fofocas = int(input())
  print(f'Rodada {n}/{qtd_rodadas}')
  print(f'Fofocas registradas: {qtd_fofocas}')
  print(f'Pontuação inicial: {pontuação}')

  for x in range(qtd_fofocas):
    fofoca = input()
    todas_fofocas += fofoca + '-'

  todas_fofocas = todas_fofocas.replace(" ", "-")
 
  palavra_proibida = input()
  palavra_proibida = palavra_proibida.replace(" ", "-")
  banco_de_tentativas = '-'
  
  tentativa = input()
  tentativa_original = tentativa
  tentativa = tentativa.replace(" ", "-")
  while jogo_ativo == True:
    if pontuação > 0:
      
      if tentativa != 'fim':
        if not(('-' + tentativa + '-') in banco_de_tentativas):
          if tentativa == palavra_proibida:
            #desconte pontos
            print(f'Armadilha da Sueli! \'{tentativa_original}\' era proibida! -5 pontos')
            pontuação += -5
          else:
            if ('-' + tentativa + '-') in todas_fofocas:
              ocorrencias = todas_fofocas.count('-' + tentativa + '-')
              pontuação += ocorrencias*2
              print(f'Investigação bem sucedida! \'{tentativa_original}\' apareceu {ocorrencias} vez(es).')
            else:
              #tire pontos
              print(f'Nada encontrado sobre \'{tentativa_original}\'. -1 ponto')
              pontuação += -1
          print(f'Pontuação atual: {pontuação}')
          banco_de_tentativas += tentativa + '-'
        else:
          #Você já tentou essa palavra anteriormente.
          print(f'Você já investigou \'{tentativa_original}\'. Tente outra.')
        tentativa = input()
        tentativa_original = tentativa
        tentativa = tentativa.replace(" ", "-")
      else:
        #Isso encerra o código por digitação de "fim"
        print(f'Rodada encerrada! Pontuação final: {pontuação}')
        jogo_ativo = False
    else:
      #Isso encerra o código por pontuação igual ou menor do que zero.
      print('Você ficou sem pontos! Sueli venceu essa rodada')
      jogo_ativo = False


x=True
tentativa=""
contador=0
numerofofocas=0
rodadastotais=0

print("Radar de Fofocas de Copacabana iniciado!")

rodadastotais=int(input())

for rodadaatual in range(1,rodadastotais+1):
    
    x=True
    pontuacao=15
    memoriazinha=""
    textodasfofoca=""

    numerofofocas=int(input())
    print(f"Rodada {rodadaatual}/{rodadastotais}")
    print(f"Fofocas registradas: {numerofofocas}")
    print(f"Pontuação inicial: 15")



    for numero in range(numerofofocas):
        fofoca=input()
        textodasfofoca+=fofoca+" "
    
    proibida=input()

    while pontuacao>0 and x:
        
        tentativa=input()
        
        if tentativa == "fim":
            print(f"Rodada encerrada! Pontuação final: {pontuacao}")
            x=False
        
        else:
            
            if (" "+tentativa+" ") in (" " + memoriazinha+ " "): 
                print(f"Você já investigou '{tentativa}'. Tente outra.")
            
            else:

                memoriazinha+=tentativa + " "

                if tentativa == proibida:
                    pontuacao-=5
                    print(f"Armadilha da Sueli! '{tentativa}' era proibida! -5 pontos")

                else:
                    
                    contador=0
                    palavrinha=""

                    for letra in textodasfofoca:
                        if letra != " ":
                            palavrinha+=letra
                        else:
                            if palavrinha == tentativa:
                                contador+=1
                            palavrinha= ""

                    if contador >0:
                        print(f"Investigação bem sucedida! '{tentativa}' apareceu {contador} vez(es).")
                        pontuacao+=(2*contador)
                    else:
                        pontuacao-=1
                        print(f"Nada encontrado sobre '{tentativa}'. -1 ponto")

                if pontuacao <=0:
                    print(f"Pontuação atual: {pontuacao}")
                    x=False
                    print(f"Você ficou sem pontos! Sueli venceu essa rodada")
                    
                else:
                    print(f"Pontuação atual: {pontuacao}")


print("Radar de Fofocas de Copacabana iniciado!")

rodadas = int(input())
rodada_atual = 1

while rodada_atual <= rodadas:

    pontos = 15
    controle = -1
    registros = ""
    usados = ""
    qtd_fofocas = int(input())

    print(f"Rodada {rodada_atual}/{rodadas}")
    print(f"Fofocas registradas: {qtd_fofocas}")
    print(f"Pontuação inicial: 15")

    contador = 0
    while contador < qtd_fofocas:
        f = input()
        registros += f + " "
        contador += 1

    proibida = input()

    while (controle != 0) and (pontos > 0):

        tentativa = input()

        if tentativa == "fim":
            print(f"Rodada encerrada! Pontuação final: {pontos}")
            controle = 0

        else:
            if (" " + tentativa + " ") in (" " + usados + " "):
                print(f"Você já investigou '{tentativa}'. Tente outra.")

            else:
                usados += tentativa + " "

                if tentativa == proibida:
                    pontos -= 5
                    print(f"Armadilha da Sueli! '{tentativa}' era proibida! -5 pontos")

                else:
                    contagem = 0
                    palavra = ""
                    i = 0

                    while i < len(registros):
                        if registros[i] != " ":
                            palavra += registros[i]
                        else:
                            if palavra == tentativa:
                                contagem += 1
                            palavra = ""
                        i += 1

                    if contagem > 0:
                        pontos += 2 * contagem
                        print(f"Investigação bem sucedida! '{tentativa}' apareceu {contagem} vez(es).")
                    else:
                        pontos -= 1
                        print(f"Nada encontrado sobre '{tentativa}'. -1 ponto")

                if pontos <= 0:
                    print(f"Pontuação atual: {pontos}")
                    print("Você ficou sem pontos! Sueli venceu essa rodada")
                    controle = 0
                else:
                    print(f"Pontuação atual: {pontos}")

    rodada_atual += 1
"""

print("Radar de Fofocas de Copacabana iniciado!")

numero_rodadas = int(input())

# ======================================= rodadas
for rodada_atual in range(numero_rodadas):
  pontos = 15
  numero_fofocas = int(input())

  print(f"Rodada {rodada_atual + 1}/{numero_rodadas}")
  print(f"Fofocas registradas: {numero_fofocas}")
  print("Pontuação inicial: 15")

  # ======================================= fofocas
  fofocas = ""
  for _ in range(numero_fofocas):  # coleta as fofocas e separa com *
    fofocas += input() + " "

  palavra_proibida = input()

  keywords_usadas = ""
  anotando = pontos > 0
  while anotando:
    keyword = input()  # palavra que vai ser procurada
    num_keywords_achados = 0
    proibicao_aplicada = False
    keyword_repetida = False
    # ======================================= separação das fofocas

    if keyword.lower() == "fim":  # comando para encerrar a rodada
      anotando = False
      print(f"Rodada encerrada! Pontuação final: {pontos}")
    else:
      palavra_em_analise = ""  # palavra da fofoca a ser comparada com a keyword

      for letra_fofoca in fofocas:
        if letra_fofoca != " ":  # ao esbarrar com o primeiro separador, o toggle é ativado
          palavra_em_analise += letra_fofoca
        else:  # se o toggle tiver sido ativado, a letra é adicionada à nova lista de fofocas_a_analisar
          if "_" + keyword + "_" in keywords_usadas:  # se a keyword já tiver sido usada, ela não é analisada
            if not keyword_repetida:  # se o aviso não foi dado antes, ele é dado agora
              print(f"Você já investigou '{keyword}'. Tente outra.")
              keyword_repetida = True

          else:
            if palavra_proibida == keyword and not proibicao_aplicada:
              pontos -= 5
              proibicao_aplicada = True  # a penalidade só é aplicada uma vez por rodada
              print(f"Armadilha da Sueli! '{keyword}' era proibida! -5 pontos")
            elif keyword in fofocas:
              if keyword == palavra_em_analise:
                pontos += 2
                num_keywords_achados += 1
          palavra_em_analise = ""  # palavra em análise é resetada
          anotando = pontos > 0  # atualização do toggle

      if num_keywords_achados > 0:
        print(f"Investigação bem sucedida! '{keyword}' apareceu {num_keywords_achados} vez(es).")
      elif (
        not keyword_repetida
      ):  # se a keyword não for a proibida, não tiver sido repetida, e não tiver sido encontrada, a pontuação é reduzida
        pontos -= 1
        print(f"Nada encontrado sobre '{keyword}'. -1 ponto")

      print(f"Pontuação atual: {pontos}")

      if pontos <= 0:
        print("Você ficou sem pontos! Sueli venceu essa rodada")
        anotando = False
    keywords_usadas += "_" + keyword + "_*"