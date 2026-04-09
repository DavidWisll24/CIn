"""
lista = [4, 25, 8, 9, 1, 7, 24, 11, 12, 74, 2, 6, 7, 9, 74, 47]

for i in range(len(lista) - 1):
    for j in range(i, len(lista) - 1):
        if lista[i] > lista[j+1]:
            lista[i], lista[j+1] = lista[j+1], lista[i]

print(lista)
"""
a = ["abcd", "bcd", "cd", "d", "acdb", "adb", "acda"]

for i in range(len(a)-1):
    for j in range(i, len(a)-1):
        if a[i] < a[j+1]:
            a[i], a[j+1] = a[j+1], a[i]

print(a)