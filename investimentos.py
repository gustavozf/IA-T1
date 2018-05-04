import os, sys, random # bibliotecas que podem vir a ser uteis

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
	print "TESTE: ATUALIZACAO"

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
	pontoDeCorte = random.randint(1, 8)

	return x[:pontoDeCorte] + y[pontoDeCorte:]

def fnFitness():
	'''
	Funcao que mede a adaptacao de um individuo
	'''
	print "TESTE: FITNESS"	

def selecao(populacao):
	'''
	Selecao realizada por torneio.
	Seleciona dois individuos aleatorios da populacao e em seguida,
	retorna o melhor!
	'''	
	
	primSelecionado = random.choice(populacao)
	segunSelecionado = random.choice(populacao)

	if fnFitness(primSelecionado) > fnFitness(segunSelecionado):
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

def buscaGenetico():
	populacao = []
	N = 1 # Quantidade de filhos gerados a cada iteracao.
	criterioParada = True
	
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
	print "A opcao selecionada foi: {0}".format(opcao)
	
	buscaGenetico()