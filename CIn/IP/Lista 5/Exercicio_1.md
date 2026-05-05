# A DIVISA JUSTA DA BRANCA DE NEVE

## Contexto
Na Floresta Encantada, o crescimento das maçãs na árvore mágica segue um padrão muito peculiar, conhecido pelos sábios como a Sequência de Fibonacci. A regra de crescimento é a seguinte:

    No dia 0, a árvore não dá frutos (0 maçãs).
    No dia 1, a árvore dá exatamente 1 maçã.
    A partir do dia 2, a quantidade de maçãs do dia é sempre a soma da quantidade de maçãs dos dois dias imediatamente anteriores.

A Branca de Neve pediu ajuda ao Espelho Mágico para prever quantas maçãs estarão disponíveis no dia da colheita usando, obrigatoriamente, uma função recursiva.

Mas a tarefa não acaba aí! Ela é muito justa e quer dividir as maçãs colhidas igualmente entre os 7 anões. O que sobrar dessa divisão exata (se sobrar algo) ficará com a própria Branca de Neve. Sua missão é calcular a colheita e determinar a parte de cada um.

## Código
Fazer um código que calcule a quantidade de maçãs no dia *x* por meio da sequencia de Fibonacci. Além disso, fazer a divisão inteira por 7 do total de maçãs e calcular o resto.

## Input
O seu programa receberá apenas um número inteiro representando o dia da colheita:
- dia_colheita (int)

## Output

Primeiramente, o seu programa deve exibir a pergunta clássica da Branca de Neve:
- Espelho, espelho meu, quantas maçãs a árvore deu?

Em seguida, exiba a quantidade de maçãs calculada para aquele dia usando a sua função recursiva:
- A árvore rendeu {quantidade_macas} maçãs no dia {dia_colheita}.

**Por fim, você deve avaliar a divisão:**

Se a quantidade de maçãs for menor que 7, exiba:
- Oh não! A colheita não foi suficiente para os sete anões.

Se for maior ou igual a 7, você deve calcular quantas maçãs cada anão recebe e quanto sobra para a Branca de Neve, exibindo:
- Cada anão receberá {macas_por_anao} maçã(s) e Branca de Neve ficará com a sobra de {sobra_branca} maçã(s).

Caso especial: Se a divisão entre os anões for exata (sem sobras), exiba uma linha adicional logo abaixo:
- A divisão foi perfeita! Nenhuma maçã sobrou para a torta da Branca de Neve.

***O uso de uma função recursiva é obrigatório.***