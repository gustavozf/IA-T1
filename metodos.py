from getInputs import get2016
import matplotlib.pyplot as plt

empresas = ["ambev", "americanas", "bancodobrasil", "cielo", "copel",  "natura", "renner", "sanepar", "vale", "weg"]
#curto, medio, longo = 21, 42, 100
#curto, medio, longo = 8, 42, 89
curto, medio, longo = 4, 9, 18
saida = open('./outputs/saida.txt', 'w')

def printHistorico(saida, copia, disponivel, vendeu, comprou):
    stringAux = "Historico geral: \n"
    global empresas
    for empresa in empresas:
        if copia[empresa] > 0:
            x = round(((disponivel[empresa]-copia[empresa])/copia[empresa])*100,2)
        else:
            x = 0.0
        stringAux += "\tEmpresa: {0} / Inicial: {1} / Retornado: {2} ({3}%)\n".format(empresa, copia[empresa], disponivel[empresa], x)
        #saida.write("\tEmpresa: {0} / Inicial: {1} / Retornado: {2} ({3}%)\n".format(empresa, copia[empresa], disponivel[empresa], x))
    stringAux +="Total de Vendas = " + str(vendeu) + " / Total de Compras = " + str(comprou)+ " / Total = " +str(sum(disponivel.values())) + "\n"
    #saida.write("Total de Vendas = " + str(vendeu) + " / Total de Compras = " + str(comprou)+ " / Total = " +str(sum(disponivel.values())) + "\n")
    print(stringAux)
    saida.write(stringAux)
    saida.close()

def vendeUltimoDia(values2016, disponivel, cotacoes):
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
    if numeroCotacoes > 0:
        valorGasto = numeroCotacoes * values2016[empresa][index] # numero de cotacoes
        cotacoes[empresa] += numeroCotacoes
        historico[empresa] = values2016[empresa][index]
        disponivel[empresa] -= valorGasto

        return True
    
    return False

def cruzamentoMediaMovel(disponivel): # Mari - Media ponderada
    global empresas
    cont = longo + 1 # posicao do segundo dia de 2016
    dias = 248 + longo #dias de 2016, tirando o 1º
    historico = {}
    global curto
    global longo
    copia = dict(disponivel)
    global saida
    comprou = 0
    vendeu = 0

    values2016 = get2016(longo) #dicionario com as infos de 15 e 16
    print("Executando o Algoritmo: Cruzamento de Media Movel!")

    cotacoes = compraPrimeiroDia(cont-1, disponivel, values2016, historico)
    while(cont<dias):
        for empresa in empresas:
            mediaLonga = sum(values2016[empresa][cont-longo:cont+1])/longo
            mediaCurta = sum(values2016[empresa][cont-curto:cont+1])/curto
            if (mediaLonga > mediaCurta): #vende
                hoje = values2016[empresa][cont]
                if (historico[empresa] < hoje) and (cotacoes[empresa] > 0):
                    #vende tudo e salva no lucro
                    saida.write("Empresa: " + empresa+ " / Status: Venda\n")
                    vendeu +=1
                    venda(cont, empresa, values2016, disponivel, cotacoes)
                else:
                    saida.write("Empresa: " + empresa+ " / Status: Nao Vende\n")
            elif(mediaLonga < mediaCurta): #compra
                #compra tudo dessa empresa com o que tiver disponivel
                if compra(cont, empresa, values2016, disponivel, cotacoes, historico):
                    comprou +=1   
                    saida.write("Empresa: " + empresa+ " / Status: Compra\n")
                else:
                    saida.write("Empresa: " + empresa+ " / Status: Nao Compra\n")
        saida.write("Dia #" + str(cont)+ " / Total: " + str(sum(disponivel.values())) + "\n\n")
        cont+=1

    vendeUltimoDia(values2016, disponivel, cotacoes)
    printHistorico(saida, copia, disponivel, vendeu, comprou)
    print("Fim de execucao!\n")
    
    return sum(disponivel.values())

