# A BIBLIOTECA DA FERA

## Contexto
A história narra o clássico desafio da **Torre de Hanói**, adaptado para o universo de *A Bela e a Fera*. O resumo do problema é o seguinte:

Bela precisa transferir uma pilha de **$n$ livros** do Pedestal de Carvalho para o Pedestal de Marfim, utilizando um Pedestal de Mármore como suporte auxiliar. Para cumprir a tarefa seguindo o método da Fera, ela deve obedecer a três regras:

## Metodo
*   **Movimentação única:** Ela só pode carregar um livro por vez.
*   **Hierarquia de tamanho:** Um livro maior nunca pode ser colocado sobre um menor; a ordem decrescente (do maior na base ao menor no topo) deve ser mantida.
*   **Eficiência máxima:** O objetivo é concluir a transferência com o **menor número possível de movimentos**.


Para resolver isso de forma **recursiva**, a estratégia consiste em mover a sub-pilha de **$n-1$** livros para o pedestal auxiliar, deslocar o maior livro para o destino final e, por fim, mover a sub-pilha auxiliar sobre o livro maior. O resultado final será sempre de $2^n - 1$ movimentos.