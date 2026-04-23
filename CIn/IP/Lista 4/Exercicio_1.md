# Perigos de Fiarlongo

## Contexto
Programa que simula os combates do jogo Silksong. A batalha é estilo alternada até que um dos combatentes sejam derrotados, RESPEITANDO QUE AÇÕES SÓ PODEM SER EXECUTADAS POR PERSONAGENS VIVOS.

## Características - Hornet
O personagem possui 5 pontos de vida(máscaras). Se esse valor chegar a 0, ela perderá a batalha. Como equipamento, ela possui um carreteu, capaz de armazenar até 8 unidades de seda(ele inicia com 0 seda) e o seu ferrão letal.
- Caso seja usado "Ferrão": O chefe (inimigo) sofre 10 de dano e a Hornet ganha 2(duas) sedas;
- Caso seja usado "Ataque de Seda": Causa 20 de dano ao chefe, mas consome 3(três) sedas;
- Casso seja usado "Vincular": Usa todas as 8(oito) sedas do carreteu para recuperar até três máscaras(NÂO PODE ULTRAPASSAR A VIDA MÁXIMA).
**OBS:***Se Hornet tentar usar uma habilidade sem sedas o suficiente, ela hesita e perde o turno*

## Características - Chefe
Sempre possui 140 pontos de vida. Tenta golpear a Hornet, podendo acertar ou errar.
- Acerto: Hornet perde uma máscara;
- Acerto Duplo: Hornet perde duas máscaras;
- Errou: Hornet sai ilesa.

## Informações Armazenadas ao Decorrer da batalha
- Máscaras Restantes: Vida de Hornet ao fim do combate;
- Máscaras Recuperadas: Total de vidas restauradas na batalha;
- Seda Restante: Quantidade de seda dispónivel no carretel ao término da luta.
- Seda desperdiçada: Diferença entre total de seda gerada e seda utilizada.

## OBS Final
Para sua solução ser válida, o alto escalão da cidadela determinou que você deverá criar as seguintes funções:

- Uma função para a ação da Hornet
- Uma função para a ação do chefe
- Uma função para o sistema de batalha