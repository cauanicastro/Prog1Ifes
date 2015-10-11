__author__ = 'cauanicastro'
__copyright__ = "Copyright 2015, Cauani Castro"
__credits__ = ["Cauani Castro"]
__license__ = "Apache License 2.0"
__version__ = "1.0"
__maintainer__ = "Cauani Castro"
__email__ = "cauani.castro@hotmail.com"
__status__ = "Examination program"

def calculaRaiz(numero, aproximacoes):
    lst = ""
    raiz = 0
    for i in range(aproximacoes):
        if (i == 0):
            raiz = numero / 2
        else:
            raiz = (raiz**2+numero) / (2 * raiz)
    return "Num = %.5f Aprox = %d Raiz Quadrada = %.10f\n" % (numero, aproximacoes, raiz)

def main():
    print("Este programa ira calcular a raiz quadrada de uma sequencia de numeros positivos, baseado no metodo de aproximacoes sucessivas de newton.")
    print("Para sair do programa digite um numero menor ou igual a zero.")
    while True:
        numero = float(input("Digite um numero (real, positivo) para calcular a sua raiz quadrada:\n"))
        if numero <= 0:
            break
        aproximacoes = int(input("Digite o numero (inteiro) de aproximacoes desejada:\n"))
        print(calculaRaiz(numero, aproximacoes))
    print("\n#####################################")
    print("           FIM DO PROGRAMA")
    print("#####################################")

if __name__ == '__main__':
    main()