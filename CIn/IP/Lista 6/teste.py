"""b = 'batata nana ma na jua p'
print(b.rsplit(' ', 2))
print(b.rsplit(' ', 1))

dic = {b:{'banana':2}}

if 'banana' in dic[b]:
    print(6)"""

c = 'bab foah fouag buaf aoifg aif iafg fiha'
nome = ''
for b in c.split()[0:-1]:
    if b == c.split()[-2]:
        nome += b    
    else:
        nome += b + ' '
print(nome)