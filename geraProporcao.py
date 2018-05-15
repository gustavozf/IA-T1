import os, sys, random, operator # bibliotecas que podem vir a ser uteis
from math import ceil
from getInputs import get2014and2015
import matplotlib.pyplot as plt

empresas = ["ambev", "americanas", "bancodobrasil", "cielo", "copel", "natura", "renner", "sanepar", "vale", "weg"]
tamPopulacao = 100
numFilhos = 100

def somaVar():
	dicionario = get2014and2015()
	dicVar = {}
	global empresas

	for empresa in empresas:
		dicVar[empresa] = []
		dicVar[empresa].append(sum(dicionario[empresa][0])//493 ) # variancia dos dois anos
		dicVar[empresa].append(sum(dicionario[empresa][:247][0])//247) # variancia de 2015
		dicVar[empresa].append(sum(dicionario[empresa][:124][0])//124) # variancia de metade de 2015
		dicVar[empresa].append(sum(dicionario[empresa][1])//493) # volume de dois anos
		dicVar[empresa].append(sum(dicionario[empresa][:247][1])//247) #volume de 2015
		dicVar[empresa].append(sum(dicionario[empresa][:124][1])//124) # volume de metade de 2015

	return dicVar


def checkSum(lista):
	soma = 0
	for i in lista:
		soma += i

	return soma

def melhorIndividuo(populacao, dicionario):
	'''
	Funcao que retorna o melhor individuo de uma populacao
	'''
	fit = []
	for individuo in populacao:
		fit.append(fnFitness(individuo, dicionario))
	return list(populacao[fit.index(max(fit))])
	# Organizar um dicionario por valor:
	# OBS.: reverese = True --> Deixa a lista em formato decrescente
	# sorted(x.items(), key=operator.itemgetter(1), reverse = True)

def atualizar(populacao, novaPopulacao, dicionario):
	'''
	Funcao que atualiza a populacao antiga com a nova. Elitista.
	'''
	fit = []
	novaPop = []
	for individuo in populacao:
		fit.append(fnFitness(individuo, dicionario))
	for i in range(int(tamPopulacao*0.3)):
		posicao = fit.index(max(fit))
		fit[posicao] = -8000000
		novaPop.append(list(populacao[posicao]))
	#print ("fit =", fit)
	fit = []
	for individuo in novaPopulacao:
		fit.append(fnFitness(individuo, dicionario))
	for i in range(int(tamPopulacao*0.7)):
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
	pontoDeCorte = random.randint(1, 8)

	filho = x[:pontoDeCorte] + y[pontoDeCorte:]

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

def fnFitness(individuo, dicionario):
	'''
	Funcao que mede a adaptacao de um individuo
	'''
	global empresas

	i = 0
	fitness = 0
	for empresa in empresas: #media pondereda, peso 1, 2 e 3 + volume
		'''
		fitness += individuo[i] * ((dicionario[empresa][0]*0.15)+
									(dicionario[empresa][1]*0.2)+
									(dicionario[empresa][2]*0.65))
		
		
		fitness +=( individuo[i] * ((dicionario[empresa][0]+dicionario[empresa][3])*0.16) +  
		individuo[i] * ((dicionario[empresa][1]+dicionario[empresa][4]) * 0.34) + 
		individuo[i] * ((dicionario[empresa][2]+ dicionario[empresa][5])*0.5))
		'''
		fitness +=( (individuo[i]/100) * (
									((dicionario[empresa][0]*0.16)+
									(dicionario[empresa][1]*0.34)+
									(dicionario[empresa][2]*0.5) * 0.95)
									+
									((dicionario[empresa][3]*0.1) + 
									(dicionario[empresa][4]*0.3) + 
									(dicionario[empresa][5]*0.6)*0.05)
									))
		
		
		i += 1

	return round(fitness, 2)

def selecao(populacao, dicionario):
	'''
	Selecao realizada por torneio.
	Seleciona dois individuos aleatorios da populacao e em seguida,
	retorna o melhor!
	'''

	primSelecionado = random.choice(populacao)
	segunSelecionado = random.choice(populacao)

	if (fnFitness(primSelecionado, dicionario) > fnFitness(segunSelecionado, dicionario)):
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
		percentagem = [30, 30, 40]
		aux = []
		# for para os cromossomos do individuo
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
		#aux = random.shuffle(aux) # embaralha os valores
		random.shuffle(aux)
		populacao.append(aux)

def buscaGenetico():
	populacao = []
	global numFilhos
	N = numFilhos # Quantidade de filhos gerados a cada iteracao.
	criterioParada = True
	criterioParada = 0
	melhorGlobal = []

	dicVar = somaVar() # Soma as variâncias
	print('Iniciando Busca...')
	gerarPopulacaoInicial(populacao)
	while criterioParada < 500:
		novaPopulacao = []
		#print( "Populcao: ", populacao, " / tamanho = ", len(populacao))
		for i in range(0, N):
			x = selecao(populacao, dicVar)
			y = selecao(populacao, dicVar)
			filho = reproduz(x, y)

			if (pequenaProbabilidadeAleatoria()):
				mutacao(filho)
			novaPopulacao.append(filho)

		populacao = atualizar(populacao, novaPopulacao, dicVar)

		
		melhorLocal =  melhorIndividuo(populacao, dicVar)
		if not melhorGlobal:
			melhorGlobal = list(melhorLocal)

		if fnFitness(melhorGlobal, dicVar) < fnFitness(melhorLocal, dicVar):
			melhorGlobal = list(melhorLocal)
			criterioParada =0
		else:
			criterioParada +=1
		plt.plot([criterioParada], [fnFitness(melhorLocal,dicVar)], 'r^')

	#plt.show()
	return melhorIndividuo(populacao, dicVar)

def buscaProporcao(valor):
	print("Gerando proporcoes de investimentos...")

	proporcoes = buscaGenetico()
	
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
