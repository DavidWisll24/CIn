#Definições iniciais
maquina_1 = input("")
quantidade_pecas_1 = int(input())
reacao_candace_1 = input()

maquina_2 = input("")
quantidade_pecas_2 = int(input())
reacao_candace_2 = input()

maquina_3 = input("")
quantidade_pecas_3 = int(input())
reacao_candace_3 = input()

maquina_4 = input("")
quantidade_pecas_4 = int(input())
reacao_candace_4 = input()

max_nome = 15
max_peça = 25

pontos_finais_1 = len(maquina_1) + quantidade_pecas_1
pontos_finais_2 = len(maquina_2) + quantidade_pecas_2
pontos_finais_3 = len(maquina_3) + quantidade_pecas_3
pontos_finais_4 = len(maquina_4) + quantidade_pecas_4

#Condições da máquina_1
if (
  "i" in maquina_1.lower()
  and "n" in maquina_1.lower()
  and "a" in maquina_1.lower()
  and "t" in maquina_1.lower()
  and "o" in maquina_1.lower()
  and "r" in maquina_1.lower()
):
  pontos_finais_1 = pontos_finais_1 - 50
  
if (
  "p" in maquina_1.lower()
  and "e" in maquina_1.lower()
  and "r" in maquina_1.lower()
  and "y" in maquina_1.lower()
):
  pontos_finais_1 = pontos_finais_1 + 20
  
if reacao_candace_1 == "MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!":
  pontos_finais_1 = pontos_finais_1 + 30
elif reacao_candace_1 == "EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!":
  pontos_finais_1 = pontos_finais_1 + 20
elif reacao_candace_1 == "OK... ISSO É BEM ESTRANHO.":
  pontos_finais_1 = pontos_finais_1 + 10
elif reacao_candace_1 == "AH, NEM É TÃO IMPRESSIONANTE ASSIM.":
  pontos_finais_1 = pontos_finais_1 + 0
elif reacao_candace_1 == "SÉRIO? SÓ ISSO?":
  pontos_finais_1 = pontos_finais_1 - 5
elif reacao_candace_1 == "MÃE! A MÁQUINA SUMIU DE NOVO!":
  pontos_finais_1 = pontos_finais_1 - 10
elif reacao_candace_1 == "AH, ESQUECE…":
  pontos_finais_1 = pontos_finais_1 - 15
  
if maquina_1 == "HidromassagemAutomáticaDoPerry":
  pontos_finais_1 = pontos_finais_1 * 2
elif maquina_1 == "MáquinaDeBanhoForçado":
  pontos_finais_1 = pontos_finais_1 - 20
  
#Condições máquina_2
if (
  "i" in maquina_2.lower()
  and "n" in maquina_2.lower()
  and "a" in maquina_2.lower()
  and "t" in maquina_2.lower()
  and "o" in maquina_2.lower()
  and "r" in maquina_2.lower()
):
  pontos_finais_2 = pontos_finais_2 - 50
  
if (
  "p" in maquina_2.lower()
  and "e" in maquina_2.lower()
  and "rr" in maquina_2.lower()
  and "y" in maquina_2.lower()
):
  pontos_finais_2 = pontos_finais_2 + 20
  
if reacao_candace_2 == "MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!":
  pontos_finais_2 = pontos_finais_2 + 30
elif reacao_candace_2 == "EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!":
  pontos_finais_2 = pontos_finais_2 + 20
elif reacao_candace_2 == "OK... ISSO É BEM ESTRANHO.":
  pontos_finais_2 = pontos_finais_2 + 10
elif reacao_candace_2 == "AH, NEM É TÃO IMPRESSIONANTE ASSIM.":
  pontos_finais_2 = pontos_finais_2 + 0
elif reacao_candace_2 == "SÉRIO? SÓ ISSO?":
  pontos_finais_2 = pontos_finais_2 - 5
elif reacao_candace_2 == "MÃE! A MÁQUINA SUMIU DE NOVO!":
  pontos_finais_2 = pontos_finais_2 - 10
elif reacao_candace_2 == "AH, ESQUECE…":
  pontos_finais_2 = pontos_finais_2 - 15

if maquina_2 == "HidromassagemAutomáticaDoPerry":
  pontos_finais_2 = pontos_finais_2 * 2
elif maquina_2 == "MáquinaDeBanhoForçado":
  pontos_finais_2 = pontos_finais_2 - 20

#Condições máquina_3  
if (
  "i" in maquina_3.lower()
  and "n" in maquina_3.lower()
  and "a" in maquina_3.lower()
  and "t" in maquina_3.lower()
  and "o" in maquina_3.lower()
  and "r" in maquina_3.lower()
):
  pontos_finais_3 = pontos_finais_3 - 50
  
if (
  "p" in maquina_3.lower()
  and "e" in maquina_3.lower()
  and "rr" in maquina_3.lower()
  and "y" in maquina_3.lower()
):
  pontos_finais_3 = pontos_finais_3 + 20
  
if reacao_candace_3 == "MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!":
  pontos_finais_3 = pontos_finais_3 + 30
elif reacao_candace_3 == "EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!":
  pontos_finais_3 = pontos_finais_3 + 20
