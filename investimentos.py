import os, sys, random # bibliotecas que podem vir a ser uteis

def melhorIndividuo(populacao):
	'''
	Funcao que retorna o melhor individuo de uma populacao
	'''
	return "TESTE: INDIVIDUO" 

def checkCriterioParada():
	'''
	Funcao que atualiza a populacao antiga com a nova. Elitista.
	'''
	return False 

def atualizar(populacao, novaPopulacao):
	'''
	Funcao que atualiza a populacao antiga com a nova. Elitista.
	'''
	print "TESTE: ATUALIZACAO"

def mutacao(filho):
	'''
	Funcao que muta um individuo
	'''
	print "TESTE: MUTACAO"

def reproduz(x, y):
	'''
	Reproduz um filho de "x" e "y"
	'''
	print "TESTE: REPRODUCAO"	

def fnFitness():
	'''
	Funcao que mede a adaptacao de um individuo
	'''
	print "TESTE: FITNESS"	

def selecao(populacao):
	'''
	Selecao realizada por torneio ou roleta
	'''
	print "TESTE: SELECAO"	
	fnFitness()

def pequenaProbabilidadeAleatoria():
	'''
	Eh sorteado um numero aleatorio entre 1 e 100.
	Se este estiver presente entre 34 - 41, eh retornado True.
	Caso contrario, False
	'''
	print "TESTE: pequenaProbabilidadeAleatoria"	
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
				filho = mutacao(filho)

			novaPopulacao.append(filho)
		
		atualizar(populacao, novaPopulacao)
		
		criterioParada = checkCriterioParada()

	return melhorIndividuo(populacao)
		
def buscaProporcao(opcao):
	print "A opcao selecionada foi: {0}".format(opcao)
	
	buscaGenetico()
