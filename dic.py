#!/usr/bin/python

def dic(nome, dicionario):
    aux = []
    dicionario[nome] = []
    with open("./inputs/2014-2015/" + nome + ".txt") as f:
        for line in f:
            if line != '\n':
                aux.append(line.split('\t'))
        for i in aux:
            dicionario[nome].append(float(i[5].replace(',','.')))

def start():
    dicionario = {}
    empresas = ["amazon", "ambev", "americanas", "cielo", "copel", "klabin", "natura", "renner", "vale", "weg"]

    for empresa in empresas:
        dic(empresa, dicionario)
        print("Empresa '", empresa,"' -> ",len(dicionario[empresa]))
    
    #print ( dicionario['amazon'])
    
    return dicionario
