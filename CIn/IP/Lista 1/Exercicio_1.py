print("Olá, eu sou o BMO! Prazer em te conhecer, estranho!")
print("Qual é o seu nome?")
seu_nome = input()

if seu_nome.lower() == "finn" or seu_nome.lower() == "jake":
  print("Caramba, que coincidência! Você tem o mesmo nome de um amigo meu!")
    

print("Gostei do seu nome!")

print("Quantos anos você tem?")
sua_idade = int(input())

if sua_idade == 12:
  print("Nossa, você tem a mesma idade do meu amigo Finn")

print("Entendi!")

print("Ei, qual princesa desse mundo é a mais bonita pra você?")
nome_princesa_bonita = input()

if nome_princesa_bonita.lower() == "princesa jujuba" or nome_princesa_bonita.lower() == "princesa de fogo":
  print("Meu amigo Finn vai ficar com ciúmes de você!")

print("Finalmente chegamos!")    
print(f"Foi um prazer te conhecer, {seu_nome}! Boa sorte para encontrar a {nome_princesa_bonita} :)")