#A BIBLIOTECA DA FERA

#Função Recursiva
def movimentar_livros(qtd_livros):
    if qtd_livros <= 1: #*Caso Base | Se tiver um livro, so  é necessário 1 movimento
        movimentos_necessarios = 1 #*Variável da quantidade de movimentos
        return movimentos_necessarios
    else:
        movimentos_necessarios = 2 * movimentar_livros(qtd_livros - 1) + 1 #*Padrão percebido ao analisar o caso base e vendo o comportamento seguinte
        return movimentos_necessarios

#INICIO
numero_livros = int(input()) #*Recebe quantos livros devem ser mudados de lugar

total_movimentos_realizados = movimentar_livros(numero_livros) #*Armazena o total de movimentos feitos por Bela para mudar os livros de lugar

print(f"Bela moveu os {numero_livros} livros em {total_movimentos_realizados} movimentos para o Pedestal de Marfim.")