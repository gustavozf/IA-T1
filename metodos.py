from getInputs import get2016

empresas = ["ambev", "americanas", "bancodobrasil", "cielo", "copel",  "natura", "renner", "sanepar", "vale", "weg"]

def compra(index, empresa, values2016, disponivel, cotacoes):
    numeroCotacoes = (disponivel[empresa]//values2016[empresa][index]) # numero de cotacoes possiveis de serem compradas
    valorGasto = numeroCotacoes * values2016[empresa][index] # numero de cotacoes
    cotacoes[empresa] += numeroCotacoes
    disponivel[empresa] -= valorGasto
    

def mediaMovelPonderada(disponivel): # Mari - Media ponderada
    global empresas
    dias = 247 #dias de 2016, tirando o 1º
    cont = 19
    investimento = {} #quanto tenho pra investir

    values2016 = get2016(18) #dicionario com as infos de 15 e 16

    #fazer o do primeiro dia/ acumulador do dinheiro do moço se sobrar
    while(dias>0):
        for empresa in empresas:
            if (sum(dicionario[empresa][cont-18:cont+1])/18 < sum(dicionario[empresa][cont-4:cont+1])/4): #vende
                #vende tudo e salva no lucro
                #caculo, agora vou tomar banho, bjs
                disponivel[empresa], investimento[empresa] = investimento[empresa], dis

            elif(sum(dicionario[empresa][cont:cont-18]) > sum(dicionario[empresa][cont:cont-4])): #compra
                #compra tudo dessa empresa com o lucro

def mediaMovelSimples(disponivel):
    global empresas

    return "teste"

def mediaMovelExponencial(disponivel):
    global empresas
    dias = 247 #dias de 2016, tirando o 1º
    cont = 18 # maximo = 266
    investimento = {} #quanto tenho pra investir

    values2016 = get2016() #dicionario com as infos de 15 e 16

    while cont < 266:
        for empresa in empresas:
            
    


    return "teste"