from investimentos import buscaProporcao
from dic import start

def menu():
    return input("Bem vindo ao ULTIMATE INVESTIDOR\n" +
            "Para continuar selecione uma das opcoes de busca de investimento:\n"
            "\t 1 - OPCAO 1 (Gustavo Zanoni)\n" + 
            "\t 2 - OPCAO 2 (Mariana Soder)\n" + 
            "\t 3 - OPCAO 3 (Narcizo)\n" +
            "> ")

if __name__ == '__main__':
    alg = menu()
    print("Importando dados de 2014-2015...")
    start()
    print("Gerando proporcoes de investimentos...")
    buscaProporcao(alg)