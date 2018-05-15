from getInputs import get2016

empresas = ["ambev", "americanas", "bancodobrasil", "cielo", "copel",  "natura", "renner", "sanepar", "vale", "weg"]
#curto, medio, longo = 21, 42, 100
#curto, medio, longo = 8, 42, 89
curto, medio, longo = 4, 9, 18


def vendeUltimoDia(cont, values2016, disponivel, cotacoes):
    for empresa in empresas:
        venda(len(values2016[empresa])-1, empresa, values2016, disponivel, cotacoes)

def setup(valor, disponivel):
    if valor == 1:
        x = mediaMovelExponencial(disponivel)
    elif valor == 2:
        x = cruzamentoMediaMovel(disponivel)
    elif valor == 3:
        x = mediaMovelSimples(disponivel)
    return x

def compraPrimeiroDia(primDia, disponivel, values2016, historico):
    cotacoes = {}

    for empresa in empresas:
        cotacoes[empresa] = disponivel[empresa] // values2016[empresa][primDia]
        historico[empresa] = values2016[empresa][primDia]
        disponivel[empresa] -= cotacoes[empresa]*values2016[empresa][primDia]

    return cotacoes

def venda(index, empresa, values2016, disponivel, cotacoes):
    valor = cotacoes[empresa]*values2016[empresa][index] # quanto ta valendo hoje
    cotacoes[empresa] = 0 #vende tudo
    disponivel[empresa] += valor #add esse valor no disponivel

def compra(index, empresa, values2016, disponivel, cotacoes, historico):
    numeroCotacoes = (disponivel[empresa]//values2016[empresa][index]) # numero de cotacoes possiveis de serem compradas
    valorGasto = numeroCotacoes * values2016[empresa][index] # numero de cotacoes
    cotacoes[empresa] += numeroCotacoes
    historico[empresa] = values2016[empresa][index]
    disponivel[empresa] -= valorGasto

def cruzamentoMediaMovel(disponivel): # Mari - Media ponderada
    global empresas
    cont = longo + 1 # posicao do segundo dia de 2016
    dias = 248 + longo #dias de 2016, tirando o 1º
    historico = {}
    global curto
    global longo
    saida = open('saida.txt', 'w')
    comprou = 0
    vendeu = 0

    values2016 = get2016(longo) #dicionario com as infos de 15 e 16
    print("Executando o Algoritmo: Cruzamento de Media Movel!")

    cotacoes = compraPrimeiroDia(cont, disponivel, values2016, historico)
    while(cont<dias):
        for empresa in empresas:
            mediaLonga = sum(values2016[empresa][cont-longo:cont+1])/longo
            mediaCurta = sum(values2016[empresa][cont-curto:cont+1])/curto
            if (mediaLonga > mediaCurta): #vende
                hoje = values2016[empresa][cont]
                if historico[empresa] < hoje:
                    #vende tudo e salva no lucro
                    saida.write("Empresa: " + empresa+ " / Status: Venda\n")
                    vendeu +=1
                    venda(cont, empresa, values2016, disponivel, cotacoes)
                else:
                    saida.write("Empresa: " + empresa+ " / Status: NADA\n")
            elif(mediaLonga < mediaCurta): #compra
                #compra tudo dessa empresa com o que tiver disponivel
                compra(cont, empresa, values2016, disponivel, cotacoes, historico)
                comprou +=1    
                saida.write("Empresa: " + empresa+ " / Status: Compra\n")
        saida.write("Dia #" + str(cont)+ " / Total: " + str(sum(disponivel.values())) + "\n\n")
        cont+=1

    saida.write("FIM! Total de Vendas = " + str(vendeu) + " / Total de Compras = " + str(comprou)+ " / Total = " +str(sum(disponivel.values())) + "\n")    
    vendeUltimoDia(cont, values2016, disponivel, cotacoes)
    saida.write("\nVendendo tudo ao ultimo dia do ano! Total = " +  str(sum(disponivel.values())) +"\n")
    saida.close()

    return sum(disponivel.values())

def mediaMovelSimples(disponivel):
    global empresas
    cont = 30 #
    passo = cont -1
    dias = 248 + cont #dias de 2016, tirando o 1º
    saida = open('saida.txt', 'w')
    historico = {}

    values2016 = get2016(cont-1)
    print("Executando o Algoritmo: Media Movel Simples!")

    cotacoes = compraPrimeiroDia(cont,disponivel, values2016, historico)
    vendeu = comprou = 0
    while cont < dias:
        for empresa in empresas:
            somaDias = sum(values2016[empresa][cont-passo:cont+1])/4
            hoje = values2016[empresa][cont]
            #print(hoje, somaQuatroDias)
            if(hoje < somaDias):
                if historico[empresa] < hoje:
                    saida.write("Empresa: " + empresa+ " / Status: Venda\n")
                    vendeu +=1
                    venda(cont, empresa, values2016, disponivel, cotacoes)
                else:
                    saida.write("Empresa: " + empresa+ " / Status: NADA\n")
            elif (hoje > somaDias):
                comprou +=1    
                saida.write("Empresa: " + empresa+ " / Status: Compra\n")
                compra(cont, empresa, values2016, disponivel, cotacoes, historico)

        saida.write("Dia #" + str(cont)+ " / Total: " + str(sum(disponivel.values())) + "\n\n")
        cont += 30

    saida.write("FIM! Total de Vendas = " + str(vendeu) + " / Total de Compras = " + str(comprou)+ " / Total = " +str(sum(disponivel.values())) + "\n")    
    vendeUltimoDia(cont, values2016, disponivel, cotacoes)
    saida.write("\nVendendo tudo ao ultimo dia do ano! Total = " +  str(sum(disponivel.values())) +"\n")
    saida.close()

    return sum(disponivel.values())

def mediaMovelExponencial(disponivel):
    global empresas
    dias = 247 #dias de 2016, tirando o 1º
    cont = 18 # maximo = 266

    values2016 = get2016(18) #dicionario com as infos de 15 e 16
    cotacoes = compraPrimeiroDia(cont,disponivel, values2016)
    print("Executando o Algoritmo: Media Movel Exponencial!")

    while cont < dias:
        for empresa in empresas:
            print("ha")
    
    return "teste"