def mediaMovelSimples(disponivel):
    global empresas
    cont = longo #
    passo = cont -1
    dias = 248 + cont #dias de 2016, tirando o 1º
    global saida
    copia = dict(disponivel)
    historico = {}

    values2016 = get2016(cont)
    print("Executando o Algoritmo: Media Movel Simples!")

    cotacoes = compraPrimeiroDia(cont-1,disponivel, values2016, historico)
    vendeu = comprou = 0
    while cont < dias:
        for empresa in empresas:
            somaDias = sum(values2016[empresa][cont-passo:cont+1])/passo
            hoje = values2016[empresa][cont]
            #print(hoje, somaQuatroDias)
            if(hoje < somaDias):
                if (historico[empresa] < hoje) and (cotacoes[empresa] > 0):
                    saida.write("Empresa: " + empresa+ " / Status: Venda\n")
                    vendeu +=1
                    venda(cont, empresa, values2016, disponivel, cotacoes)
                else:
                    saida.write("Empresa: " + empresa+ " / Status: NADA (Nao-Venda)\n")
            elif (hoje > somaDias): 
                if compra(cont, empresa, values2016, disponivel, cotacoes, historico):
                    comprou +=1   
                    saida.write("Empresa: " + empresa+ " / Status: Compra\n")
                else:
                    saida.write("Empresa: " + empresa+ " / Status: Nao Compra\n")

        saida.write("Dia #" + str(cont)+ " / Total: " + str(sum(disponivel.values())) + "\n\n")
        cont += 1

    vendeUltimoDia(values2016, disponivel, cotacoes)
    printHistorico(saida, copia, disponivel, vendeu, comprou)

    return sum(disponivel.values())

def mme(dia, n, empresa, values2016):
    valorMme = 0
    contador = dia
    for i in range(dia-n, dia+1):
        preco = values2016[empresa][i]
        k = 2/(1+contador)
        valorMme = valorMme + k*(preco-valorMme)
        contador -=1
    return valorMme

def mediaMovelExponencial(disponivel):
    global empresas
    global longo
    global curto
    global saida
    comprou = 0
    vendeu = 0
    cont = longo + 1
    dias = 248 + longo #dias de 2016
    historico = {}
    copia = dict(disponivel)

    values2016 = get2016(longo) #dicionario com as infos de 15 e 16
    cotacoes = compraPrimeiroDia(cont,disponivel, values2016, historico)
    print("Executando o Algoritmo: Media Movel Exponencial!")

    while cont < dias:
        for empresa in empresas:
            hoje = values2016[empresa][cont]
            valorLongo = mme(cont, longo, empresa, values2016)
            valorCurto = mme(cont, curto, empresa, values2016)
            #if(valorCurto < valorLongo):
            if(hoje < valorLongo):
                if (historico[empresa] < hoje) and (cotacoes[empresa] > 0):
                    saida.write("Empresa: " + empresa+ " / Status: Venda\n")
                    vendeu +=1
                    venda(cont, empresa, values2016, disponivel, cotacoes)
                else:
                    saida.write("Empresa: " + empresa+ " / Status: NADA (Nao-Venda)\n")
            #elif (valorCurto > valorLongo):
            elif (hoje > valorLongo): 
                if compra(cont, empresa, values2016, disponivel, cotacoes, historico):
                    comprou +=1   
                    saida.write("Empresa: " + empresa+ " / Status: Compra\n")
                else:
                    saida.write("Empresa: " + empresa+ " / Status: NADA (Nao-Compra)\n")

        saida.write("Dia #" + str(cont)+ " / Total: " + str(sum(disponivel.values())) + "\n\n")
        cont += 1

    vendeUltimoDia(values2016, disponivel, cotacoes)
    printHistorico(saida, copia, disponivel, vendeu, comprou)

    return sum(disponivel.values())

def otimo(disponivel):
    values2016 = get2016(0)
    global empresas
    historico = {}

    cotacoes = compraPrimeiroDia(18, disponivel, values2016, historico)

    for empresa in empresas:
        act = {}
        for dia in range(18, len(values2016[empresa]) - 18):
            if not False in [(values2016[empresa][dia] >= values2016[empresa][i]) for i in range(dia-18, dia + 19)]:
                act[dia] = 0 # venda
            elif not False in [(values2016[empresa][dia] <= values2016[empresa][i]) for i in range(dia-18, dia + 19)]:
                act[dia] = 1 # compra
        
        for i in act.keys():
            if act[i] == 0:
                if cotacoes[empresa] > 0:
                    venda(i, empresa, values2016, disponivel, cotacoes)
            else:
                compra(i, empresa, values2016, disponivel, cotacoes, historico)
    
    vendeUltimoDia(values2016, disponivel, cotacoes)

    return sum(disponivel.values())