elif reacao_candace_3 == "OK... ISSO É BEM ESTRANHO.":
  pontos_finais_3 = pontos_finais_3 + 10
elif reacao_candace_3 == "AH, NEM É TÃO IMPRESSIONANTE ASSIM.":
  pontos_finais_3 = pontos_finais_3 + 0
elif reacao_candace_3 == "SÉRIO? SÓ ISSO?":
  pontos_finais_3 = pontos_finais_3 - 5
elif reacao_candace_3 == "MÃE! A MÁQUINA SUMIU DE NOVO!":
  pontos_finais_3 = pontos_finais_3 - 10
elif reacao_candace_3 == "AH, ESQUECE…":
  pontos_finais_3 = pontos_finais_3 - 15
  
if maquina_3 == "HidromassagemAutomáticaDoPerry":
  pontos_finais_3 = pontos_finais_3 * 2
elif maquina_3 == "MáquinaDeBanhoForçado":
  pontos_finais_3 = pontos_finais_3 - 20

#Condições máquina_4  
if (
  "i" in maquina_4.lower()
  and "n" in maquina_4.lower()
  and "a" in maquina_4.lower()
  and "t" in maquina_4.lower()
  and "o" in maquina_4.lower()
  and "r" in maquina_4.lower()
):
  pontos_finais_4 = pontos_finais_4 - 50
  
if (
  "p" in maquina_4.lower()
  and "e" in maquina_4.lower()
  and "rr" in maquina_4.lower()
  and "y" in maquina_4.lower()
):
  pontos_finais_4 = pontos_finais_4 + 20
  
if reacao_candace_4 == "MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!":
  pontos_finais_4 = pontos_finais_4 + 30
elif reacao_candace_4 == "EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!":
  pontos_finais_4 = pontos_finais_4 + 20
elif reacao_candace_4 == "OK... ISSO É BEM ESTRANHO.":
  pontos_finais_4 = pontos_finais_4 + 10
elif reacao_candace_4 == "AH, NEM É TÃO IMPRESSIONANTE ASSIM.":
  pontos_finais_4 = pontos_finais_4 + 0
elif reacao_candace_4 == "SÉRIO? SÓ ISSO?":
  pontos_finais_4 = pontos_finais_4 - 5
elif reacao_candace_4 == "MÃE! A MÁQUINA SUMIU DE NOVO!":
  pontos_finais_4 = pontos_finais_4 - 10
elif reacao_candace_4 == "AH, ESQUECE…":
  pontos_finais_4 = pontos_finais_4 - 15
  
if maquina_4 == "HidromassagemAutomáticaDoPerry":
  pontos_finais_4 = pontos_finais_4 * 2
elif maquina_4 == "MáquinaDeBanhoForçado":
  pontos_finais_4 = pontos_finais_4 - 20

