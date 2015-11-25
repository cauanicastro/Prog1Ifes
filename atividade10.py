import random

__author__ = "cauanicastro"
__copyright__ = "Copyright 2015, cauanicastro"
__credits__ = ["Cauani Castro"]
__license__ = "Apache License 2.0"
__version__ = "1.0"
__created_on__ = "15-11-24"
__maintainer__ = "cauanicastro"
__email__ = "cauani.castro@hotmail.com"
__status__ = "Examination program"


def retornaTamanhoLista(lista):
    cont = 0
    for _ in lista:
        cont += 1
    return cont


def retornaIndexLista(lista, elemento):
    cont = 0
    for e in lista:
        if e[0] == elemento:
            return cont
        cont += 1
    return -1


def removeElementoLista(lista, pos):
    cont = 0
    nLista = []
    for e in lista:
        if cont != pos:
            nLista.append(e)
        cont += 1
    return nLista


def calculaFrequencias(lista):
    nLista = []
    for i in lista:
        aux = retornaIndexLista(nLista, i)
        if aux == -1:
            nLista.append([i, 1, (1 / retornaTamanhoLista(lista))])
        else:
            nLista[aux][1] += 1
            nLista[aux][2] = nLista[aux][1] / retornaTamanhoLista(lista)
    return nLista


def ordenaLista(lista, crescente = True):
    if retornaTamanhoLista(lista) == 0:
        return []
    count = 0
    minmax = lista[0]
    index = 0
    for i in lista:
        if crescente and i < minmax or not crescente and i > minmax:
            minmax = i
            index = count
        count += 1
    aux = removeElementoLista(lista, index)
    return [minmax] + ordenaLista(aux, crescente)


def imprimeFrequencias(lista):
    nLista = ordenaLista(calculaFrequencias(lista))
    for e in nLista:
        print("Nota: %.1f, Freq. Absoluta: %d, Freq. Relativa: %.4f" % (e[0], e[1], e[2]))


#Gera uma lista com 80 valores aleatorios, a nota dos alunos, variando entre 0 e 10, com incrementos de 1 decimo
def geraListaAlunos():
    return [(random.randint(0, 100) / 10) for _ in range(80)]


def main():
    print("Este programa ira ler uma lista com notas de 80 alunos diferentes. As notas variam de 0 a 10 e a frequencia absoluta e relativa das notas dos alunos devera ser calculada.")
    print("Para fins de praticidade (e facilitar os testes), ja que nao foi explicitada a forma de gerar tal lista, irei gerar a lista de forma aleatoria.")
    lista = geraListaAlunos()
    print("Lista com as 80 notas:", lista)
    print("------------------------------")
    imprimeFrequencias(lista)
    return 0


if __name__ == '__main__':
    main()