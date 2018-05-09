import os, sys, random # bibliotecas que podem vir a ser uteis
from math import ceil

def checkSum(lista):
	soma = 0
	for i in lista:
		soma += i

	return soma

def melhorIndividuo(populacao):
	'''
	Funcao que retorna o melhor individuo de uma populacao
	'''
	return "TESTE: INDIVIDUO" 

def checkCriterioParada():
	'''
	Verifica se ja esta hapto a parar
	'''
	return False 

def atualizar(populacao, novaPopulacao):
	'''
	Funcao que atualiza a populacao antiga com a nova. Elitista.
	'''
	print( "TESTE: ATUALIZACAO")

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
	
	print( "Filho: ", filho)

	# Verifica se o filho alcancou 100%
	soma = checkSum(filho)
	print('soma: ', soma)

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
	print( "Filho: {0} / Soma: {1}".format(filho, soma))

	return filho

def fnFitness(individuo):
	'''
	Funcao que mede a adaptacao de um individuo
	'''
	print( "TESTE: FITNESS"	)
	return random.randint(1,10)

def selecao(populacao):
	'''
	Selecao realizada por torneio.
	Seleciona dois individuos aleatorios da populacao e em seguida,
	retorna o melhor!
	'''	
	
	primSelecionado = random.choice(populacao)
	segunSelecionado = random.choice(populacao)

	if (fnFitness(primSelecionado) > fnFitness(segunSelecionado)):
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
	# for para gerar todos os individuos da populacao
	for i in range(0,8): 
		percentagem = 100
		aux = []
		# for para os cromossomos do individuo
		for j in range(0,4):
			valor = random.randint(0, int(percentagem/3))
			aux.append(valor)
			percentagem -= valor
		for j in range(0,5):
			valor = random.randint(0,percentagem)
			aux.append(valor)
			percentagem -= valor			
		if percentagem > 0:
			aux.append(percentagem) # faz isso para dar ao ultimo, o resto da percentagem
		else:
			aux.append(0)
		#aux = random.shuffle(aux) # embaralha os valores
		random.shuffle(aux)
		populacao.append(aux)

def buscaGenetico():
	populacao = []
	N = 1 # Quantidade de filhos gerados a cada iteracao.
	criterioParada = True

	gerarPopulacaoInicial(populacao)
	print( "Populcao: ", populacao	)
	while criterioParada:
		novaPopulacao = []

		for i in range(0, N):
			x = selecao(populacao)
			y = selecao(populacao)
			filho = reproduz(x, y)

			if (pequenaProbabilidadeAleatoria()):
				mutacao(filho)	
			novaPopulacao.append(filho)

		atualizar(populacao, novaPopulacao)

		criterioParada = checkCriterioParada()	

	return melhorIndividuo(populacao)
		
def buscaProporcao(opcao):
	print( "A opcao selecionada foi: {0}".format(opcao))
	
	buscaGenetico()
