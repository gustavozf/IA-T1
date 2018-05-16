from getInputs import *
import statistics
from metodos import *

empresas = ["ambev", "americanas", "bancodobrasil", "cielo", "copel", "natura", "renner", "sanepar", "vale", "weg"]


def somaVar():
	dicionario = get2014and2015()
	dicVar = {}

	for empresa in empresas:
		dicVar[empresa] = []
		tam = len(dicionario[empresa])
		for i in range(2):
			for j in [1,2,4]:
				dp = sum([dicionario[empresa][x][i] for x in range(tam//j)])/(tam//j)
				#valor = statistics.pstdev([i/sum(dp) for i in dp])
				valor = dp 
				dicVar[empresa].append(valor)

		#dicVar[empresa].append(sum([dicionario[empresa][x][0] for x in range(tam)])/ tam ) # variancia dos dois anos
		#dicVar[empresa].append(sum([dicionario[empresa][x][0] for x in range(tam//2)])/ (tam//2)) # variancia de 2015
		#dicVar[empresa].append(sum([dicionario[empresa][x][0] for x in range(tam//4)])/ (tam//4) ) # variancia de metade de 2015
		#dicVar[empresa].append(sum([dicionario[empresa][x][1] for x in range(tam)])/ tam) # valor de dois anos
		#dicVar[empresa].append(sum([dicionario[empresa][x][1] for x in range(tam//2)])/ (tam//2)) # valor de 2015
		#dicVar[empresa].append(sum([dicionario[empresa][x][1] for x in range(tam//4)])/ (tam//4)) # valor de metade de 2015
		#dicVar[empresa].append(sum([dicionario[empresa][x][2] for x in range(tam)])/ tam) # valor de dois anos
		#dicVar[empresa].append(sum([dicionario[empresa][x][2] for x in range(tam//2)])/ (tam//2)) # valor de 2015
		#dicVar[empresa].append(sum([dicionario[empresa][x][2] for x in range(tam//4)])/ (tam//4)) # valor de metade de 2015
		
	#print(dicVar)

	return dict(dicVar)

def fnFitness(individuo, valor, dicionario2):
	'''
	Funcao que mede a adaptacao de um individuo
	'''
	global empresas

	i = 0
	fitness = 0

	'''
	valorSimbolico = valor
	disponivel = {}
	for empresa in empresas:
		disponivel[empresa] = valorSimbolico * individuo[i]/100
		i+=1

	#x = sum([maxMM(0, 493, disponivel, dicionario2)*0.16 , 
	#		 maxMM(0, 247, disponivel, dicionario2) * 0.34, 
	#		 maxMM(0, 146, disponivel, dicionario2)*0.5])
	#x = maxMM(0, 493, disponivel, dicionario2)
	#y = sum([maxMM(247, 493, disponivel)*0.35, maxMM(0, 247, disponivel) *0.65])
	#print(x, y)
	
	fitness += individuo[i] * ((dicionario[empresa][0]*0.15)+
								(dicionario[empresa][1]*0.2)+
								(dicionario[empresa][2]*0.65))


	fitness += individuo[i] * ((dicionario[empresa][0]*0.15)+
								(dicionario[empresa][1]*0.2)+
								(dicionario[empresa][2]*0.65))


	fitness +=( individuo[i] * ((dicionario[empresa][0]+dicionario[empresa][3])*0.16) +  
	individuo[i] * ((dicionario[empresa][1]+dicionario[empresa][4]) * 0.34) + 
	individuo[i] * ((dicionario[empresa][2]+ dicionario[empresa][5])*0.5))
	'''	
	for empresa in empresas: #media pondereda, peso 1, 2 e 3 + volume	
		fitness += (individuo[i]/100) * (
									((dicionario2[empresa][0] *0.16)+
									(dicionario2[empresa][1]  *0.34)+
									(dicionario2[empresa][2] *0.5))*0.3
									+
									((dicionario2[empresa][3]*0.16) + 
									(dicionario2[empresa][4]*0.34) + 
									(dicionario2[empresa][5] *0.5))*0.7
									)

		i += 1
	
	for i in individuo:
		if not i in range(7, 30):
			fitness -= 10
	
	#fitness = x #max(x, y)
	return round(fitness,2)

def maxMM(inicio, fim, disponivel, dicionario2):
    return max(MME(inicio, fim, disponivel, dicionario2), 
			   MMS(inicio, fim, disponivel, dicionario2), 
			   MMC(inicio, fim, disponivel, dicionario2))
	
def MME(inicio, fim, disp, dicionario2):
	historico = {}
	disponivel = dict(disp)

	cotacoes = compraPrimeiroDia(inicio + 18, disponivel, dicionario2, historico)
	for dia in range(inicio+18, fim):
		for empresa in empresas:
			hoje = dicionario2[empresa][dia]
			mediaLonga = mme(dia, 18, empresa, dicionario2)
			mediaCurta = mme(dia, 4, empresa, dicionario2)
			if (mediaLonga > hoje): #vende
				if (historico[empresa] < hoje) and (cotacoes[empresa] > 0):
					venda(dia, empresa, dicionario2, disponivel, cotacoes)
			elif(mediaLonga < hoje): #compra
				compra(dia, empresa, dicionario2, disponivel, cotacoes, historico)
	vendeUltimoDia(dicionario2, disponivel, cotacoes)
	return sum(disponivel.values())

def MMS(inicio, fim, disp, dicionario2):
	historico = {}
	disponivel = dict(disp)

	cotacoes = compraPrimeiroDia(inicio + 18, disponivel, dicionario2, historico)
	for dia in range(inicio+18, fim):
		for empresa in empresas:
			somaDias = sum(dicionario2[empresa][dia-18:dia+1])/18
			hoje = dicionario2[empresa][dia]
			if (hoje < somaDias): #vende
				if (historico[empresa] < hoje) and (cotacoes[empresa] > 0):
					venda(dia, empresa, dicionario2, disponivel, cotacoes)
			elif(hoje > somaDias): #compra
				compra(dia, empresa, dicionario2, disponivel, cotacoes, historico)
	vendeUltimoDia(dicionario2, disponivel, cotacoes)
	return sum(disponivel.values())

def MMC(inicio, fim, disp, dicionario2):
	historico = {}
	disponivel = dict(disp)

	cotacoes = compraPrimeiroDia(inicio + 18, disponivel, dicionario2, historico)
	for dia in range(inicio+18, fim):
		for empresa in empresas:
			mediaLonga = sum(dicionario2[empresa][dia-18:dia+1])/18
			mediaCurta = sum(dicionario2[empresa][dia-4:dia+1])/4
			if (mediaLonga > mediaCurta): #vende
				hoje = dicionario2[empresa][dia]
				if (historico[empresa] < hoje) and (cotacoes[empresa] > 0):
					venda(dia, empresa, dicionario2, disponivel, cotacoes)
			elif(mediaLonga < mediaCurta): #compra
				compra(dia, empresa, dicionario2, disponivel, cotacoes, historico)
	vendeUltimoDia(dicionario2, disponivel, cotacoes)
	return sum(disponivel.values())