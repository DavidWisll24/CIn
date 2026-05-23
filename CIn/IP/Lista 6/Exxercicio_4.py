#O DICIONÁRIO PERDIDO   

#INICIO
num_operacoes = int(input()) #*Número de Vezes que será analisado as traduções
dicionário = {'EN':{}, 'ES':{}}#*Dicionário das traduções

for _ in range(num_operacoes):
    frase_recebida = str(input()).split() #*Recebe na forma de lista as informações para serem traduzidas

    if frase_recebida[0] == '1': #*Se a ação for aprender uma nova palavra
        lingua = frase_recebida[1] #*Recebe a linguagem da tradução

        palavra_traducao = frase_recebida[2:] #*Palavras que serão traduzindas | [0] -> Palavra no idioma estrangeiro; [1] -> Palavra em português
        dicionário[lingua][palavra_traducao[1]] = palavra_traducao[0] #*Adiciona no dicionário a tradução

    elif frase_recebida[0] == '2':
        lingua = frase_recebida[1] #*Recebe a linguagem da tradução
        palavra_traducao = frase_recebida[2:] #*Palavras que serão traduzindas

        traduzido = True #*Diz se conseguiu traduzir TODA a frase
        palavras_traduzidas = list() #*Lista que vai armazenar as palavras traduzindas

        for palavra in palavra_traducao: #*Para cada palavra que deve ser traduzida
            if palavra in dicionário[lingua]: #*Verifica se conhece a tradução
                palavras_traduzidas.append(dicionário[lingua][palavra]) #*Adiciona na lista cada palavra traduzida

            else: #*Não sabe a palavra lida/escutada
                traduzido = False   

        if traduzido: #*Se atradução foi um sucesso
            frase_traduzida = " ".join(palavras_traduzidas)
            print(frase_traduzida)
        else:
            print(f"Não entendi nada daqui, faltam palavras no meu dicionário de {lingua}!")