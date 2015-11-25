import sys
import random

__author__ = "cauanicastro"
__copyright__ = "Copyright 2015, cauanicastro"
__credits__ = ["Cauani Castro"]
__license__ = "Apache License 2.0"
__version__ = "1.0"
__created_on__ = "15-11-25"
__maintainer__ = "cauanicastro"
__email__ = "cauani.castro@hotmail.com"
__status__ = "Examination program"


def retornaTamanhoLista(lista):
    cont = 0
    for _ in lista:
        cont += 1
    return cont


def calculaRespostas(lista):
    resp = [[0 for _ in range(5)] for e in range(10)]
    for e in lista:
        count = 0
        for ei in e[-10:]:
            resp[count][int(ei) - 1] = resp[count][int(ei) - 1] + 1
            count += 1
    return resp


def geraListaCenso(n):
    pessoas = ["Joao", "Ze", "Jurema", "Biscoito", "Arroz", "Manteiga", "Macau", "Joel", "Ma", "Ximba", "Egeu", "Gago", "Faca", "Porco", "Ea", "Zuco", "Muco", "Uco", "Tuco", "Hotdog", "Mapplesyrup"]
    sobrenomes = ["", "", "Marcos", "Filho", "Sebastiao", "Fragoso", "Fragado", "Feijo", "Pindamonhangaba", "Ukulele", "Snow", "Da Silva", "Sauro", "Amoeba", "Massa"]
    return ["%s %s %s, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d" % (random.sample(pessoas, 1)[0], random.sample(sobrenomes, 1)[0], random.sample(sobrenomes, 1)[0], random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5)) for _ in range(n)]


def criarCSV(arquivo):
    with open(arquivo, 'w') as f:
        f.write('\n'.join(geraListaCenso(220)))


def lerArquivo(arquivo):
    return [e.split(', ') for e in [l.rstrip('\n') for l in open(arquivo)]]


def imprimeQuestionario(lista):
    for p in range(retornaTamanhoLista(lista)):
        print("\nPergunta de numero %d ---" % p)
        for v in range(retornaTamanhoLista(lista[p])):
            print("Opcao %d foi selecionada por %d pessoas" % (v, lista[p][v]))


def main():
    print("Este programa ira gerar um arquivo csv com 220 entradas de nomes de pessoas e suas respectivas respostas, de 1 a 5, para 10 perguntas distintas. Logo apos ele ira carregar este mesmo arquivo e contabilizar a quantidade de respostas para cada alternativa por questao. Para deixar de gerar uma nova lista, comente a proxima linha no codigo.")
    criarCSV('atividade11.txt')
    lista = lerArquivo('atividade11.txt')
    print("\nLista com as perguntas e seus respectivos valores:\n", lista)
    print("-----------------------------\n")
    imprimeQuestionario(calculaRespostas(lista))
    return 0


if __name__ == '__main__':
    main()