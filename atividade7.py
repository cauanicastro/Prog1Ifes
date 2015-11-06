__author__ = "Cauani Castro"
__copyright__ = "Copyright 2015, Cauani Castro"
__credits__ = ["Cauani Castro"]
__license__ = "Apache License 2.0"
__version__ = "1.0"
__maintainer__ = "Cauani Castro"
__email__ = "cauani.castro@hotmail.com"
__status__ = "Examination program"


# Validacao de dados de entrada: fallback com valor padrao caso valor invalido seja inserido pelo usuario
def recebeDados(mensagem, tipo, padrao=0, checaSaida=False):
    odata = input(mensagem)
    try:
        data = tipo(odata)
    except ValueError:
        data = padrao
    if checaSaida is not False:
        if odata == checaSaida:
            return False
    return data


# Retorna a resolucao de uma eq de primeiro grau
def calculaFuncaoPrimeiroGrau(a, b):
    return -b / a


# Retorna as raizes obtidas de uma eq de segundo grau. Distingue raizes reais e complexas
def calculaRaiz(a, b, c):
    d = delta(a, b, c)
    if d >= 0:
        root = d ** (1/2.0)
        x1 = (-b + root) / (2*a)
        x2 = (-b - root) / (2*a)
        return ("Raiz real encontrada.\nx'  = %.2f\nx'' = %.2f " % (x1, x2))
    else:
        m = (b*-1)/(2*a)
        n = ((d*-1) ** (1/2.0))
        x1 = "%.2f + %.2fni" % (m, n)
        x2 = "%.2f - %.2fni" % (m, ((n**2)**(1/2.0)))
        return "Raiz complexa encontrada, retornando a representacao retangular dela.\nx'  = %s\nx'' = %s" % (x1, x2)


# Retorna o valor de delta, para uma eq de segundo grau
def delta(a, b, c):
    return (b ** 2) - ((4 * a) * c)


# Identifica o tipo de funcao atraves dos valores de entrada
def calculaFuncao(a, b, c):
    if a == 0:
        if b == 0:
            return "x = %f" % c
        return "Equacao de primeiro grau encontrada. x = %f" % calculaFuncaoPrimeiroGrau(b, c)
    else:
        return "Equacao de segundo grau encontrada. %s" % calculaRaiz(a, b, c)


# Bloco principal de execucao do programa
def main():
    print("Este programa ira montar e resolver uma equacao de segundo ou primeiro grau, no formato: ax^2 + bx + c.\nPara sair do programa, digite sair no primeiro elemento.")
    while True:
        valor1 = recebeDados("\n\nEntre com o valor de a\n", float, 0, "sair")
        if valor1 is False:
            break
        valor2 = recebeDados("Entre com o valor de b\n", float)
        valor3 = recebeDados("Entre com o valor de c\n", float)
        print(calculaFuncao(valor1, valor2, valor3))
    print("\n\n######################################\nFim do programa.")
    return 1


if __name__ == '__main__':
    main()
