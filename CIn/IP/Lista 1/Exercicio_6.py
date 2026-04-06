robin_disponibilidade = input()
estelar_disponibilidade = input()
ciborgue_disponibilidade = input()
ravena_disponibilidade = input()
mutano_disponibilidade = input()
quantidade_mutano = 0
quantidade_ciborgue = 0
text_robin = 0
text_ravena = 0
text_mutano = 0
text_ciborgue = 0
text_estelar = 0
text_0 =0
text_1 = 0
text_2_4 = 0
text_5 = 0
text_nulo = 0
text_nulo_excesso = 0
text_amor = 0
text_tofu = 0
text_maisforte = 0
text_tranquilo = 0
text_candidatos = 0
quantidade_candidatos = 0
todas_respostas = robin_disponibilidade + estelar_disponibilidade + ciborgue_disponibilidade + ravena_disponibilidade + mutano_disponibilidade
todas_respostas = todas_respostas.upper()

if todas_respostas == "NNNNN":
  text_candidatos = 0
  text_nulo = 1
  text_tranquilo = 1
  
elif  (
  todas_respostas == "SNNNN"
  or todas_respostas == "NSNNN"
  or todas_respostas == "NNSNN"
  or todas_respostas == "NNNSN"
  or todas_respostas == "NNNNS"
):
  text_tranquilo = 1
  quantidade_candidatos = 1
  text_candidatos = 1
  if todas_respostas == "SNNNN":
    selecionado = "Robin"
    text_robin = 1

  elif todas_respostas == "NSNNN":
    selecionado = "Estelar"
    text_estelar = 1
    
  elif todas_respostas == "NNSNN":
    selecionado = "Ciborgue"
    text_ciborgue = 1

  elif todas_respostas == "NNNSN":
    selecionado = "Ravena"
    text_ravena = 1
  elif todas_respostas == "NNNNS":
    selecionado = "Mutano"
    text_mutano = 1
  

elif todas_respostas == "SSNNN":
  quantidade_candidatos = 2
  text_candidatos = 2
  selecionado = "Estelar"
  text_estelar = 1
  text_amor = 1

elif todas_respostas == "NNNSS":
  quantidade_candidatos = 2
  text_candidatos = 2
  selecionado = "Ravena"
  text_amor = 1
  text_ravena = 1
    
elif todas_respostas == "NNSNS":
  quantidade_candidatos = 2
  text_candidatos = 2
  quantidade_mutano = int(input())
  quantidade_ciborgue = int(input())
  
  if quantidade_ciborgue == quantidade_mutano:
    selecionado = input()
    
    if selecionado == "Mutano":
      text_mutano = 1
      text_tofu = 1
      
    elif selecionado == "Ciborgue":
      text_tofu = 1
      text_ciborgue = 1
        
  elif quantidade_mutano > quantidade_ciborgue:
    selecionado = "Mutano"
    text_mutano = 1
    text_tofu = 1

  elif quantidade_ciborgue > quantidade_mutano:
    selecionado = "Ciborgue"
    text_tofu = 1
    text_ciborgue = 1
  
elif (
  todas_respostas == "SSSNN"
  or todas_respostas == "SSNSN"
  or todas_respostas == "SSNNS"
  or todas_respostas == "SNSSN"
  or todas_respostas == "SNSNS"
  or todas_respostas == "SNNSS"
  or todas_respostas == "NSSSN"
  or todas_respostas == "NSSNS"
  or todas_respostas == "NSNSS"
  or todas_respostas == "NNSSS"
  or todas_respostas == "SSSSN"
  or todas_respostas == "SSSNS"
  or todas_respostas == "SSNSS"
  or todas_respostas == "SNSSS"
  or todas_respostas == "NSSSS"  
):
  if (
    todas_respostas == "SSSNN"
  or todas_respostas == "SSNSN"
  or todas_respostas == "SSNNS"
  or todas_respostas == "SNSSN"
  or todas_respostas == "SNSNS"
  or todas_respostas == "SNNSS"
  or todas_respostas == "NSSSN"
  or todas_respostas == "NSSNS"
  or todas_respostas == "NSNSS"
  or todas_respostas == "NNSSS"
  ):
    quantidade_candidatos = 3
  else:
    quantidade_candidatos = 4
  text_candidatos = 2
  if robin_disponibilidade.upper() == "S":
    selecionado = "Robin"
    text_robin = 1
    text_tranquilo = 1

  elif  robin_disponibilidade.upper() == "N":
    selecionado = "Ravena"
    text_ravena = 1
    text_maisforte = 1

