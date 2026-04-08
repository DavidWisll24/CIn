# Todo Rick em Todo Lugar ao Mesmo Tempo

A questão trabalha em torno do Scanner Dimensional do Rick, que:
- **Sempre  inicia com ["C-137", "Planeta Squanch"] no histórico de dimensões**
- **Analisa condições do ambiente, como:**
    - *O usuario no terminal*
    - *A dimensão alvo*
    - *O nível de fluido de portal*

Além disso, o dado sobre o *status de alerta da Federação*  é essencial para a decisão do que será feito para mudar o histórico de dimensões e definir uma estrátegia de saltos, com o intuito de despistar a Federação. 

O programa inicia pedindo 5 informações, nessa ordem: usuario_terminal (str); dimensao_alvo (str); fluido_portal (int or str); status_federacao (str); acao_historico (str)
Onde:
- *usuario_terminal* → Nome de quem está operando a arma no momento
- *dimensao_alvo* → O nome da dimensão detectada pelo scanner
- *fluido_portal* → O nível atual da bateria de fluido verde da arma
- *status_federacao* → Nível de alerta da Federação no setor (alta ou baixa)
- *acao_historico* → O que o sistema deve fazer com a memória da arma (anexar, esconder ou priorizar)

O programa será dividido em 3 fase.
Na **FASE 1** verifica se o fluido de portal foi "Suco de Limão". Se foi, para o código na hora!
Na **FASE 2** verifica o ususario do terminal e a dimensão. Se o usuario_terminal for "Rick Prime" ou "Evil Morty" tem um print x. Já se a dimensão for escrita inteiramente em letras maiúsculas print y.
Na **FASE 3** verifica se deve alterar o histórico de dimensões com os seguintes critérios:
- Se a ação for "anexar" (adicionar dimensão alvo ao final da lista)
- Se a ação for "esconder" (remover o último elemento da lista)
- Se a ação for "priorizar" (inserir dimensão alvo no início da lista)

Após isso, bats apenas verificar a condição de salto atendida, na seguinte ordem de prioridade:
- Se fluido_portal for maior ou igual a 50 E status_federacao for "alta" E o tamanho atual da lista de histórico for maior que 2
- Se fluido_portal for menor que 15
- Se status_federacao for "baixa" E a dimensao_alvo estiver contida dentro da lista de histórico atualizada
- Caso nenhuma das condições anteriores seja atendida