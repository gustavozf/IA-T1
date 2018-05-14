from getInputs import get2016

empresas = ["ambev", "americanas", "bancodobrasil", "cielo", "copel",  "natura", "renner", "sanepar", "vale", "weg"]

def setup(valor, disponivel):
    if valor == 1:
        print("Exponencial")
        mediaMovelExponencial(disponivel)
    elif valor == 2:
        print("Ponderada")
        mediaMovelPonderada(disponivel)
    elif valor == 3:
        print("Simples")
        mediaMovelSimples(disponivel)

def compraPrimeiroDia(primDia, disponivel, values2016):
    cotacoes = {}

    for empresa in empresas:
        cotacoes[empresa] = disponivel[empresa] // values2016[empresa][primDia]
        disponivel[empresa] -= cotacoes[empresa]*values2016[empresa][primDia]

    return cotacoes

def venda(index, empresa, values2016, disponivel, cotacoes):
    valor = cotacoes[empresa]*values2016[empresa][index] # quanto ta valendo hoje
    cotacoes[empresa] = 0 #vende tudo
    disponivel[empresa] += valor #add esse valor no disponivel

def compra(index, empresa, values2016, disponivel, cotacoes):
    numeroCotacoes = (disponivel[empresa]//values2016[empresa][index]) # numero de cotacoes possiveis de serem compradas
    valorGasto = numeroCotacoes * values2016[empresa][index] # numero de cotacoes
    cotacoes[empresa] += numeroCotacoes
    disponivel[empresa] -= valorGasto

def mediaMovelPonderada(disponivel): # Mari - Media ponderada
    global empresas
    dias = 247 #dias de 2016, tirando o 1º
    cont = 19 # posicao do segundo dia de 2016
    investimento = {} #quanto tenho pra investir

    values2016 = get2016(17) #dicionario com as infos de 15 e 16

    cotacoes = compraPrimeiroDia(cont, disponivel, values2016)
    while(cont<dias):
        for empresa in empresas:
            if (sum(values2016[empresa][cont-18:cont+1])/18 < sum(values2016[empresa][cont-4:cont+1])/4): #vende
                #vende tudo e salva no lucro
                venda(cont, empresa, values2016, disponivel, cotacoes)
            elif(sum(values2016[empresa][cont:cont-18]) > sum(values2016[empresa][cont:cont-4])): #compra
                #compra tudo dessa empresa com o que tiver disponivel
                compra(cont, empresa, values2016, disponivel, cotacoes)
        cont+=1

    print(sum(disponivel.values()))
    return sum(disponivel.values())

def mediaMovelSimples(disponivel):
    global empresas
    dias = 247 #dias de 2016, tirando o 1º
    cont = 5 #maximo = 266

    investimento = {}
    values2016 = get2016(4)
    cotacoes = compraPrimeiroDia(cont,disponivel, values2016)
    vendeu = comprou = 0
    while cont < dias:
        for empresa in empresas:
            valor = values2016[empresa][cont] - sum(values2016[empresa][cont-3:cont+1])/4
            print(valor, values2016[empresa][cont]*0.1)

            if(valor > values2016[empresa][cont]*0.05): # se os valores dos dias passados estiverem mais baixos
                print("vendeu")
                vendeu +=1                              # hoje esta alto, entao eu vendo
                venda(cont, empresa, values2016, disponivel, cotacoes)
            elif ((valor < (values2016[empresa][cont]*0.1)) and (valor <0)): # se os valores dos dias passados estiverem maiores
                comprou +=1    
                print("comprou")                           # hoje esta mais barato, entao compro
                compra(cont, empresa, values2016, disponivel, cotacoes)
        cont += 1

    print(vendeu, comprou)
    print(sum(disponivel.values()))
    return sum(disponivel.values())

def mediaMovelExponencial(disponivel):
    global empresas
    dias = 247 #dias de 2016, tirando o 1º
    cont = 18 # maximo = 266
    investimento = {} #quanto tenho pra investir

    values2016 = get2016(18) #dicionario com as infos de 15 e 16
    cotacoes = compraPrimeiroDia(cont,disponivel, values2016)
    print(cotacoes)

    while cont < 266:
        for empresa in empresas:
            print("ha")
    
    return "teste"
