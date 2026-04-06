print("Ô promessa sem jeito…\n")
moeda_total = 0
quantidade_desculpas = 0
desculpa = ''
plan_b = 0

for i in range(7):
  print(f'Dia {(i + 1)}: Quantas moedas João Grilo conseguiu arrecadar hoje?')
  moeda_dia = int(input())
  moeda_total += moeda_dia
  print(f'No dia {(i + 1)}, o baú já tem R$ {moeda_total}')

print(f"\nTotal arrecadado após o plano: R$ {moeda_total}\n")

if moeda_total == 0:
  print("João Grilo não conseguiu arrecadar nada... direto para o plano B!!")
  plan_b = 1

else:
  print("João Grilo começa a despedida da cachorra:")
  print("'Canis Mortus, Dinherus no Bolsus'")
  print("'Caro nostra quae in patina eius est, canis.'\n")

  print("João Grilo, o padeiro acreditou?")
  resposta = input()

  if resposta.lower() == "sim":
    print("O padeiro acreditou! Chicó pode se casar com Rosinha!")
    print("Como o padeiro acreditou?")

  elif resposta.lower() == "não":
    print("O padeiro não acreditou... João Grilo parte para o Plano B!")
    plan_b = 1
  
if plan_b == 1:
  print("\nQuantas desculpas João Grilo precisa inventar para o Padeiro?\n")
  
  quantidade_desculpas = int(input())

  for i in range(quantidade_desculpas):
    print(f"Digite a {(i + 1)}ª desculpa:")
    desculpa = input()
    print(f"João Grilo disse: '{desculpa}'... e o padeiro caiu na conversa!")
  
print("Chicó: 'Não sei, só sei que foi assim!'")