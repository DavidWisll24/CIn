# A CORRIDA DE KARTS

## Contexto
O Rei Doce decidiu tornar a final de Sugar Rush uma verdadeira prova de física para Vanellope von Schweetz. A pista é um percurso complexo de *N partes distintas*, repleto de retas, subidas íngremes, descidas perigosas e curvas fechadas. Para vencer, Vanellope precisa prever o futuro!

## Código
No começo de cada segmento, ela deve ajustar o motor do kart escolhendo uma de três ações:

* **Acelerar:** Aumenta a velocidade de entrada no começo do segmento em (+10 m/s.)
* **Manter:** Mantém a velocidade igual à que está no começo do segmento (+0 m/s).
* **Frear:** Reduz a velocidade de entrada no começo do segmento em (-10 m/s.)

Sendo Velocidade atual a velocidade que o kart tem ao começar o segmento, a Velocidade de Entrada no novo trecho é:
***Velocidade de entrada = Velocidade atual + Ação***

### Condições
**Movimento Mínimo:** Se a Velocidade de entrada ≤ 0, o kart apaga o motor e Vanellope perde a corrida.
**Tempo:** O tempo gasto no segmento é: Δt=Velocidade de entrada/Distância.
**Velocidade de Saída (Vsaida):** Dependendo do terreno em que se encontra, a velocidade do kart é alterada após sair do segmento atual em que se encontra:
* Reta (Reta): Velocidade constante. Velocidade de saida = Velocidade de entrada.

* Curva (Curva): Possui um limite de atrito máximo. Se Velocidade de entrada > Limite, o kart derrapa. Senão, Velocidade de saida = Velocidade de entrada.

* Subida (Subida): A gravidade puxa o kart para trás. Velocidade de saida = Velocidade de entrada − Perda. Se a Velocidade de saida≤0, o kart perde a força e rola de ré.

* Descida (Descida): A gravidade empurra o kart! Velocidade de saida = Velocidade de entrada + Ganho. Atenção: Se essa nova Velocidade de saida ultrapassar o Limite_Descida, o kart perde o controle e capota por excesso de velocidade!

***O Fator Glitch:*** Vanellope possui *G* cargas de Glitch. Se a escolha de uma ação resultar em acidente (motor apagar, derrapar na curva, rolar na subida ou capotar na descida) e ela tiver glitches, ela utiliza uma carga de glitch e é salva! Ela completa o segmento da pista instantaneamente, ou seja, tempo gasto no trecho passa a ser 0 segundos, porém, sua velocidade de saída volta a ser 10/ms.

Objetivo: Seu objetivo é encontrar o menor tempo possível para terminar a corrida. Sua solução DEVE ser baseada em uma função recursiva.

## Funcionamento

Comece verificando se Venellope terminou a corrida, caso tenha, verifique o tempo e faça as alterações necessárias.

* Caso ainda não tenha terminado, para cada opção de ajuste do motor do kart:
    - Verifique se a opção tenha velocidade mínima para continuar.
    - Caso tenha, verifique a pista atual em que se encontra e aplique suas propriedades.
    - Se resultou em um acidente, caso ainda tenha, tente utilizar o glitch para avançar na pista.
    - Caso não tenha resultado em um acidente, continue para a próxima pista com a opção selecionada.