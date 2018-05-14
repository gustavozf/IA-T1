from getInputs import get2016

empresas = ["ambev", "americanas", "bancodobrasil", "cielo", "copel",  "natura", "renner", "sanepar", "vale", "weg"]

<<<<<<< HEAD
def compraPrimeiroDia(disponivel, values2016):
    primDia = 18 #primeiro dia 2016 
    cotacoes = {}

    for empresa in empresas:
        cotacoes[empresa] = disponivel[empresa] // values2016[empresa][primDia]
        disponivel[empresa] -= cotacoes[empresa]*disponivel[empresa]

    return cotacoes

def venda()
=======
def compra(index, empresa, values2016, disponivel, cotacoes):
    numeroCotacoes = (disponivel[empresa]//values2016[empresa][index]) # numero de cotacoes possiveis de serem compradas
    valorGasto = numeroCotacoes * values2016[empresa][index] # numero de cotacoes
    cotacoes[empresa] += numeroCotacoes
    disponivel[empresa] -= valorGasto
    
>>>>>>> c95513f4fc9e68b0322f6730ed3ef0b25aaa42e7

def mediaMovelPonderada(disponivel): # Mari - Media ponderada
    global empresas
    dias = 247 #dias de 2016, tirando o 1º
    cont = 19 # posicao do segundo dia de 2016
    investimento = {} #quanto tenho pra investir

<<<<<<< HEAD
    values2016 = get2016(17) #dicionario com as infos de 15 e 16

    cotacoes = compraPrimeiroDia(disponivel, values2016)
=======
    values2016 = get2016(18) #dicionario com as infos de 15 e 16
>>>>>>> c95513f4fc9e68b0322f6730ed3ef0b25aaa42e7

    #fazer o do primeiro dia/ acumulador do dinheiro do moço se sobrar
    #disponivel é o dinheiro, tem que ter 

    while(dias>0):
        for empresa in empresas:
            if (sum(values2016[empresa][cont-18:cont+1])/18 < sum(values2016[empresa][cont-4:cont+1])/4): #vende
                #vende tudo e salva no lucro
                #disponivel[empresa], investimento[empresa] = investimento[empresa], dis
                compra(cont)

            elif(sum(values2016[empresa][cont:cont-18]) > sum(values2016[empresa][cont:cont-4])): #compra
                #compra tudo dessa empresa com o lucro
        dias -= 1

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