# A Lobotomy CInCorporation

## Contexto
Vocẽ acaba de ser convocado para fazer um código para a **Lobotomy CinCorporation** para fazer um código que analisa os níveis de energia gerados durante o dia.

## Código
Cada dia na corporação é documentado. O primeiro dia **sempre** necessitará de **100** de energia para ser concluído, com um acréscimo de 40 de energia a cada dia seguinte. Um dia será considerado bem-sucedido se a energia gerada naquele dia for maior ou igual a energia necessária do dia. Caso contrário, o dia é considerado falho!

**A Cada** novo dia, deve ser recebido o nome de um Sefirá.
**Sefirás válidos: Malkuth, Yesod e Binah**
Caso não seja um desses Sefirás, o DIA acaba e é considerado falha.

Dependendo do Sefirá recebido, uma série de etapas devem ser realizadas.

### Mulkuth
**Algoritmo de Ordenação de Nomes:** Recebe uma lista de nomes separados por espaço. Esses nomes devem ser ordenados de acordo com o tamanho do nome (do maior para o menor).
Após a ordenação, use a seguinte fórmula para determinar a energia coletada no dia: 
(Tamanho do primeiro nome + Tamanho do último nome) × 20

**OBS1**: Nomes de mesmo tamanho devem manter a ordem original da entrada.
**OBS2**: Caso nenhum nome seja fornecido, encerre o dia imediatamente — o resultado do dia será falha.
**OBS3**: O uso de .sort() e .sorted() é proibido, apenas nesse Sefirá.

### Yesod
**Algoritmo de Compressão de Dados:** Seu objetivo é comprimir essa sequência para o formato "NC", onde N é o número de vezes que o caractere aparece consecutivamente e C é o caractere correspondente. Caracteres que aparecem apenas uma vez devem ser mantidos como estão. Por exemplo, dada a sequência **AAABBBCCDDEEEEF**, a saída esperada seria: **3A3B2C2D4EF**.

Se não houver nenhuma corrupção nessa fase, o dia encerra em sucesso automatico, independente da quantidade de energia necessária para finalizar o dia.

A corrupção ocorre quando um dos caracteres lidos na sequência é ***&***. Quando esse caractere aparecer na sequência, você deve parar a compressão naquele ponto. Por exemplo, se a sequência for: **AAA&BB** a saída esperada seria **3A**, pois nada a partir do & deve ser contabilizado. Independente de onde a corrupção apareceu, o resultado do dia sempre é falho.

**OBS:** Caso a corrupção ocorra logo no início, você deve manter a saída vazia.

### Binah
**Algoritmo de Multiplicação de Matrizes:** No dia da Binah, você receberá duas matrizes 3x3, cada uma com suas linhas separadas por espaços. Seu objetivo é calcular o produto entre as duas matrizes e exibir a matriz resultante. A energia coletada será a soma da diagonal principal da matriz resultante.

## Funções
Você deverá criar as seguintes funções de maneira obrigatória:

- Função do manejo dos dias;
- Uma função para cada Sefirá.