#Comparação de Igualdade
if (
  pontos_finais_1 == pontos_finais_2
  or pontos_finais_1 == pontos_finais_3
  or pontos_finais_1 == pontos_finais_4
  or pontos_finais_2 == pontos_finais_3
  or pontos_finais_2 == pontos_finais_4
  or pontos_finais_3 == pontos_finais_4
):
  parametro_1 = 0
  parametro_2 = 0
  parametro_3 = 0
  parametro_4 = 0
  parametro_5 = 0
  parametro_6 = 0
  
  
  if pontos_finais_1 == pontos_finais_2:
    if len(maquina_1) > max_nome:
      parametro_1 = 1
    if quantidade_pecas_1 > max_peça:
      parametro_1 = parametro_1 + 1
    if len(maquina_2) > max_nome:
      parametro_2 = 1
    if quantidade_pecas_2 > max_peça:
      parametro_2 = parametro_2 + 1
      
    if parametro_1 > parametro_2:
      maio_entre = maquina_1
      maio_pont_entre = pontos_finais_1
      menor_entre = maquina_2
      menor_pont_entre = pontos_finais_2
    elif parametro_2 > parametro_1:
      maio_entre = maquina_2
      maio_pont_entre = pontos_finais_2
      menor_entre = maquina_1
      menor_pont_entre = pontos_finais_1
    elif parametro_1 == parametro_2:
      if quantidade_pecas_1 > quantidade_pecas_2:
        maio_entre = maquina_1
        maio_pont_entre = pontos_finais_1
        menor_entre = maquina_2
        menor_pont_entre = pontos_finais_2
      elif quantidade_pecas_1 < quantidade_pecas_2:
        maio_entre = maquina_2
        maio_pont_entre = pontos_finais_2
        menor_entre = maquina_1
        menor_pont_entre = pontos_finais_1
      elif quantidade_pecas_1 == quantidade_pecas_2:
        if len(maquina_1) > len(maquina_2):
          maio_entre = maquina_1
          maio_pont_entre = pontos_finais_1
          menor_entre = maquina_2
          menor_pont_entre = pontos_finais_2
        elif len(maquina_1) < len(maquina_2):
          maio_entre = maquina_2
          maio_pont_entre = pontos_finais_2
          menor_entre = maquina_1
          menor_pont_entre = pontos_finais_1
    
  elif pontos_finais_1 == pontos_finais_3:
    if len(maquina_1) > max_nome:
      parametro_1 = 1
    if quantidade_pecas_1 > max_peça:
      parametro_1 = parametro_1 + 1
    if len(maquina_3) > max_nome:
      parametro_2 = 1
    if quantidade_pecas_3 > max_peça:
      parametro_2 = parametro_2 + 1
      
    if parametro_1 > parametro_2:
      maio_entre = maquina_1
      maio_pont_entre = pontos_finais_1
      menor_entre = maquina_3
      menor_pont_entre = pontos_finais_3
    elif parametro_2 > parametro_1:
      maio_entre = maquina_3
      maio_pont_entre = pontos_finais_3
      menor_entre = maquina_1
      menor_pont_entre = pontos_finais_1
    elif parametro_1 == parametro_2:
      if quantidade_pecas_1 > quantidade_pecas_3:
        maio_entre = maquina_1
        maio_pont_entre = pontos_finais_1
        menor_entre = maquina_3
        menor_pont_entre = pontos_finais_3
      elif quantidade_pecas_1 < quantidade_pecas_3:
        maio_entre = maquina_3
        maio_pont_entre = pontos_finais_3
        menor_entre = maquina_1
        menor_pont_entre = pontos_finais_1
      elif quantidade_pecas_1 == quantidade_pecas_3:
        if len(maquina_1) > len(maquina_3):
          maio_entre = maquina_1
          maio_pont_entre = pontos_finais_1
          menor_entre = maquina_3
          menor_pont_entre = pontos_finais_3
        elif len(maquina_1) < len(maquina_3):
          maio_entre = maquina_3
          maio_pont_entre = pontos_finais_3
          menor_entre = maquina_1
          menor_pont_entre = pontos_finais_1
          
  elif pontos_finais_1 == pontos_finais_4:
    if len(maquina_1) > max_nome:
      parametro_1 = 1
    if quantidade_pecas_1 > max_peça:
      parametro_1 = parametro_1 + 1
    if len(maquina_4) > max_nome:
      parametro_2 = 1
    if quantidade_pecas_4 > max_peça:
      parametro_2 = parametro_2 + 1
      
    if parametro_1 > parametro_2:
      maio_entre = maquina_1
      maio_pont_entre = pontos_finais_1
      menor_entre = maquina_4
      menor_pont_entre = pontos_finais_4
    elif parametro_2 > parametro_1:
      maio_entre = maquina_4
      maio_pont_entre = pontos_finais_4
      menor_entre = maquina_1
      menor_pont_entre = pontos_finais_1
    elif parametro_1 == parametro_2:
      if quantidade_pecas_1 > quantidade_pecas_4:
        maio_entre = maquina_1
        maio_pont_entre = pontos_finais_1
        menor_entre = maquina_4
        menor_pont_entre = pontos_finais_4
      elif quantidade_pecas_1 < quantidade_pecas_4:
        maio_entre = maquina_4
        maio_pont_entre = pontos_finais_4
        menor_entre = maquina_1
        menor_pont_entre = pontos_finais_1
      elif quantidade_pecas_1 == quantidade_pecas_4:
        if len(maquina_1) > len(maquina_4):
          maio_entre = maquina_1
          maio_pont_entre = pontos_finais_1
          menor_entre = maquina_4
          menor_pont_entre = pontos_finais_4
        elif len(maquina_1) < len(maquina_4):
          maio_entre = maquina_4
          maio_pont_entre = pontos_finais_4
          menor_entre = maquina_1
          menor_pont_entre = pontos_finais_1
          
  if pontos_finais_2 == pontos_finais_3:
    if len(maquina_2) > max_nome:
      parametro_3 = 1
    if quantidade_pecas_2 > max_peça:
      parametro_3 = parametro_3 + 1
    if len(maquina_3) > max_nome:
      parametro_4 = 1
    if quantidade_pecas_3 > max_peça:
      parametro_4 = parametro_4 + 1
      
    if parametro_3 > parametro_4:
      maio_entre2 = maquina_2
      maio_pont_entre2 = pontos_finais_2
      menor_entre2 = maquina_3
      menor_pont_entre2 = pontos_finais_3
    elif parametro_4 > parametro_3:
      maio_entre2 = maquina_3
      maio_pont_entre2 = pontos_finais_3
      menor_entre2 = maquina_2
      menor_pont_entre2 = pontos_finais_2
    elif parametro_3 == parametro_4:
      if quantidade_pecas_2 > quantidade_pecas_3:
        maio_entre2 = maquina_2
        maio_pont_entre2 = pontos_finais_2
        menor_entre2 = maquina_3
        menor_pont_entre2 = pontos_finais_3
      elif quantidade_pecas_2 < quantidade_pecas_3:
        maio_entre2 = maquina_3
        maio_pont_entre2 = pontos_finais_3
        menor_entre2 = maquina_2
        menor_pont_entre2 = pontos_finais_2
      elif quantidade_pecas_2 == quantidade_pecas_3:
        if len(maquina_2) > len(maquina_3):
          maio_entre2 = maquina_2
          maio_pont_entre2 = pontos_finais_2
          menor_entre2 = maquina_3
          menor_pont_entre2 = pontos_finais_3
        elif len(maquina_2) < len(maquina_3):
          maio_entre2 = maquina_3
          maio_pont_entre2 = pontos_finais_3
          menor_entre2 = maquina_2
          menor_pont_entre2 = pontos_finais_2
          
  elif pontos_finais_2 == pontos_finais_4:
    if len(maquina_2) > max_nome:
      parametro_3 = 1
    if quantidade_pecas_2 > max_peça:
      parametro_3 = parametro_3 + 1
    if len(maquina_4) > max_nome:
      parametro_4 = 1
    if quantidade_pecas_4 > max_peça:
      parametro_4 = parametro_4 + 1
      
    if parametro_3 > parametro_4:
      maio_entre2 = maquina_2
      maio_pont_entre2 = pontos_finais_2
      menor_entre2 = maquina_4
      menor_pont_entre2 = pontos_finais_4
    elif parametro_4 > parametro_3:
      maio_entre2 = maquina_4
      maio_pont_entre2 = pontos_finais_4
      menor_entre2 = maquina_2
      menor_pont_entre2 = pontos_finais_2
    elif parametro_3 == parametro_4:
      if quantidade_pecas_2 > quantidade_pecas_4:
        maio_entre2 = maquina_2
        maio_pont_entre2 = pontos_finais_2
        menor_entre2 = maquina_4
        menor_pont_entre2 = pontos_finais_4
      elif quantidade_pecas_2 < quantidade_pecas_4:
        maio_entre2 = maquina_4
        maio_pont_entre2 = pontos_finais_4
        menor_entre2 = maquina_2
        menor_pont_entre2 = pontos_finais_2
      elif quantidade_pecas_2 == quantidade_pecas_4:
        if len(maquina_2) > len(maquina_4):
          maio_entre2 = maquina_2
          maio_pont_entre2 = pontos_finais_2
          menor_entre2 = maquina_4
          menor_pont_entre2 = pontos_finais_4
        elif len(maquina_2) < len(maquina_4):
          maio_entre2 = maquina_4
          maio_pont_entre2 = pontos_finais_4
          menor_entre2 = maquina_2
          menor_pont_entre2 = pontos_finais_2
          
  elif pontos_finais_3 == pontos_finais_4:
    if len(maquina_3) > max_nome:
      parametro_5 = 1
    if quantidade_pecas_3 > max_peça:
      parametro_5 = parametro_5 + 1
    if len(maquina_4) > max_nome:
      parametro_6 = 1
    if quantidade_pecas_4 > max_peça:
      parametro_6 = parametro_6 + 1
      
    if parametro_5 > parametro_6:
      maio_entre3 = maquina_3
      maio_pont_entre3 = pontos_finais_3
      menor_entre3 = maquina_4
      menor_pont_entre3 = pontos_finais_4
    elif parametro_6 > parametro_5:
      maio_entre3 = maquina_4
      maio_pont_entre3 = pontos_finais_4
      menor_entre3 = maquina_3
      menor_pont_entre3 = pontos_finais_3
    elif parametro_5 == parametro_6:
      if quantidade_pecas_3 > quantidade_pecas_4:
        maio_entr3 = maquina_3
        maio_pont_entre3 = pontos_finais_3
        menor_entre3 = maquina_4
        menor_pont_entre3 = pontos_finais_4
      elif quantidade_pecas_3 < quantidade_pecas_4:
        maio_entre3 = maquina_4
        maio_pont_entre3 = pontos_finais_4
        menor_entre3 = maquina_3
        menor_pont_entre3 = pontos_finais_3
      elif quantidade_pecas_3 == quantidade_pecas_4:
        if len(maquina_3) > len(maquina_4):
          maio_entre3 = maquina_3
          maio_pont_entre3 = pontos_finais_3
          menor_entre3 = maquina_4
          menor_pont_entre3 = pontos_finais_4
        elif len(maquina_3) < len(maquina_4):
          maio_entre3 = maquina_4
          maio_pont_entre3 = pontos_finais_4
          menor_entre3 = maquina_3
          menor_pont_entre3 = pontos_finais_3

