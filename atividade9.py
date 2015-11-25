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


# Remove todos os elementos el de uma lista
def removeElementosLista(lista, el):
    nLista = []
    for e in lista:
        if e != el:
            nLista.append(e)
    return nLista


# Caso n possa usar funcoes basicas de listas, remove um elemento da lista na posicao pos.
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


# Caso n possa usar funcoes basicas de listas, ordena a lista
def ordenaListaSemDuplicados(lista, crescente = True):
    if retornaTamanhoLista(lista) == 0:
        return []
    minmax = lista[0]
    vezesEncontrado = 0
    for i in lista:
        if crescente and i <= minmax or not crescente and i >= minmax:
            if i != minmax:
                minmax = i
                vezesEncontrado = 1
            else:
                vezesEncontrado += 1
    aux = removeElementosLista(lista, minmax)
    if vezesEncontrado > 1:
        print("O numero %d se repete %d vezes" % (minmax, vezesEncontrado))
    return [minmax] + ordenaListaSemDuplicados(aux, crescente)


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
        print("O conjunto ordenado e sem duplicatas e:", ordenaListaSemDuplicados(lista))
        print("\n\n")
    print("\n\n######################################\nFim do programa.")
    return 1


if __name__ == '__main__':
    main()
