import random

__author__ = "Cauani Castro"
__copyright__ = "Copyright 2015, Cauani Castro"
__credits__ = ["Cauani Castro"]
__license__ = "Apache License 2.0"
__version__ = "1.0"
__created_on__ = "15-11-24"
__maintainer__ = "Cauani Castro"
__email__ = "cauani.castro@hotmail.com"
__status__ = "Examination program"


# Caso n possa usar funcoes basicas de listas, retorna o tamanho da lista
def retornaTamanhoLista(lista):
    cont = 0
    for e in lista:
        cont += 1
    return cont


# Caso n possa usar funcoes basicas de listas, remove um unico elemento da lista. Caso tenha mais de um, remove o primeiro encontrado (esquerda-direita)
def removeElementoLista(lista, pos):
    cont = 0
    nLista = []
    for e in lista:
        if cont != pos:
            nLista.append(e)
        cont += 1
    return nLista


# Caso n possa usar funcoes basicas de listas, retorna o index de um elemento da lista. Caso tenha mais de um, retorna o index do primeiro encontrado (esquerda-direita)
def retornaIndexLista(lista, elemento):
    cont = 0
    for e in lista:
        if e == elemento:
            return cont
        cont += 1


# Retorna uma lista com a quantidade de elementos duplicados encontrada e a lista como ultimo elemento (prolog-style recursion pattern)
def removeDuplicados(lista, elemento):
    aux = removeElementoLista(lista, retornaIndexLista(lista, elemento))
    if aux == lista:
        return [lista]
    return [1] + removeDuplicados(aux, elemento)


# Caso n possa usar funcoes basicas de listas, ordena a lista
def ordenaLista(lista, crescente = True):
    if retornaTamanhoLista(lista) == 0:
        return []
    minmax = lista[0]
    index = 0
    for i in lista:
        if crescente and i < minmax or not crescente and i > minmax:
            minmax = i
            index = retornaIndexLista(lista, minmax)
    aux = removeDuplicados(lista, minmax)
    auxCount = retornaTamanhoLista(aux)
    if auxCount > 2:
        print("O numero %d se repete %d vezes" % (minmax, auxCount - 1))
    return [minmax] + ordenaLista(aux[auxCount - 1], crescente)


def recebeDados(A):
    n = input("Entre com a quantidade de valores desejada (entre 0 e 1000). Entre -1 para sair.\n")
    if n == "-1":
        return False
    n = int(n)
    if n >= 0 and n <= 1000:
        return A[:n]
    return recebeDados(A)


def main():
    print("Este programa ira gerar uma lista com (0 <= n <= 1000) valores do vetor A (que contem mil elementos aleatorios, de 1 a 100) e:\n Ordenar esta lista de forma crescente;\n Remover as duplicatas (indicando quantas foram encontradas, para cada elemento);\n Imprimir a nova lista gerada, sem as duplicatas.")
    A = [random.randint(0, 100) for _ in range(1000)]
    while True:
        lista = recebeDados(A)
        if not lista:
            break
        print("\nO conjunto original e:", lista)
        print("O conjunto ordenado e sem duplicatas e:", ordenaLista(lista))
        print("\n\n")
    print("\n\n######################################\nFim do programa.")
    return 1


if __name__ == '__main__':
    main()
