# Restam ZERO Dias

## Contexto
Zero é um assassino silencioso em uma metrópole decadente e violenta. Ele utiliza uma katana e a habilidade de manipular o tempo para prever ataques e corrigir falhas. Em suas missões contra criminosos, a precisão é vital: qualquer erro exige que ele utilize seus poderes para recomeçar e tentar novamente até atingir a perfeição. 
O programa que deve ser feito tem o objetivo de classificar e determinar o sucesso e fracassos das missões do Zero.

## Contagem Regressiva
Será recebido de inicio um vaor correspondente a quantidade de dias que faltam para Zero concluir as missões e no inicio de cada novo dia, deve ser mostrado quantos dias faltam para que todas as missões sejam concluidas. Para cada dia, deve ser executado uma série de verificações

## Caso Especial
Caso o autor da musica seja “DJ Electrohead” e o alvo também seja o “DJ Electrohead” todas as verificações devem ser puladas e seu programa deve seguir para o próximo dia.

## ETAPAS
### Etapa 1
**Classificação dos Alvos:** 
- nivel_ameaca maior ou igual a 7 e armado: "Elite"
- nivel_ameaca maior ou igual a 7 e não armado: "Executor"
- nivel_ameaca maior ou igual a 4 e menor que 7 e armado: "Veterano"
- nivel_ameaca maior ou igual a 4 e menor que 7 e não armado: "Operador"
- nivel_ameaca menor que 4: "Iniciante"

### Etapa 2
O ZERO utiliza manipulação temporal para realizar múltiplas tentativas de uma missão, cada uma representada por um código numérico em uma lista. A missão só é bem-sucedida se a soma dos códigos for divisível pela quantidade de tentativas (resto zero); caso contrário, o processo é encerrado.

### Etapa 3
O inimigo Dragão possui tipos de ataques favoritos para refletir, já definidos na lista abaixo. Deve percorrer a lista de ataques recebidos e verificar quais ataques são múltiplos de qualquer um dos tipos favoritos.

favoritos = [3, 5]

## Funções
Vai precisar montar uma função para cada verificação.

    Uma para classificar o alvo
    Uma para analisar as tentativas.
    Uma para os ataques refletidos.

## Informações recebidas - Em Ordem
dia_inicial (int)
musica (str) formato: nome_da_musica - autor
alvo (str) formato: nome - nivel de ameaça - armado
tentativas (str) formato: lista de numeros separados por espaço
ataques_inimigos (str) formato: lista de numeros separados por espaço