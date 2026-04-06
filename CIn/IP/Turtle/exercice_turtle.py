import turtle 
# Tela da tartaruga
turtle.Screen()

# A tartaruga
tartaruga = turtle.Turtle()
tartaruga.shape('turtle')
tartaruga.pensize(4)
tartaruga.up()
tartaruga.setposition(-700, 250)
tartaruga.down()
tartaruga.speed(0)

# Função para a malha
def malha(lado_quadrado, abssisas):
    lado_quadrado = lado_quadrado * 5

    for i in range(abssisas):
        for j in range(4):
            tartaruga.forward(lado_quadrado)
            tartaruga.left(90)
        tartaruga.forward(lado_quadrado)

    tartaruga.up()
    tartaruga.backward(lado_quadrado * (abssisas))
    tartaruga.right(90)
    tartaruga.forward(lado_quadrado)
    tartaruga.left(90)
    tartaruga.down()

tamanho_celula = int(input("Digite o tamanho do quadrado da malha: "))
grind_x = int(input("Digite a largura da malha: "))
grind_y = int(input("Digite o comprimento  da malha: "))

for b in range (grind_y):
    malha(tamanho_celula, grind_x)

# Manter a tel aberta
turtle.done()

