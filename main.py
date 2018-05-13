from geraProporcao import buscaProporcao
from dic import start
import os

def menu():
    return int(input("Bem vindo ao ULTIMATE INVESTIDOR\n" +
            "Para continuar selecione uma das opcoes de busca de investimento:\n"
            "\t 1 - OPCAO 1 (Gustavo Zanoni)\n" + 
            "\t 2 - OPCAO 2 (Mariana Soder)\n" + 
            "\t 3 - OPCAO 3 (Narcizo)\n" +
            "> "))

def getValor():
    return float(input("Insira o valor a ser investido:\n" +
                        ">"))

if __name__ == '__main__':
    condicoes = [False, False]
    valor = 0

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
        condicoes[1] = valor >= 1000

        if not condicoes[1]:
            os.system("clear")
            print("Valor insuficiente para investir em 10 empresas! Favor inserir um valor maior ou igual a R$1000,00")
    
    os.system("clear")
    proporcao = buscaProporcao(valor)
    