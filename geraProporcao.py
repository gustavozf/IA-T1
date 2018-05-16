import os, sys, random, operator # bibliotecas que podem vir a ser uteis
from math import ceil
from getInputs import *
from fnFitness import *
import matplotlib.pyplot as plt

empresas = ["ambev", "americanas", "bancodobrasil", "cielo", "copel", "natura", "renner", "sanepar", "vale", "weg"]
tamPopulacao = 100
numFilhos = 100
dicionario2 = [] #= getValues2014and2015()
fitValues= {}

def localFitness(elem, valor, dicionario):
	global fitValues
	nome = str(elem)
	if nome not in fitValues:
		fitValues[nome] = fnFitness(elem, valor, dicionario)
	return fitValues[nome]

def checkSum(lista):
	soma = 0
	for i in lista:
		soma += i

	return soma

def melhorIndividuo(populacao, valor, dicionario):
	'''
	Funcao que retorna o melhor individuo de uma populacao
	'''
	fit = []
	for individuo in populacao:
		fit.append(localFitness(individuo, valor, dicionario))
	return list(populacao[fit.index(max(fit))])
	# Organizar um dicionario por valor:
	# OBS.: reverese = True --> Deixa a lista em formato decrescente
	# sorted(x.items(), key=operator.itemgetter(1), reverse = True)

def atualizar(populacao, novaPopulacao, valor, dicionario):
	'''
	Funcao que atualiza a populacao antiga com a nova. Elitista.
	'''
	fit = []
	novaPop = []
	for individuo in populacao:
		fit.append(localFitness(individuo, valor, dicionario))
	for i in range(int(tamPopulacao*0.85)):
		posicao = fit.index(max(fit))
		fit[posicao] = -8000000
		novaPop.append(list(populacao[posicao]))
	#print ("fit =", fit)
	fit = []
	for individuo in novaPopulacao:
		fit.append(localFitness(individuo, valor, dicionario))
	for i in range(int(tamPopulacao*0.15)):
		posicao = fit.index(max(fit))
		fit[posicao] = -8000000
		novaPop.append(list(novaPopulacao[posicao]))

	#print ("pop = ", populacao)
	#print ("novapop = ", novaPopulacao)
	#print ("fit =", fit)
	#print ( "novaPop = ", novaPop)
	#print ("tamanho = ", len(novaPop)) 
	return list(novaPop)

def mutacao(filho):
	'''
	Funcao que muta um individuo. Utiliza do swap.
	'''
	for i in range(0,4):
		a = random.randint(0, 9) # Inclui o 9
		b = random.randint(0, 9)
		filho[a], filho[b] = filho[b], filho[a]

def reproduz(x, y):
	'''
	Reproduz um filho de "x" e "y". O ponto de corte eh decidido aleatoriamente
	'''
	soma = 0
	diferenca = 0
	porcentagem = 0
	pontoDeCorte = [random.randint(1, 8), random.randint(1, 8)]

	pontoDeCorte.sort()

	filho = x[:pontoDeCorte[0]] + y[pontoDeCorte[0]:pontoDeCorte[1]] + x[pontoDeCorte[1]:]

	#print( "Filho: ", filho)

	# Verifica se o filho alcancou 100%
	soma = checkSum(filho)
	#print('soma: ', soma)

	if soma != 100:
		for i in range(10):
			filho[i] = int((filho[i]/soma)*100)
		aux = checkSum(filho)
		if aux < 100:
			resto = 100 - aux
			if 0 in filho:
				filho[filho.index(0)] = resto
			else:
				filho[random.randint(0,9)] = resto

	soma = checkSum(filho)
	#print( "Filho: {0} / Soma: {1}".format(filho, soma))

	return filho

def selecao(populacao,valor, dicionario):
	'''
	Selecao realizada por torneio.
	Seleciona dois individuos aleatorios da populacao e em seguida,
	retorna o melhor!
	'''

	primSelecionado = random.choice(populacao)
	segunSelecionado = random.choice(populacao)

	if (localFitness(primSelecionado, valor, dicionario) > localFitness(segunSelecionado, valor, dicionario)):
		return primSelecionado
	else:
		return segunSelecionado

def pequenaProbabilidadeAleatoria():
	'''
	Eh sorteado um numero aleatorio entre 1 e 100.
	Se este estiver presente entre 34 - 41, eh retornado True.
	Caso contrario, False
	'''

	return random.randint(1, 100) in range(34, 41)

