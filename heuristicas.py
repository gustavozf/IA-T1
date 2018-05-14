from dic import FUNCAO

empresas = ["ambev", "americanas", "bancodobrasil", "cielo", "copel",  "natura", "renner", "sanepar", "vale", "weg"]

def heuristica1(disponivel): # heuristica - Mari - Media ponderada
    global empresas
    dias = 247 #dias de 2016, tirando o 1º
    cont = 19
    investimento = {} #quanto tenho pra investir

    dicionario = FUNCAO() #dicionario com as infos de 15 e 16

    #fazer o do primeiro dia/ acumulador do dinheiro do moço se sobrar
    while(dias>0):
        for empresa in empresas:
            if (sum(dicionario[empresa][cont-18:cont+1])/18 < sum(dicionario[empresa][cont-4:cont+1])/4): #vende
                #vende tudo e salva no lucro
                #caculo, agora vou tomar banho, bjs
                disponivel[empresa], investimento[empresa] = investimento[empresa], dis

            elif(sum(dicionario[empresa][cont:cont-18]) > sum(dicionario[empresa][cont:cont-4])): #compra
                #compra tudo dessa empresa com o lucro


