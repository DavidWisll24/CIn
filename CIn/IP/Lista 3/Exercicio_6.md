# De Volta Para O Futuro
\\\\\\\\\\\\\\\\\\\\\\\\
## ideia principal
Matriz, onde serão listas: Itens pegos, Quantidade itens pegos

## Coleta de Recursos
O DeLorean não vai a lugar nenhum sem os componentes certos. Marty McFly e o Embananado desceram em um Ponto de Interesse da Ilha para "lootear" tudo o que puderem. No entanto, o inventário é precioso, então não podemos sair catando qualquer lixo que encontrarmos por aí!

Nesta fase sua tarefa é processar uma lista de itens até que a mensagem "Fim Da Coleta!" seja recebida. Os itens são classificados em quatro categorias:

    Objetivos de Missão: Itens essenciais que o Doc pediu.

["Capacitor de Fluxo", "Válvula de Vácuo", "Fragmento do Ponto-Zero"]

    Itens Bônus: Itens raros que seria um absurdo deixá-los para trás.

["Escopeta Lendária", "Vira-Vira", "Peixinho-Dourado Mítico"]

    Lixos: Tralhas que apenas ocupam espaço. (Os Lixos não devem ser coletados!)

["Lata Enferrujada", "Bota Velha", "Cogumelo Mordido"]

    Resto: Todo o resto que não aparece nas categorias anteriores.

Regras da Coleta:

1. Armazenamento: Todos os itens (exceto os Lixos) devem ser guardados em uma lista de inventário. Se um mesmo item for coletado mais de uma vez, você deve apenas incrementar a sua quantidade.

2. Ordenação: Ao final da coleta, o inventário deve ser ordenado com base na quantidade (do item que mais foi coletado pro que menos foi coletado). Caso dois itens tenham aparecido na mesma quantidade, deve prevalecer aquele que foi coletado primeiro.

3. Pontuação: Após a ordenação, a coleta vai ser avaliada com base em uma pontuação. Se o valor da pontuação da coleta não alcançar os 30 pontos, a missão falhou e o código deve encerrar.

    Obs: Se o Marty não coletar pelo menos um dos 3 Objetivos de Missão, a missão falha automaticamente, independentemente da pontuação e o código deve encerrar.

**IMPORTANTE:** Não está autorizado o uso das funções sort() e sorted() nessa questão!
Cálculo da Pontuação:

-Para cada item da Categoria Objetivos de Missão coletado a pontuação é de +30 pontos.

-Para cada item da Categoria Itens Bônus coletado a pontuação é de +10 pontos.

-Para cada item da Categoria Resto coletado a pontuação é de -5 pontos.

-A pontuação deve ser adicionada item por item, na ordem da nossa lista de inventário após a ordenação.

    Obs:

    Se durante o processo a pontuação ficar maior que 100 pontos, ela deve ser reduzida para 100.

    Se durante o processo a pontuação ficar menor que 0 pontos, ela deve ser aumentada para 0.

    Resumindo: A pontuação a cada análise de item, deve sempre ficar no intervalo [0, 100].

## Fase 2: Mapeamento de Frequências Dimensionais

Nesta fase, você receberá uma matriz, onde cada posição dessa matriz contém um sinal (float) que corresponde ao valor da frequência lida naquela posição do mapa.

    Obs: Os valores da matriz vão vir separados na entrada por um hífen entre espaços ' - '

O Doc irá começar o mapeamento no canto superior esquerdo da matriz (linha = 0, coluna = 0). A cada posição visitada ele deve verificar os valores do sinal nas (no máximo 4 [Cima, Baixo, Esquerda, Direita]) posições adjacentes.

A partir disso ele deve se locomover para a posição adjacente com maior sinal, mas apenas se esse maior sinal for maior que a frequência da posição atual.

    Obs: Não haverá casos de empate nessa escolha do movimento.

O Mapeamento termina quando o sinal da posição atual for maior que o de todos os seus vizinhos. Depois do mapeamento, será necessário imprimir uma matriz (com mesmas dimensões da matriz original) no seguinte formato:

    Coloque um '.' para as posições que Doc não visitou.
    Coloque um 'X' para a posição final do mapeamento.
    Coloque um '>' caso Doc tenha se movimentado para a Direita.
    Coloque um '<' caso Doc tenha se movimentado para a Esquerda.
    Coloque um '^' caso Doc tenha se movimentado para Cima.
    Coloque um 'v' caso Doc tenha se movimentado para Baixo.

## Fase 3: De Volta para 1985

Nesta fase, você deve calcular o "Custo de Processamento" para o carro atingir a Velocidade Crítica.

Você receberá uma entrada no formato de string com 7 caracteres — contendo apenas 0 e 1 — (Ex: "0001001", que corresponde ao número 9 em decimal). Essa string representa o estado_inicial do contador.

Binario x Decimal

Sua tarefa é contar o número total de trocas de estado dos bits desse contador para sair do estado_inicial até 88 mph (Velocidade de Transmutação Temporal).

Obs: Essa contagem deve ser feita de número em número (estado por estado). Exemplo: para passar de 67 ("1000011") para 68 ("1000100"), houve 3 bits (marcados em negrito) que mudaram de estado simultaneamente. Você deve acumular todas essas mudanças ocorridas em cada incremento até o objetivo final.

    Dica 1: Para converter de uma (string) binária para um decimal (int) você pode fazer:

string_binario = "0001001"
valor_decimal = int(string_binario, 2)

    Dica 2: Para converter de um decimal (int) para uma (string) binária você pode fazer:

valor_decimal = 9
string_binario = format(valor_decimal, 'b')

    Obs: Em casos de números menores que 64, a string binária convertida pode vir com menos de 7 dígitos, o que pode atrapalhar na comparação com os próximos digitos, lembre-se de adiconar zeros à esquerda nesses casos.