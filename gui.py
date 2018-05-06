from tkinter import *

def printa():
	nome_str = nome.get() # pega o valor do campo nome e salva no texto do resultado
	if nome_str != "":
		print("Campo nao vazio!") # printa no log
		resultado["text"] = "Ola " + nome_str + "! :)"
		resultado["fg"] = "white"
		resultado["bg"] = "green"
	else:
		print("Campo vazio!") # printa no log
		resultado["text"] = "Insira um nome! >:("
		resultado["fg"] = "white" # Cor da letra
		resultado["bg"] = "red" # Cor do fundo

# Cria tela
tela = Tk()

# Da titulo a tela
tela.title("Investidor Inteligente")

# Da tamanho a tela
tela.geometry("300x100")

# Cria um campo de entrada
nome = Entry(tela)
nome_label = Label(tela, text="Insira seu nome: ", fg = "blue")

# Posiciona na tela
nome_label.pack()
nome.pack()

# Cria um botao
botao1 = Button(text = "GO!", command = printa)
botao1.pack()

resultado = Label(tela, text = "")
resultado.pack()

tela.mainloop()
