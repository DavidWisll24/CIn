# LABIIRINTO DE JAFAR

## Contexto
Jafar prendeu a Princesa Jasmine nas masmorras do palácio de Agrabah. O lugar é um labirinto complexo e sombrio. Aladdin conseguiu um mapa do local, mas as paredes mágicas de Jafar podem confundir qualquer um. Além das paredes, Jafar espalhou tapetes de espinhos que podem ferir a princesa. Para ajudar Jasmine a planejar a fuga mais segura, Aladdin precisa saber exatamente de quantas formas diferentes ela pode sair da cela e chegar ao portão principal.

## Código
Escreva uma função recursiva que receba uma matriz representando o labirinto. A matriz contém:

**. (ponto):** Espaço vazio por onde Jasmine pode caminhar.

**| (barra vertical):** Paredes mágicas intransponíveis.

**, (vírgula):** Tapete de espinhos. Jasmine pode passar por eles, mas são perigosos.

**J:** A posição inicial (cela da Jasmine).

**S:** Saída (portão principal).

Regras de Movimentação e Sobrevivência:

* Jasmine pode se mover para as quatro direções cardinais: Cima, Baixo, Esquerda e Direita.
* Ela não pode passar por cima de uma parede (|).
* Ela não pode visitar a mesma célula duas vezes em um mesmo caminho (para evitar loops infinitos).
* Resistência: Jasmine é forte, mas se pisar em 3 espinhos (,), ela ficará ferida demais para continuar. Portanto, um caminho só é válido se ela chegar à saída tendo pisado em menos de 3 espinhos.

Input

o numero de linhas

    M (int)

o numero de colunas

    N (int)

M linhas:

    M1

    M2

    M3

    M4

    .

    .

    .

Output

Primeiramente, digite:

    Existem {n} maneira(s) de sair do labirinto!

Se não existir caminho possivel, digite:

    Pelo visto Jafar conseguiu tudo que ele sempre quis, Jasmine ficara calada para sempre, ouvi dizer que ele vai espandir o reino até Ababwa

Se existir somente 1 caminho possivel, digite:

    Ufa! Jasmine consegue escapar, mas agora precisam tirar Jafar do poder, é melhor pedirem ajuda ao gênio!

Se existir mais de 1 caminho possível, digite:

    Ninguém me cala! Jasmine derruba Jafar sozinha sem a ajuda de ninguém.
