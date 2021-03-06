#!/usr/bin/python

empresas = ["ambev", "americanas", "bancodobrasil", "cielo", "copel",  "natura", "renner", "sanepar", "vale", "weg"]

def getValues2014and2015():
    global empresas
    dicionario = {}

    print("Importando dados de 2016...")
    for empresa in empresas:
        dicionario[empresa] = []
        arquivo2015 = open("./inputs/2014-2015/"+empresa+'.txt', 'r')

        aux2 = []
        for linha in arquivo2015:
            if linha != '\n':
                aux2.append(float((linha.split('\t')[1]).replace(',','.')))

        aux2.reverse()
        dicionario[empresa] =  aux2
    
    return dicionario

def get2016(dias2015):
    global empresas
    dicionario = {}

    print("Importando dados de 2016...")
    for empresa in empresas:
        dicionario[empresa] = []
        arquivo2015 = open("./inputs/2014-2015/"+empresa+'.txt', 'r')
        arquivo2016 = open("./inputs/2016/"+empresa+'.txt', 'r')

        aux = []
        for i in range(dias2015):
            linha = arquivo2015.readline()
            if linha != '\n':
                aux.append(float((linha.split('\t')[1]).replace(',','.')))

        aux2 = []
        for linha in arquivo2016:
            if linha != '\n':
                aux2.append(float((linha.split('\t')[1]).replace(',','.')))

        aux.reverse()
        aux2.reverse()
        dicionario[empresa] = aux + aux2
    
    return dicionario

def insertDict(nome, dicionario):
    aux = []
    dicionario[nome] = []
    with open("./inputs/2014-2015/" + nome + ".txt") as f:
        for line in f:
            if line != '\n':
                aux.append(line.split('\t'))
        for i in aux:
            dicionario[nome].append([float(i[5].replace(',','.')),
                                     float(i[1].replace(',','.')),
                                     float(i[6].replace('.',''))])

def get2014and2015():
    dicionario = {}
    global empresas

    print("Importando dados de 2014-2015...")
    for empresa in empresas:
        insertDict(empresa, dicionario)

    return dicionario