# DBCIn x DBIp

## Contexto
Simule uma partida entre as equipes DBCIn e DBIp baseada no jogo Dead by Daylight, um jogo de perseguição que consiste em uma equipe de 4 sobreviventes e 1 assassino.
DBCIn será a equipe de sobreviventes com personagens fixos. E DBIp será o assassino. Em partidas diferentes, podem-se usar 3 opções de assassinos.

## Informações/dados principais

**Sobreviventes do DBCIn:**
    *Kate, Dwight, Ada, Vee*

**Assassinos do DBIp:**
    *Spirit, Singularidade, Huntress*

Os sobreviventes e assassinos que forem fornecidos no input **devem ser verificados**.
Cada sobrevivente pode ser enganchado *2 vezes*. Na segunda vez enganchado, o sobrevivente é morto pela entidade. Então, o assassino tem que engachar *8 vezes para vencer*
A partida começa com o assassino no ponto mais *distante* do sobrevivente.
A partida acaba se os sobreviventes fizerem *5 geradores* ou se *todos os sobreviventes morrerem*.
Os sobreviventes precisam se *revezar* para loopar (fugir) do o assassino e *conseguir tempo* para os outros sobreviventes fazerem os geradores.
    **Um gerador é feito a cada 100s.**
Um sobrevivente perde uma perseguição ao tentar sair da área do mapa ou após seu percurso acabar

## Mapa, estruturas e movimentação

O jogo decorre numa matriz 9x9. O mapa é inicialmente preenchido com Mato (M). Dependendo do mapa escolhido (ex: MacMillan, Autohaven), estruturas especiais são colocadas em coordenadas específicas.
Pelo mapa, existem 3 estruturas principais para conseguir tempo, :
    *Shack (Cabana do Assassino): +40s* 
    *Jungle: +25s*
    *LT: +20s*
    *M: +5s*
A Shack e a Jungle só podem ser usadas *uma vez na partida*, depois disso são substituídas por Mato. A LT tem *uso ilimitado*.

Os sobreviventes podem se movimentar pela matriz indo para direita(d), esquerda(e), cima(c), baixo(b) e para as diagonais.
    Para as diagonais:
        d1 = diagonal superior esquerda
        d2 = diagonal superior direita
        d3 = diagonal inferior esquerda
        d4 = diagonal inferior direita

O sobrevivente começa com um tempo de 0 segundos de chase, a medida que ele vai passando pelas estruturas, o tempo deve ir acumulando até que o sobrevivente seja pego (ou seja, acabou seu percurso).

Exemplo: Se o sobrivente percorrer M -> Shack -> M, ele terá um tempo de chase de 50 segundos

**OBS:** Os sobreviventes podem realizar múltiplos movimentos de uma vez

Existe colisão com os limites do mapa, se o sobrevivente chegar no limite, ele é pego pelo assassino.

Localização das estruturas em certos mapas:
*Se for MacMillan:*
- Shack (C): (5, 1)
- Jungle (J): (3, 7)
- LT (LT): (1, 5)
*Se for Autohaven:*
- Shack (C): (1, 6)
- Jungle (J): (2, 2)
- LT (LT): (6, 3)
*Para qualquer outro mapa as coordenadas são:*
- Shack (C): (6, 7)
- Jungle (J): (2, 2)
- LT (LT): (7, 1)

Tenha em mente que as coordenadas começam no (0, 0)

O primeiro elemento da coordenada representa a linha e o segundo a coluna

## Distância e vantagem inicial

O assassino, inicialmente, estára no canto do mapa mais distante entre a posição inicial dos sobreviventes.

Os cantos do mapa são os limites da matriz do mapa, em termos de código, seriam as seguintes coordenadas: 
``[0,0], [0,8], [8,0], [8,8]``

A distância entre os sobreviventes e o assassino é calculada pela expressão:
    Distancia = |linha_1 - linha_2| + |coluna_1 - coluna_2|

Os sobreviventes, inicialmente, terão um tempo de vantagem inicial, que será contabilizado para os geradores.

Esse tempo de vantagem é calculado da seguinte forma:
    tempo de vantagem = 60 + (distancia * 10), sendo distancia o valor da distância inicial entre os sobreviventes e o assassino

## Funções

Você deverá criar as seguintes funções de maneira obrigatória:
    Função do percurso;
    Função para calcular a nova posição do percurso;
    Função para atualizar geradores;
    Função de estruturas.