def gerarPopulacaoInicial(populacao):
	'''
	Esta funcao gera a populacao inicial para 8 individuos de forma aleatoria.
	'''
	global tamPopulacao
	# for para gerar todos os individuos da populacao
	for i in range(tamPopulacao):
		percentagem = 100 #[30, 30, 40]
		aux = []
		# for para os cromossomos do individuo
		'''
		for j in range(0,3):
			valor = random.randint(0, int(percentagem[0]))
			aux.append(valor)
			percentagem[0] -= valor
		for j in range(0,3):
			valor = random.randint(0,percentagem[1])
			aux.append(valor)
			percentagem[1] -= valor
		for j in range(0,3):
			valor = random.randint(0,percentagem[2])
			aux.append(valor)
			percentagem[2] -= valor
		
		if sum(percentagem) > 0:
    		aux.append(sum(percentagem)) # faz isso para dar ao ultimo, o resto da percentagem
		else:
			aux.append(0)
		aux = random.shuffle(aux) # embaralha os valores
		random.shuffle(aux)
		populacao.append(aux)

		'''
		y =  random.randint(6, 9)
		aux = [y for i in range(10)]

		percentagem -= y*10
		for i in range(0,10):
			y = random.randint(0, percentagem)
			aux[i] += y
			percentagem -= y

		if percentagem > 0:
			aux[random.randint(0, 9)] = percentagem
			

		random.shuffle(aux)
		populacao.append(aux)

def buscaGenetico(valor):
	populacao = []
	global numFilhos
	N = numFilhos # Quantidade de filhos gerados a cada iteracao.
	contador = 0
	criterioParada = 0
	melhorGlobal = []
	global dicionario2

	dicionario2 = somaVar() # Soma as variâncias
	print('Iniciando Busca...')
	gerarPopulacaoInicial(populacao)
	while criterioParada < 1000:
		if criterioParada in [i*100 for i in range(10)]:
			print("Concluido -> ", criterioParada/10, "%")
		novaPopulacao = []
		#print( "Populcao: ", populacao, " / tamanho = ", len(populacao))
		for i in range(0, N):
			x = selecao(populacao, valor, dicionario2)
			y = selecao(populacao, valor, dicionario2)
			filho = reproduz(x, y)

			if (pequenaProbabilidadeAleatoria()):
				mutacao(filho)
			novaPopulacao.append(filho)

		populacao = atualizar(populacao, novaPopulacao, valor, dicionario2)

		melhorLocal =  melhorIndividuo(populacao, valor, dicionario2)
		if not melhorGlobal:
			melhorGlobal = list(melhorLocal)

		if localFitness(melhorGlobal, valor, dicionario2) < localFitness(melhorLocal, valor, dicionario2):
			melhorGlobal = list(melhorLocal)
			#print(melhorGlobal, localFitness(melhorGlobal, valor, dicionario2))
		#	contador = 0
		
		#if contador > 40:
		#	gerarPopulacaoInicial(populacao)
		#else:
		#	contador +=1
		criterioParada +=1
		#print(melhorLocal, localFitness(melhorLocal, valor, dicionario2))
		
		plt.plot([criterioParada], [localFitness(melhorLocal, valor, dicionario2)], 'ro')

	plt.title("Algoritmo Genetico: Convergencia")
	plt.xlabel('Geracao')
	plt.ylabel('Valor Fitness')
	plt.savefig("./outputs/convAlgGen.png")
	return melhorGlobal

def buscaProporcao(valor):
	print("Gerando proporcoes de investimentos...")

	proporcoes = buscaGenetico(valor)
	
	#proporcoes = [5, 5, 15, 0, 10, 10, 15, 30, 10, 0]

	saldo = [
			round((proporcoes[0]/100) * valor,2),
			round((proporcoes[1]/100) * valor,2),
			round((proporcoes[2]/100) * valor,2),
			round((proporcoes[3]/100) * valor,2),
			round((proporcoes[4]/100) * valor,2),
			round((proporcoes[5]/100) * valor,2),
			round((proporcoes[6]/100) * valor,2),
			round((proporcoes[7]/100) * valor,2),
			round((proporcoes[8]/100) * valor,2),
			round((proporcoes[9]/100) * valor,2)]

	print(("As proporcoes estipuladas foram:\n"+
			"\tAmbev: R${10} ({0}%)\n" +
			"\tLojas Americanas: R${11} ({1}%)\n" +
			"\tBanco do Brasil: R${12} ({2}%)\n" +
			"\tCielo: R${13} ({3}%)\n" +
			"\tCopel: R${14} ({4}%)\n" +
			"\tNatura: R${15} ({5}%)\n" +
			"\tLojas Renner: R${16} ({6}%)\n" +
			"\tSanepar: R${17} ({7}%)\n" +
			"\tVale: R${18} ({8}%)\n" +
			"\tWeg: R${19} ({9}%)\n").format(
				proporcoes[0], proporcoes[1], proporcoes[2], proporcoes[3], proporcoes[4],
				proporcoes[5], proporcoes[6], proporcoes[7], proporcoes[8], proporcoes[9],
				saldo[0], saldo[1], saldo[2], saldo[3], saldo[4],
				saldo[5], saldo[6], saldo[7], saldo[8], saldo[9],
			)
	)

	return saldo
