# O Labirinto

## Contexto:
No labirinto do filme Maze Runner, você é um corredor que teve de adentrar no labirinto após Thomas e Minho se machucarem. Lá, você encontra sinais nas paredes e percebe a relação com a matemática, em especifico com o postulado de Bertrand.
**POSTULADO:** Se k é um número inteiro e k > 1, então existe ao menos 1 número primo(p) entre k e seu dobro, tal que k < p < 2k.

## Regras de Execusão (Mapeamento do Labirinto)
- **1 Rastreamento de seções** Para cada seção maior que 2, deve ser calculado os primos pelo postulado, até a seção n.
- **2 Coleta de Primos** Para cada seção, guardar os números primos encontrados pelo Postulado *SEM REPETIÇÃO*
- **3 Decodificação Final** Após a seção n(última):
    1º Ordene do maior primo para o menor primo ESPECIFICAMENTE DA LISTA DE PRIMOS ENCONTRADOS NESSA SEÇÃO;
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
