A = int(input())
L = int(input())
P = int(input())
H = int(input())

med_A = A * H
med_L = L * H
med_P = P * H

max_AL = (med_A + med_L + abs(med_A - med_L))//2
max_ALP = (max_AL + med_P + abs(max_AL - med_P))//2

print(max_ALP)