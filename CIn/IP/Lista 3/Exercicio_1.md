# Sistema para embarque, desembarque e movimentação na Coração de Ouro

## Tripulação inicial
- Zaphod Beeblebrox (o presidente da galáxia de duas cabeças)
- Ford Prefect (um escritor do Guia do Mochileiro das Galáxias)
- Arthur Dent (um terráqueo desorientado)
- Marvin (um robô depressivo)

## Eventos possíveis
**Embarcar**: Alguem entra na nave no fim da lista de tripulantes
**Priorizar**: O tripulante precisa ir para o inicio da lista
**Remover**: O tripulante sai da nave
**Mover**: O tripulante muda de local na fila

O sistema recebe o nome primeiro o número de ocorrências(valor int). Depois, pede a ação(evento) a ser realizada, o tripulante que sofrerá essa ação e, caso seja "Mover", o index que ele ocupará (valor str).

O sistema utilizará um for, onde cada ocorrencia será analisada
Em cada ocorrencia, ele  deve conseguir diferenciar as três informações [Ação, Tripulante, index(se for mover)] e realizar o evento correspondente dentre as opções.