#Caso dos 3 == 4
  if pontos_finais_3 == pontos_finais_4:
    if pontos_finais_1 > pontos_finais_2 > maio_pont_entre3 == menor_pont_entre3:
      print(f"1º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"2º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"3º lugar - {maio_entre3} : {maio_pont_entre3} pontos")
      print(f"4º lugar - {menor_entre3} : {menor_pont_entre3} pontos")
    elif pontos_finais_1 > maio_pont_entre3 == menor_pont_entre3 > pontos_finais_2:
      print(f"1º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"2º lugar - {maio_entre3} : {maio_pont_entre3} pontos")
      print(f"3º lugar - {menor_entre3} : {menor_pont_entre3} pontos")
      print(f"4º lugar - {maquina_2} : {pontos_finais_2} pontos")
    elif maio_pont_entre3 == menor_pont_entre3 > pontos_finais_1 > pontos_finais_2:
      print(f"1º lugar - {maio_entre3} : {maio_pont_entre3} pontos")
      print(f"2º lugar - {menor_entre3} : {menor_pont_entre3} pontos")
      print(f"3º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"4º lugar - {maquina_2} : {pontos_finais_2} pontos")
    elif pontos_finais_2 > pontos_finais_1 > maio_pont_entre3 == menor_pont_entre3:
      print(f"1º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"2º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"3º lugar - {maio_entre3} : {maio_pont_entre3} pontos")
      print(f"4º lugar - {menor_entre3} : {menor_pont_entre3} pontos")
    elif pontos_finais_2 > maio_pont_entre3 == menor_pont_entre3 > pontos_finais_1:
      print(f"1º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"2º lugar - {maio_entre3} : {maio_pont_entre3} pontos")
      print(f"3º lugar - {menor_entre3} : {menor_pont_entre3} pontos")
      print(f"4º lugar - {maquina_1} : {pontos_finais_1} pontos")
    elif maio_pont_entre3 == menor_pont_entre3 > pontos_finais_2 > pontos_finais_1:
      print(f"1º lugar - {maio_entre3} : {maio_pont_entre3} pontos")
      print(f"2º lugar - {menor_entre3} : {menor_pont_entre3} pontos")
      print(f"3º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"4º lugar - {maquina_1} : {pontos_finais_1} pontos")

#Casos 2 == 3, 2 == 4
  if (
    pontos_finais_2 == pontos_finais_4
    or pontos_finais_2 == pontos_finais_3
  ):
    if pontos_finais_1 > pontos_finais_3 > maio_pont_entre2 == menor_pont_entre2:
      print(f"1º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"2º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"3º lugar - {maio_entre2} : {maio_pont_entre2} pontos")
      print(f"4º lugar - {menor_entre2} : {menor_pont_entre2} pontos")
    elif pontos_finais_1 > maio_pont_entre2 == menor_pont_entre2 > pontos_finais_3:
      print(f"1º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"2º lugar - {maio_entre2} : {maio_pont_entre2} pontos")
      print(f"3º lugar - {menor_entre2} : {menor_pont_entre2} pontos")
      print(f"4º lugar - {maquina_3} : {pontos_finais_3} pontos")
    elif maio_pont_entre2 == menor_pont_entre2 > pontos_finais_1 > pontos_finais_3:
      print(f"1º lugar - {maio_entre2} : {maio_pont_entre2} pontos")
      print(f"2º lugar - {menor_entre2} : {menor_pont_entre2} pontos")
      print(f"3º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"4º lugar - {maquina_3} : {pontos_finais_3} pontos")
    elif pontos_finais_3 > pontos_finais_1 > maio_pont_entre2 == menor_pont_entre2:
      print(f"1º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"2º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"3º lugar - {maio_entre2} : {maio_pont_entre2} pontos")
      print(f"4º lugar - {menor_entre2} : {menor_pont_entre2} pontos")
    elif pontos_finais_3 > maio_pont_entre2 == menor_pont_entre2 > pontos_finais_1:
      print(f"1º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"2º lugar - {maio_entre2} : {maio_pont_entre2} pontos")
      print(f"3º lugar - {menor_entre2} : {menor_pont_entre2} pontos")
      print(f"4º lugar - {maquina_1} : {pontos_finais_1} pontos")
    elif maio_pont_entre2 == menor_pont_entre2 > pontos_finais_3 > pontos_finais_1:
      print(f"1º lugar - {maio_entre2} : {maio_pont_entre2} pontos")
      print(f"2º lugar - {menor_entre2} : {menor_pont_entre2} pontos")
      print(f"3º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"4º lugar - {maquina_1} : {pontos_finais_1} pontos")

    elif pontos_finais_1 > pontos_finais_4 > maio_pont_entre2 == menor_pont_entre2:
      print(f"1º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"2º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"3º lugar - {maio_entre2} : {maio_pont_entre2} pontos")
      print(f"4º lugar - {menor_entre2} : {menor_pont_entre2} pontos")
    elif pontos_finais_1 > maio_pont_entre2 == menor_pont_entre2 > pontos_finais_4:
      print(f"1º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"2º lugar - {maio_entre2} : {maio_pont_entre2} pontos")
      print(f"3º lugar - {menor_entre2} : {menor_pont_entre2} pontos")
      print(f"4º lugar - {maquina_4} : {pontos_finais_4} pontos")
    elif maio_pont_entre2 == menor_pont_entre2 > pontos_finais_1 > pontos_finais_4:
      print(f"1º lugar - {maio_entre2} : {maio_pont_entre2} pontos")
      print(f"2º lugar - {menor_entre2} : {menor_pont_entre2} pontos")
      print(f"3º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"4º lugar - {maquina_4} : {pontos_finais_4} pontos")
    elif pontos_finais_4 > pontos_finais_1 > maio_pont_entre2 == menor_pont_entre2:
      print(f"1º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"2º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"3º lugar - {maio_entre2} : {maio_pont_entre2} pontos")
      print(f"4º lugar - {menor_entre2} : {menor_pont_entre2} pontos")
    elif pontos_finais_4 > maio_pont_entre2 == menor_pont_entre2 > pontos_finais_1:
      print(f"1º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"2º lugar - {maio_entre2} : {maio_pont_entre2} pontos")
      print(f"3º lugar - {menor_entre2} : {menor_pont_entre2} pontos")
      print(f"4º lugar - {maquina_1} : {pontos_finais_1} pontos")
    elif maio_pont_entre2 == menor_pont_entre2 > pontos_finais_4 > pontos_finais_1:
      print(f"1º lugar - {maio_entre2} : {maio_pont_entre2} pontos")
      print(f"2º lugar - {menor_entre2} : {menor_pont_entre2} pontos")
      print(f"3º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"4º lugar - {maquina_1} : {pontos_finais_1} pontos")

#Casos 1 == 2, 1 == 3, 1 == 4
  if(
    pontos_finais_1 == pontos_finais_2
    or pontos_finais_1 == pontos_finais_3
    or pontos_finais_1 == pontos_finais_4
  ):
    if pontos_finais_4 > pontos_finais_2 > maio_pont_entre == menor_pont_entre:
      print(f"1º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"2º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"3º lugar - {maio_entre} : {maio_pont_entre} pontos")
      print(f"4º lugar - {menor_entre} : {menor_pont_entre} pontos")
    elif pontos_finais_4 > maio_pont_entre == menor_pont_entre > pontos_finais_2:
      print(f"1º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"2º lugar - {maio_entre} : {maio_pont_entre} pontos")
      print(f"3º lugar - {menor_entre} : {menor_pont_entre} pontos")
      print(f"4º lugar - {maquina_2} : {pontos_finais_2} pontos")
    elif maio_pont_entre == menor_pont_entre > pontos_finais_4 > pontos_finais_2:
      print(f"1º lugar - {maio_entre} : {maio_pont_entre} pontos")
      print(f"2º lugar - {menor_entre} : {menor_pont_entre} pontos")
      print(f"3º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"4º lugar - {maquina_2} : {pontos_finais_2} pontos")
    elif pontos_finais_2 > pontos_finais_4 > maio_pont_entre == menor_pont_entre:
      print(f"1º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"2º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"3º lugar - {maio_entre} : {maio_pont_entre} pontos")
      print(f"4º lugar - {menor_entre} : {menor_pont_entre} pontos")
    elif pontos_finais_2 > maio_pont_entre == menor_pont_entre > pontos_finais_4:
      print(f"1º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"2º lugar - {maio_entre} : {maio_pont_entre} pontos")
      print(f"3º lugar - {menor_entre} : {menor_pont_entre} pontos")
      print(f"4º lugar - {maquina_4} : {pontos_finais_4} pontos")
    elif maio_pont_entre == menor_pont_entre > pontos_finais_2 > pontos_finais_4:
      print(f"1º lugar - {maio_entre} : {maio_pont_entre} pontos")
      print(f"2º lugar - {menor_entre} : {menor_pont_entre} pontos")
      print(f"3º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"4º lugar - {maquina_4} : {pontos_finais_4} pontos")

    elif pontos_finais_3 > pontos_finais_2 > maio_pont_entre == menor_pont_entre:
      print(f"1º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"2º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"3º lugar - {maio_entre} : {maio_pont_entre} pontos")
      print(f"4º lugar - {menor_entre} : {menor_pont_entre} pontos")
    elif pontos_finais_3 > maio_pont_entre == menor_pont_entre > pontos_finais_2:
      print(f"1º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"2º lugar - {maio_entre} : {maio_pont_entre} pontos")
      print(f"3º lugar - {menor_entre} : {menor_pont_entre} pontos")
      print(f"4º lugar - {maquina_2} : {pontos_finais_2} pontos")
    elif maio_pont_entre == menor_pont_entre > pontos_finais_3 > pontos_finais_2:
      print(f"1º lugar - {maio_entre} : {maio_pont_entre} pontos")
      print(f"2º lugar - {menor_entre} : {menor_pont_entre} pontos")
      print(f"3º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"4º lugar - {maquina_2} : {pontos_finais_2} pontos")
    elif pontos_finais_2 > pontos_finais_3 > maio_pont_entre == menor_pont_entre:
      print(f"1º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"2º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"3º lugar - {maio_entre} : {maio_pont_entre} pontos")
      print(f"4º lugar - {menor_entre} : {menor_pont_entre} pontos")
    elif pontos_finais_2 > maio_pont_entre == menor_pont_entre > pontos_finais_3:
      print(f"1º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"2º lugar - {maio_entre} : {maio_pont_entre} pontos")
      print(f"3º lugar - {menor_entre} : {menor_pont_entre} pontos")
      print(f"4º lugar - {maquina_3} : {pontos_finais_3} pontos")
    elif maio_pont_entre == menor_pont_entre > pontos_finais_2 > pontos_finais_3:
      print(f"1º lugar - {maio_entre} : {maio_pont_entre} pontos")
      print(f"2º lugar - {menor_entre} : {menor_pont_entre} pontos")
      print(f"3º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"4º lugar - {maquina_3} : {pontos_finais_3} pontos")

    elif pontos_finais_3 > pontos_finais_4 > maio_pont_entre == menor_pont_entre:
      print(f"1º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"2º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"3º lugar - {maio_entre} : {maio_pont_entre} pontos")
      print(f"4º lugar - {menor_entre} : {menor_pont_entre} pontos")
    elif pontos_finais_3 > maio_pont_entre == menor_pont_entre > pontos_finais_4:
      print(f"1º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"2º lugar - {maio_entre} : {maio_pont_entre} pontos")
      print(f"3º lugar - {menor_entre} : {menor_pont_entre} pontos")
      print(f"4º lugar - {maquina_4} : {pontos_finais_4} pontos")
    elif maio_pont_entre == menor_pont_entre > pontos_finais_3 > pontos_finais_4:
      print(f"1º lugar - {maio_entre} : {maio_pont_entre} pontos")
      print(f"2º lugar - {menor_entre} : {menor_pont_entre} pontos")
      print(f"3º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"4º lugar - {maquina_4} : {pontos_finais_4} pontos")
    elif pontos_finais_4 > pontos_finais_3 > maio_pont_entre == menor_pont_entre:
      print(f"1º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"2º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"3º lugar - {maio_entre} : {maio_pont_entre} pontos")
      print(f"4º lugar - {menor_entre} : {menor_pont_entre} pontos")
    elif pontos_finais_4 > maio_pont_entre == menor_pont_entre > pontos_finais_3:
      print(f"1º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"2º lugar - {maio_entre} : {maio_pont_entre} pontos")
      print(f"3º lugar - {menor_entre} : {menor_pont_entre} pontos")
      print(f"4º lugar - {maquina_3} : {pontos_finais_3} pontos")
    elif maio_pont_entre == menor_pont_entre > pontos_finais_4 > pontos_finais_3:
      print(f"1º lugar - {maio_entre} : {maio_pont_entre} pontos")
      print(f"2º lugar - {menor_entre} : {menor_pont_entre} pontos")
      print(f"3º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"4º lugar - {maquina_3} : {pontos_finais_3} pontos")

#Casos dois pares de iguais
  if (
    pontos_finais_1 == pontos_finais_2 and pontos_finais_3 == pontos_finais_4
    or pontos_finais_1 == pontos_finais_3 and pontos_finais_2 == pontos_finais_4
    or pontos_finais_1 == pontos_finais_4 and pontos_finais_2 == pontos_finais_3
  ):
    if pontos_finais_3 == pontos_finais_4:  
      if maio_pont_entre == menor_pont_entre  > maio_pont_entre3 == menor_pont_entre3:
        print(f"1º lugar - {maio_entre} : {maio_pont_entre} pontos")
        print(f"2º lugar - {menor_entre} : {menor_pont_entre} pontos")
        print(f"3º lugar - {maio_entre3} : {maio_pont_entre3} pontos")
        print(f"4º lugar - {menor_entre3} : {menor_pont_entre3} pontos")
      elif maio_pont_entre == menor_pont_entre  < maio_pont_entre3 == menor_pont_entre3:
        print(f"1º lugar - {maio_entre3} : {maio_pont_entre3} pontos")
        print(f"2º lugar - {menor_entre3} : {menor_pont_entre3} pontos")
        print(f"3º lugar - {maio_entre} : {maio_pont_entre} pontos")
        print(f"4º lugar - {menor_entre} : {menor_pont_entre} pontos")
    
    elif maio_pont_entre == menor_pont_entre  > maio_pont_entre2 == menor_pont_entre2:
        print(f"1º lugar - {maio_entre} : {maio_pont_entre} pontos")
        print(f"2º lugar - {menor_entre} : {menor_pont_entre} pontos")
        print(f"3º lugar - {maio_entre2} : {maio_pont_entre2} pontos")
        print(f"4º lugar - {menor_entre2} : {menor_pont_entre2} pontos")
    elif maio_pont_entre == menor_pont_entre  < maio_pont_entre2 == menor_pont_entre2:
        print(f"1º lugar - {maio_entre2} : {maio_pont_entre2} pontos")
        print(f"2º lugar - {menor_entre2} : {menor_pont_entre2} pontos")
        print(f"3º lugar - {maio_entre} : {maio_pont_entre} pontos")
        print(f"4º lugar - {menor_entre} : {menor_pont_entre} pontos")

#Pondo no Pódio
else:
  if pontos_finais_1 > pontos_finais_2 > pontos_finais_3 > pontos_finais_4:
    print(f"1º lugar - {maquina_1} : {pontos_finais_1} pontos")
    print(f"2º lugar - {maquina_2} : {pontos_finais_2} pontos")
    print(f"3º lugar - {maquina_3} : {pontos_finais_3} pontos")
    print(f"4º lugar - {maquina_4} : {pontos_finais_4} pontos")

  elif pontos_finais_1 > pontos_finais_2 > pontos_finais_4 > pontos_finais_3:
      print(f"1º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"2º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"3º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"4º lugar - {maquina_3} : {pontos_finais_3} pontos")

  elif pontos_finais_1 > pontos_finais_3 > pontos_finais_2 > pontos_finais_4:
      print(f"1º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"2º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"3º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"4º lugar - {maquina_4} : {pontos_finais_4} pontos")

  elif pontos_finais_1 > pontos_finais_3 > pontos_finais_4 > pontos_finais_2:
      print(f"1º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"2º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"3º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"4º lugar - {maquina_2} : {pontos_finais_2} pontos")

  elif pontos_finais_1 > pontos_finais_4 > pontos_finais_2 > pontos_finais_3:
      print(f"1º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"2º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"3º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"4º lugar - {maquina_3} : {pontos_finais_3} pontos")

  elif pontos_finais_1 > pontos_finais_4 > pontos_finais_3 > pontos_finais_2:
      print(f"1º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"2º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"3º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"4º lugar - {maquina_2} : {pontos_finais_2} pontos")

  elif pontos_finais_2 > pontos_finais_1 > pontos_finais_3 > pontos_finais_4:
      print(f"1º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"2º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"3º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"4º lugar - {maquina_4} : {pontos_finais_4} pontos")

  elif pontos_finais_2 > pontos_finais_1 > pontos_finais_4 > pontos_finais_3:
      print(f"1º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"2º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"3º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"4º lugar - {maquina_3} : {pontos_finais_3} pontos")

  elif pontos_finais_2 > pontos_finais_3 > pontos_finais_1 > pontos_finais_4:
      print(f"1º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"2º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"3º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"4º lugar - {maquina_4} : {pontos_finais_4} pontos")

  elif pontos_finais_2 > pontos_finais_3 > pontos_finais_4 > pontos_finais_1:
      print(f"1º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"2º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"3º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"4º lugar - {maquina_1} : {pontos_finais_1} pontos")

  elif pontos_finais_2 > pontos_finais_4 > pontos_finais_1 > pontos_finais_3:
      print(f"1º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"2º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"3º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"4º lugar - {maquina_3} : {pontos_finais_3} pontos")

  elif pontos_finais_2 > pontos_finais_4 > pontos_finais_3 > pontos_finais_1:
      print(f"1º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"2º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"3º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"4º lugar - {maquina_1} : {pontos_finais_1} pontos")

  elif pontos_finais_3 > pontos_finais_1 > pontos_finais_2 > pontos_finais_4:
      print(f"1º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"2º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"3º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"4º lugar - {maquina_4} : {pontos_finais_4} pontos")

  elif pontos_finais_3 > pontos_finais_1 > pontos_finais_4 > pontos_finais_2:
      print(f"1º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"2º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"3º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"4º lugar - {maquina_2} : {pontos_finais_2} pontos")

  elif pontos_finais_3 > pontos_finais_2 > pontos_finais_1 > pontos_finais_4:
      print(f"1º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"2º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"3º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"4º lugar - {maquina_4} : {pontos_finais_4} pontos")

  elif pontos_finais_3 > pontos_finais_2 > pontos_finais_4 > pontos_finais_1:
      print(f"1º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"2º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"3º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"4º lugar - {maquina_1} : {pontos_finais_1} pontos")

  elif pontos_finais_3 > pontos_finais_4 > pontos_finais_1 > pontos_finais_2:
      print(f"1º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"2º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"3º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"4º lugar - {maquina_2} : {pontos_finais_2} pontos")

  elif pontos_finais_3 > pontos_finais_4 > pontos_finais_2 > pontos_finais_1:
      print(f"1º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"2º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"3º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"4º lugar - {maquina_1} : {pontos_finais_1} pontos")

  elif pontos_finais_4 > pontos_finais_1 > pontos_finais_2 > pontos_finais_3:
      print(f"1º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"2º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"3º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"4º lugar - {maquina_3} : {pontos_finais_3} pontos")

  elif pontos_finais_4 > pontos_finais_1 > pontos_finais_3 > pontos_finais_2:
      print(f"1º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"2º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"3º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"4º lugar - {maquina_2} : {pontos_finais_2} pontos")

  elif pontos_finais_4 > pontos_finais_2 > pontos_finais_1 > pontos_finais_3:
      print(f"1º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"2º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"3º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"4º lugar - {maquina_3} : {pontos_finais_3} pontos")

  elif pontos_finais_4 > pontos_finais_2 > pontos_finais_3 > pontos_finais_1:
      print(f"1º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"2º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"3º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"4º lugar - {maquina_1} : {pontos_finais_1} pontos")

  elif pontos_finais_4 > pontos_finais_3 > pontos_finais_1 > pontos_finais_2:
      print(f"1º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"2º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"3º lugar - {maquina_1} : {pontos_finais_1} pontos")
      print(f"4º lugar - {maquina_2} : {pontos_finais_2} pontos")

  elif pontos_finais_4 > pontos_finais_3 > pontos_finais_2 > pontos_finais_1:
      print(f"1º lugar - {maquina_4} : {pontos_finais_4} pontos")
      print(f"2º lugar - {maquina_3} : {pontos_finais_3} pontos")
      print(f"3º lugar - {maquina_2} : {pontos_finais_2} pontos")
      print(f"4º lugar - {maquina_1} : {pontos_finais_1} pontos")