elif todas_respostas == "SSSSS":
  text_tranquilo = 1
  text_candidatos = 3
  selecionado = "nulo"
  text_nulo = 1
  text_nulo_excesso = 1

else:
  if (
    todas_respostas == "SNSNN"
    or todas_respostas == "SNNSN"
    or todas_respostas == "SNNNS"
    or todas_respostas == "NSSNN"
    or todas_respostas == "NSNSN"
    or todas_respostas == "NSNNS"
    or todas_respostas == "NNSSN"
  ):
    text_tranquilo = 1
    quantidade_candidatos = 2
    text_candidatos = 2
  if robin_disponibilidade == "S":
    selecionado = "Robin"
    text_tranquilo = 1
    text_robin = 1

  elif ravena_disponibilidade == "S":
    selecionado = "Ravena"
    text_tranquilo = 1
    text_ravena = 1
      
  elif estelar_disponibilidade == "S":
    selecionado = 'Estelar'
    text_tranquilo = 1
    text_estelar = 1

  elif ciborgue_disponibilidade == "S":
    selecionado = "Ciborgue"
    text_tranquilo = 1
    text_ciborgue = 1

  else:
    selecionado = "Mutano"
    text_tranquilo = 1
    text_mutano = 1

#Vendo Quantos Candidatos Tem
if text_candidatos == 0:
  text_0 = 1
elif text_candidatos == 1:
  text_1 = 1
elif text_candidatos == 2:
  text_2_4 = 1
elif text_candidatos == 3:
  text_5 = 1

#Respostas por Candidato

if text_0 == 1:
  print("Parece que ninguém quer participar da Liga da Justiça, o Batman vai ter que ouvir um Super-Esculacho do Super-Homem por não ter conseguido ninguém super forte!")
elif text_1 == 1:
  print("Através de um processo seletivo rigoroso, o mais novo integrante da Liga da Justiça foi escolhido!")
elif text_2_4 == 1:
  print(f"Mesmo com {quantidade_candidatos} candidatos, o(a) {selecionado} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {selecionado}!")
elif text_5 == 1:
  print("Em toda a vida do Batman, ele nunca viu um lugar tão caótico quanto a torre dos titãns depois da notícia, nem mesmo Gotham, com isso ele percebe que não seria ali o local ideal para encontrar o novo salvador da terra!")

#Resposta por pessoa
if text_robin == 1:
  print("Finalmente, Batman e Robin lado a lado, agora como iguais na Liga, será que o Menino Prodígio se provar digno do cargo?!")
elif text_ravena == 1:
  print("Não tinha como a filha de Trigon não ser a escolhida, a mais forte dos Titãns vai botar os inimigos da Liga para correr!")
elif text_ciborgue == 1:
  print("BOOYAH! A tecnologia de ponta do Ciborgue agora faz parte do arsenal da Liga. Até parece que já foi antes...")
elif text_mutano == 1:
  print("O herói mais versátil da torre está pronto para mostrar que tamanho não é documento, especialmente se ele virar um tiranossauro!")
elif text_estelar == 1:
  print("Com a fúria de Tamaran e o brilho das suas rajadas, a Estelar vai iluminar o caminho da Liga da Justiça!")
elif text_nulo == 1:
  print("Poxa, mas que pena, os Titãns vão ter que esperar mais um pouco antes de darem mais um passo na carreira, se continuar assim, vão assinar a CLT.")

#Com Base Nas Condições Especiais

if text_amor == 1:
  print("Parece que o cavalherismo ainda não morreu não é mesmo?")
elif text_tofu == 1:
  print("Nem uma competição árdua assim pode abalar a amizade desses caras!")
elif text_maisforte == 1:
  print("O Batman não iria perder a chance de ter um dos seres mais poderosos do Universo DC no time, o preparo dele não permite isso!")
elif text_tranquilo == 1:
  print("Que bom que tudo deu certo, sem dificuldades!")  