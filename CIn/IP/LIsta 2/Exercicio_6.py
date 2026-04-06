#Variáveis
quant_cidades = cidade = 0
informacao = validacao = aux_info =  ''
info_endereco = info_lembraca = info_identidade = 0
validacao_final = info = False

#Print Inicial
print("Pega a sua trouxa, moleque. O ônibus pro sertão já vai sair.")

quant_cidades = int(input())
print(f"Se ajeita nesse banco, menino, que o chacoalho vai ser grande. A gente tem {quant_cidades} cidade(s) de poeira pela frente até achar o tal do teu pai. Presta atenção no que o povo fala...")

#Procurando informações em cada cidade
while quant_cidades > 0:
    repetida_s = repetida_bj = repetida_j = repetida_m = repetida_i = repetida_l = false = true = 0
    validacao =  informacao = ''
    cidade += 1
    quant_cidades -= 1
    info = False

    print(f"Atenção, {cidade}ª cidade! Carta de graça! A gente só quer informação da minha família em troca!")
    while informacao != "FIM":
        informacao = input() 

        #Verificando teve ao menos uma informação
        if informacao != "FIM":
            info = True


        #Verificando endereços
        if "sertao" in informacao and repetida_s == 0:
            validacao += "{"
            repetida_s = 1
    
        elif "sertao" in informacao and repetida_s == 1:
            validacao += "}"
            repetida_s = 0
    
        elif "bom jesus" in informacao and repetida_bj == 0:
            validacao += "{"
            repetida_bj = 1
    
        elif "bom jesus" in informacao and repetida_bj == 1:
            validacao += "}"
            repetida_bj = 0
    
        #Verificando identidade
        elif "jesus" in informacao and "bom jesus" not in informacao and repetida_j == 0:
            validacao += "("
            repetida_j = 1
        elif "jesus" in informacao and "bom jesus" not in informacao and repetida_j == 1:
            validacao += ")"
            repetida_j = 0
    
        elif "isaias" in informacao and repetida_i == 0:
            validacao += "("
            repetida_i = 1
        elif "isaias" in informacao and repetida_i == 1:
            validacao += ")"
            repetida_i = 0
    
        elif "moises" in informacao and repetida_m == 0:
            validacao += "("
            repetida_m = 1
    
        elif "moises" in informacao and repetida_m == 1:
            validacao += ")"
            repetida_m = 0
        
        #Verificando lembraça
        elif repetida_l == 0 and informacao != 'FIM':
            validacao += "["
            repetida_l = 1
        elif repetida_l == 1 and informacao != 'FIM':
            validacao += "]"
            repetida_l = 0

        
    #Caso informação for nula
    if info == False and quant_cidades > 0:
        print("Ô cidadezinha morta, Josué. Ninguém abriu a boca pra dar um pio do teu pai. Dobra essa mesa que aqui a gente só gastou saliva à toa.")

    #Criando duas variáveis para auxiliar no processo de verificar ser 'validacao' é válido
    aux_valido = ''
    valido = True

    #Analisando informações recebidas
    for i in validacao:
        if (i == '{'
            or i == '('
            or i == '['
        ):
            aux_valido += i
        
        else:
            if aux_valido == '':
                valido = False
            
            else:
                ultimo = ''

                for j in aux_valido:
                    ultimo = j 

                if (ultimo == '(' and i != ')'
                    or ultimo == '[' and i != ']'
                    or ultimo == '{' and i != '}'
                ):
                    valido = False
                else:
                    novo_valido = ''
                    novo_tamanho = 0
                    tamanho = len(aux_valido)

                    for k in aux_valido:
                        if novo_tamanho < tamanho - 1:
                            novo_valido += k
                        novo_tamanho += 1

                    aux_valido = novo_valido

    if aux_valido != '':
        valido = False

    #Vendo se os dados são válidos
    if (valido == True
        and '(' in validacao and ')' in validacao
        and '[' in validacao and ']' in validacao
        and '{' in validacao and '}' in validacao   
    ):
        print("A história bateu, Josué. O povo falou a mesma coisa. Pega tuas coisas que a gente achou o caminho do teu pai.")
        quant_cidades = 0  
        validacao_final = True  
    
    elif (valido == False
        or '(' not in validacao or ')' not in validacao
        or '[' not in validacao or ']' not in validacao
        or '{' not in validacao or '}' not in validacao           
    ): 
        if quant_cidades != 0 and info != False:
            print("Essa conversa tá toda torta, um fala uma coisa, outro fala outra. Vamos embora, menino, a busca continua.")


if validacao_final == False:
    print("Não achamos eles nessas cidades, Dona Dora... Mas amanhã a gente bota a mesinha de novo, né? O Brasil é grande, uma hora a gente encontra.")

elif validacao_final == True:
    print("------------------------------------------------------------")
    print("✅ Pistas confirmadas. Josué encontrou os irmãos e uma carta de seu pai.")
    print("A missão de Dora terminou. Pela janela do ônibus, ela escreve para o menino que deixou para trás:")
    print("✉️ Dora: 'Você tem razão. Seu pai ainda vai aparecer e, com certeza, ele é tudo aquilo que você diz que ele é.'")
    print("✉️ Dora: 'Quando você estiver cruzando as estradas no seu caminhão enorme, espero que você lembre que fui eu a primeira pessoa a te fazer botar a mão no volante.'")
    print("✉️ Dora: 'No dia que você quiser lembrar de mim, dá uma olhada no retratinho que a gente tirou junto... Tenho medo que um dia você também me esqueça. Tenho saudade de tudo.'")