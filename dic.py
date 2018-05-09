#!/usr/bin/python

def dic(nome, dicionario):
    aux = []
    dicionario[nome] = []
    with open("./inputs/2014-2015/" + nome + ".txt") as f:
        for line in f:
            if line != '\n':
                aux.append(line.split('\t'))
        for i in aux:
            dicionario[nome].append(i[5])

def start():
    dicionario = {}

    dic("amazon", dicionario)
    dic("ambev", dicionario)
    dic("americanas", dicionario)
    dic("cielo", dicionario)
    dic("copel", dicionario)
    dic("klabin", dicionario)
    dic("natura", dicionario)
    dic("renner", dicionario)
    dic("vale", dicionario)
    dic("weg", dicionario)

    return dicionario
