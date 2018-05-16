from geraProporcao import buscaProporcao
import os
from metodos import *

def menu():
    return int(input("Bem vindo ao Investidor Inteligente\n" +
            "Para continuar selecione uma das opcoes de busca de investimento:\n"
            "\t 1 - Media Movel Exponencial (Gustavo Zanoni)\n" + 
            "\t 2 - Media Movel Ponderada (Mariana Soder)\n" + 
            "\t 3 - Media Movel Simples (Narcizo)\n" +
            "> "))

def getValor():
    return float(input("Insira o valor a ser investido:\n" +
                        ">"))

if __name__ == '__main__':
    condicoes = [False, False]
    valor = 0
    empresas = ["ambev", "americanas", "bancodobrasil", "cielo", "copel",  "natura", "renner", "sanepar", "vale", "weg"]

    os.system("clear")
    while not condicoes[0]:
        alg = menu()
        condicoes[0] = alg in range(1, 4)

        if not condicoes[0]:
            os.system("clear")
            print("Opcao inexistente! Tente novamente!")
    
    os.system("clear")
    while not condicoes[1]:
        valor = getValor()
        condicoes[1] = valor >= 4000

        if not condicoes[1]:
            os.system("clear")
            print("Valor insuficiente para investir em 10 empresas! Favor inserir um valor maior ou igual a R$4000,00")
    
    os.system("clear")
    proporcao = buscaProporcao(valor)
    disponivel = {}

    i = 0
    for empresa in empresas:
        disponivel[empresa] = proporcao[i]
        i +=1

    copia = dict(disponivel)
    print('Simulando...')
    total = setup(alg, disponivel)
    print("Total Acumulado = " +str(total)+ "\n" +
          "Total de Lucro = " + str(round(total - valor,2)) +" ("+ str(round(((total-valor)/valor)*100,2))+ "%)\n\n" + 
          "Para mais informacoes, veja o arquivo 'saida.txt'!\n" +
          "Fim de simulacao!\n")

    choice = input('Deseja exibir o otimo para esta configuracao? (s/n)\n> ')
    if (choice.upper() == 'S'):
        total = otimo(copia)
        print('Otimo estipulado => Total: {0} / Lucro: {1} ({2} %)'.format(total, total-valor, 
                                                                    round((((total-valor)/valor)*100),2)))
