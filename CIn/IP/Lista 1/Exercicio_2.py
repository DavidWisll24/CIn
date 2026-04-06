velocidade_IJ = int(input())
velocidade_LR = int(input())
dificuldade_inimigos = int(input())

pontos = (velocidade_LR * velocidade_IJ) / dificuldade_inimigos

print(pontos)

if pontos <= 65000:
  print("BRUTAL! Ninguém jamais conseguiu alcançar as pontuações fantásticas do Jorel.")
  
elif pontos > 65000 and pontos <= 99000:
  print("INCRÍVEL! A dupla conseguiu alcançar o top 10 nas pontuações do jogo.")
  
elif pontos > 99000 and pontos <= 153000:
  print("SENSACIONAL!! Os jogadores conseguiram alcançar o pódio do jogo ao lado das outras pontuações do Jorel.")

elif pontos > 153000:
  print("IMPOSSÍVEL!!! A DUPLA IMPLACÁVEL FOI CAPAZ DE QUEBRAR O RECORDE INALCANÇÁVEL DO JOREL!")