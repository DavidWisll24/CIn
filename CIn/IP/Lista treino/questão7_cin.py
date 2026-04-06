D = int(input())

A = 10
L = 30
P = 100

if D <= A:
  print("Arthur")
  
elif D <= L and D > A:
  print("Luiz")
  
elif D <= P and D > L:
  print("Pedro")
  
else:
  print("Nenhum")
  