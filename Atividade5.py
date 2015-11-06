__author__ = "Cauani Castro"
__copyright__ = "Copyright 2015, Cauani Castro"
__credits__ = ["Cauani Castro"]
__license__ = "Apache License 2.0"
__version__ = "1.0"
__maintainer__ = "Cauani Castro"
__email__ = "cauani.castro@hotmail.com"
__status__ = "Examination program"


def f(x):
    #funcao definida na questao
    return 1/(1+(x**2))


def calculaPi(n):
    #n e a quantidade de trapezios
    a = 0. #intervalo inferior
    b = 1. #intervalo superior
    h = (b-a)/n #altura dos trapezios
    Area = 0

    for i in range(n):
        if i == 0:
            #caso especial da regra para y0
            Area += f(a)/2
        elif i == n:
            #caso especial da regra para yn
            Area += f(b)/2
        else:
            #regra padrao
            Area += f(a + (i*h))
    Area = Area * h
    return "Para %d trapezios, a aproximacao de pi e = %f" % (n, 4.0*Area)


def main():
    print("Este programa ira calcular um valor aproximado de pi, baseado na quantidade de trapezios desejada, utilizando para tal a lei dos trapezoides.")
    print("Fonte de referencia utilizada para o aprendizado da lei dos trapezoides: http://www.intmath.com/integration/5-trapezoidal-rule.php")
    while True:
        n = int(input("Entre com a quantidade desejada de trapezios para efetuar o calculo (digite 0 para sair do programa):\n"))
        if n == 0:
            break
        print(calculaPi(n))

    print("\n#####################################")
    print("           FIM DO PROGRAMA")
    print("#####################################")
    return True


if __name__ == '__main__':
    main()
