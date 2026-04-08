print("Sistema Operacional RickOS v3.14 - Inicializando Arma de Portais...")

#Variáveis
historico_dimensional = ["C-137", "Planeta Squanch"]
usuario_terminal = input()
dimensao_alvo = input()
fluido_portal = input()
fluido_portal = int(fluido_portal) if fluido_portal.replace(' ', '').isnumeric() else str(fluido_portal)
status_federacao = input()
acao_historico = input()
letra_dimensao = 'a'

#Verificando Suco de Limão
if fluido_portal == "Suco de Limão":
    print("BURP Morty, você colocou Suco de Limão onde devia ter número! O sistema pifou!")

#Código continua
else:
    #Verifica se a dimensão possui apenas letras
    if dimensao_alvo.replace(" ", '').isalpha():
        letra_dimensao = dimensao_alvo
    #Print especial
    if usuario_terminal == "Rick Prime" or usuario_terminal == "Evil Morty":
        print("Alerta Vermelho: Variante perigosa detectada no terminal!")
    if letra_dimensao.isupper():
        print("Não precisa gritar, Morty! O painel da arma não é surdo!")

    #Alterando histórico
    if acao_historico == "anexar":
        print("Rastro anexado ao final do histórico.")
        historico_dimensional.append(dimensao_alvo)
    elif acao_historico == "esconder":
        print("Apagando o último rastro... Federação idiota.")
        historico_dimensional.pop()
    elif acao_historico == "priorizar":
        print("Sobrescrevendo prioridades. Nova dimensão no topo da lista!")
        historico_dimensional.insert(0, dimensao_alvo)

    #Definindo plano de salto
    if type(fluido_portal) == int:
        if fluido_portal >= 50 and status_federacao == "alta" and len(historico_dimensional) > 2:
            print("Fuga tática ativada! Saltando por múltiplas dimensões para despistar os insetos!")
        elif fluido_portal < 15:
            print("Ferrou! A Arma de Portais tá quase vazia. Pega a nave, Morty!")
        elif status_federacao == "baixa" and dimensao_alvo in historico_dimensional:
            print(f"Ah, já estivemos na dimensão {dimensao_alvo}. Bora encher a cara no Blips and Chitz!")
        else:
            print("Preparando salto interdimensional... Wubba Lubba Dub Dub!")
    else:
        if status_federacao == "baixa" and dimensao_alvo in historico_dimensional:
            print(f"Ah, já estivemos na dimensão {dimensao_alvo}. Bora encher a cara no Blips and Chitz!")
        else:
            print("Preparando salto interdimensional... Wubba Lubba Dub Dub!")