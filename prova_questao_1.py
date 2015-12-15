import os

__author__ = "cauanicastro"
__copyright__ = "Copyright 2015, cauanicastro"
__credits__ = ["Cauani Castro"]
__license__ = "Apache License 2.0"
__version__ = "1.0"
__created_on__ = "15-12-15"
__maintainer__ = "cauanicastro"
__email__ = "cauani.castro@hotmail.com"
__status__ = "Examination program"


def diretorio():
	caminho = os.getcwd()
	return caminho.replace("\\", "/")


def lerArquivo(arquivo):
	caminho = diretorio()
	with open( caminho + "/" + arquivo, 'r') as arquivo:
		return [f.rstrip("\n").split(";") for f in arquivo]


def formataLista(lista):
	nLista = ""
	for i in lista:
		aux = ""
		inicial = True
		for ii in i:
			if inicial:
				inicial = False
				aux += str(ii)
			else:
				aux += ":" + str(ii)
		nLista += aux + "\n"
	return nLista


def imprimeArquivo(arquivo, conteudo):
	caminho = diretorio()
	arq = open(caminho + "/" + arquivo, 'w')
	arq.writelines(conteudo)
	arq.close()


def comparaResposta(r1, r2):
	if r1 == "I" or r2 == "I":
		return 1
	if (r1 == r2):
		return 1
	return 0


def processaListas(rapazes, mocas):
	matrizAfinidade = [[0 for _ in mocas] for _ in rapazes]
	count1 = 0
	for rapaz in rapazes:
		count2 = 0
		for moca in mocas:
			soma = 0
			for resposta in range(len(rapaz)):
				soma += comparaResposta(rapaz[resposta - 1], moca[resposta - 1])
			matrizAfinidade[count1][count2] = soma
			count2 += 1
		count1 += 1
	imprimeArquivo("afinidade.txt", formataLista(matrizAfinidade))
	return matrizAfinidade


def main():
	rapazes = lerArquivo("rapazes.txt")
	mocas = lerArquivo("mocas.txt")
	processaListas(rapazes, mocas)
	return 0


if __name__ == '__main__':
	main()

