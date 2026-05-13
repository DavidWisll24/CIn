# A LENDA DO PIQUENIQUE REAL

## Contexto

Durante o Festival das Lanternas Flutuantes no Reino de Corona, Rapunzel decidiu transformar a celebração em um grande desafio lógico: uma caça ao tesouro mágica dentro de uma floresta encantada.

José Bezerra começa sua jornada no meio dessa floresta, que foi transformada em uma matriz cheia de perigos e pistas. O objetivo é encontrar o **Piquenique Real Perfeito**, localizado na posição especial marcada pela **Lanterna 2**.

## Código (Regras do Jogo)

A floresta é representada por uma matriz NxN onde cada posição pode ser:

* **0 (Espinheiros):** Área proibida. Se José pisar, perde imediatamente.
* **Letras:** Representam lanternas mágicas que formam caminhos possíveis.

José pode se mover pela matriz seguindo as regras:

* Ele pode pisar livremente em letras que pertencem à **Palavra-Chave (S)**.
* Letras que **não pertencem à Palavra-Chave** só podem ser usadas um número limitado de vezes.

## Condições

**Movimento válido:**

* Não pode sair dos limites da matriz.
* Não pode pisar em posições com valor 0.

**Restrição de Letras:**

* Letras da Palavra-Chave → uso ilimitado.
* Letras fora da Palavra-Chave → uso limitado por um valor máximo.

**Backtracking (Caminho Inteligente):**

* Nem todo caminho leva ao destino.
* José pode precisar voltar atrás e tentar novos caminhos.
* A solução exige exploração completa com tentativa e erro.

## Objetivo

Encontrar um caminho válido da posição inicial até a posição do **Piquenique Real (Lanterna 2)** respeitando todas as regras.

A solução ideal deve usar **recursão com backtracking**, explorando todos os caminhos possíveis até encontrar o correto (ou determinar que não existe).

## Input

1. Um inteiro **N** (1 ≤ N ≤ 8): tamanho da matriz.
2. Uma string **S**: Palavra-Chave.
3. Dois inteiros **R e C**: posição inicial de José.
4. **N linhas** com **N caracteres** cada: representação da matriz.
5. Um inteiro: quantidade máxima de usos de letras fora da Palavra-Chave.

## Resumo da Missão

Guie José Bezerra por uma floresta mágica:

* Evite os espinheiros (0).
* Siga as letras permitidas.
* Controle o uso de letras proibidas.
* Volte atrás quando necessário.
* Encontre o caminho até o banquete real.
