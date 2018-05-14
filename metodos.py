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

def compraPrimeiroDia(disponivel, values2016):
    primDia = 18 #primeiro dia 2016
    cotacoes = {}

    for empresa in empresas:
        cotacoes[empresa] = []
        cotacoes[empresa] = disponivel[empresa] // values2016[empresa][primDia]
        disponivel[empresa] -= cotacoes[empresa]*disponivel[empresa]

    return cotacoes

<<<<<<< HEAD
def venda(index, empresa, values2016, disponivel, cotacoes):
    valor = cotacoes[empresa]*values2016[empresa][index] # quanto ta valendo hoje
    cotacoes[empresa] = 0 #vende tudo
    disponivel[empresa] += valor #add esse valor no disponivel
=======
def venda():
    return 0
>>>>>>> cea6451f3016ba2652511d3407317bff013f61d8

def compra(index, empresa, values2016, dpyisponivel, cotacoes):
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

    cotacoes = compraPrimeiroDia(disponivel, values2016)

    while(dias>0):
        for empresa in empresas:
            if (sum(values2016[empresa][cont-18:cont+1])/18 < sum(values2016[empresa][cont-4:cont+1])/4): #vende
                #vende tudo e salva no lucro
                print ("ha")
            elif(sum(values2016[empresa][cont:cont-18]) > sum(values2016[empresa][cont:cont-4])): #compra
                #compra tudo dessa empresa com o que tiver disponivel
                compra(cont, empresa, values2016, disponivel, cotacoes)
        dias -= 1

def mediaMovelSimples(disponivel):
    global empresas
    dias = 247 #dias de 2016, tirando o 1º
    cont = 5 #maximo = 266

    investimento = {}

    values2016 = get2016(4)

    cotacoes = compraPrimeiroDia(disponivel, values2016)

    while cont < (dias + cont):
        for empresa in empresas:
            if(sum(values2016[empresa][cont-4:cont+1])/4 > values2016[empresa][cont]):
                #venda()
                print("ha")
            else:
                compra(cont, empresa, values2016, disponivel, cotacoes)
        cont += 1

    while cont < (dias + cont):
        for empresa in empresas:
            if(sum(values2016[empresa][cont-4:cont+1])/4 > values2016[empresa][cont]):
                #venda()
            else:
                compra(cont, empresa, values2016, disponivel, cotacoes)
        cont += 1
    return "teste"

def mediaMovelExponencial(disponivel):
    global empresas
    dias = 247 #dias de 2016, tirando o 1º
    cont = 18 # maximo = 266
    investimento = {} #quanto tenho pra investir
    cotacoes = compraPrimeiroDia(disponivel, values2016)
    print(cotacoes)

    values2016 = get2016() #dicionario com as infos de 15 e 16

    while cont < 266:
        for empresa in empresas:
            print("ha")
    
    return "teste"
