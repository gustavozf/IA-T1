from investimentos import buscaProporcao

def menu():
    entrada = raw_input("Bem vindo ao ULTIMATE INVESTIDOR\n" +
            "Para continuar selecione uma das opcoes de busca de investimento:\n"
            "\t 1 - OPCAO 1 (Gustavo Zanoni)\n" + 
            "\t 2 - OPCAO 2 (Mariana Soder)\n" + 
            "\t 3 - OPCAO 3 (Narcizo)\n" +
            "> ")

    buscaProporcao(entrada)
    



if __name__ == '__main__':
    menu()