# O Labirinto

## Contexto:
No labirinto do filme Maze Runner, você é um corredor que teve de adentrar no labirinto após Thomas e Minho se machucarem. Lá, você encontra sinais nas paredes e percebe a relação com a matemática, em especifico com o postulado de Bertrand.
**POSTULADO:** Se k é um número inteiro e k > 1, então existe ao menos 1 número primo(p) entre k e seu dobro, tal que k < p < 2k.

## Regras de Execusão (Mapeamento do Labirinto)
- **1 Rastreamento de seções** Para cada seção maior que 2, deve ser calculado os primos pelo postulado, até a seção n.
- **2 Coleta de Primos** Para cada seção, guardar os números primos encontrados pelo Postulado *SEM REPETIÇÃO*
- **3 Decodificação Final** Após a seção n(última):
    1º Ordene do maior primo para o menor primo especificamente da lista de primos encontrados nesta seção;
    2º Selecionar o maior primo dessa lista
    3º Aplicar formulá de saída: Some 1 a esse maior primo e divida o resultado por dois. Essa será a possível saída.
- **Por fim,** mostre todos os números primos encontrados e a quantidade de vezes que cada um deles apareceu para cada intervalo.

## Exemplo prático
Se a entrada for n = 5, o seu programa fará a seguinte análise:

1. Iniciando com a seção 2:

    Intervalo entre 2 e 4
    Primos encontrados: [3] (pois 2 < 3 < 4)

2. Avançando para a seção 3:

    Intervalo entre 3 e 6
    Primos encontrados: [5] (pois 3 < 5 < 6)

3. Chegando na seção (n = 4):

    Intervalo entre 4 e 8.
    Primos encontrados: [5, 7] (pois 4 < 5 < 8 e 4 < 7 < 8)

4. Seção final de número 5:

    Intervalo entre 5 e 10.
    Primos encontrados: [7] (pois 5 < 7 < 10)

Aplicando a decodificação em n = 5:

    Lista de primos encontrados (em ordem inversa): [7, 5, 3]
    Maior primo encontrado: 7
    Cálculo do destino m: (7 + 1)/2 = 4
    Possível Seção destino: 4

**OBS: O uso do Bubble Sort é obrigatório**

## Entradas
Número da seção (int)

## Saída
Caso seja uma seção menor que 9, encerre o código;
Caso seja válida:
    - Mostre a lista de números primos ordenados inversamente e separados por espaços;
    - Em seguida, imprima, na ordem crescente dos números, a quantidade de vezes que cada número apareceu de maneira correspondente
    - Print vazio(quebra de linha)
    - Caso valor m encontrado no cálculo for igual a entrada informada, isso significa uma armadilha. Mostre:
        Thomas: O cálculo apontou para a seção que você estava! Isso é uma armadilha.
        Minho: O Thomas tem razão.

    - Caso a diferença entre a entrada e o valor seja 1, eles falam:
        Thomas: A decodificação diz que a saída está na seção imediatamente anterior a que você estava.
        Minho: Se isso realmente for válido, então restam 2 opções de saída.
    
    - Já se a diferença entre a entrada e o valor for maior de 1, você diz para eles:
        De todos os cálculos feitos, a única seção que apresentou diferença maior do que 1 foi essa.



## Pensando na lógica
Pelo Crivo de Eurastoteles, a ideia para achar os primos que existem até 2k é eliminar de uma lista com todos os termos de 2 até 2k os multipos de outros numeros diferentes de 1(ou seja, números que não são primos)
 Então:
 A lista se inicia em 2, e como multipos nada mais é que 2 somado x vezes, dá para aplicar essa lógica no código, andando a lista de 2 em 2 para, ou em p em p para um primo qualquer. Acho que um for (i², 2k, i)resolve (o inicial é i² par evitar eliminar o próprio número primo).