# Missão Lazarus e Endurece

**Baseado no Filme Interestelar**, o código da questão 4 tem como objetivo realizar duas fases: Uma de recebimento de dados e outra de análise.

*OBS*: Todos os dados dessa questão devem ser manipulados por meio de uma unica lista (podendo haver sublistas na lista).

## Fase 1
*Missão Lazarus*
Na primeira fase, o usuario vai enviar uma grande string contendo dados sobre planetas que serão analisados.
Esses dados são:
- Nome do planeta
- O nível de habitabilidade (um valor numerico no intervalo [0, 10])
- Estado da sonda (valor string "ok" ou "falha")

## Fase 2
*Missão Endurece*
Agora, na fase de análise, temos dois processos:
**1** - Se um planeta possuir *nivel de habitacionalidade* menor que 6 ou o *status de sua sonda* for "falha", ele deve ser ELIMINADO DA LISTA DE PLANETAS CANDIDATOS

**2** - Apos a eliminação de candidatos incapazes, deve-se organizar a lista de planetas candidatos em **ordem decrescente**, usando como  parametro o *nível de habitalidade*

OUTPUTS:
Antes de começar a Missão Lazarus, imprima:
    Bem vindos, exploradores! Começaremos à Missão Lazarus!

Dada a lista de planetas candidatos, imprima:
    Planetas armazenados. Fim da Missão Lazarus.

Iniciada a Missão da Endurance:
    Hora de escolher os melhores planetas para habitarmos!

Terminada a análise de planetas habitáveis:
    Caso haja pelo menos um planeta na lista, imprima:

        Planetas habitáveis encontrados: {nomes_planetas}.
    - O nome dos planetas devem ser separados por vírgula

    Caso contrário, imprima:
        Planetas habitáveis encontrados: nenhum.

    Além disso, imprima:
        Quantidade de planetas desconsiderados: {num_planetas_removidos}.