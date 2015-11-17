__author__ = "Cauani Castro"
__copyright__ = "Copyright 2015, Cauani Castro"
__credits__ = ["Cauani Castro"]
__license__ = "Apache License 2.0"
__version__ = "1.0"
__maintainer__ = "Cauani Castro"
__email__ = "cauani.castro@hotmail.com"
__status__ = "Examination program"


def calculaDados(sx, sy, sxy, sx2, sy2, n):
    return calculaA(sx, sy, sxy, sx2, n), calculaB(sx, sy, sxy, sx2, n), calculaR(sx, sy, sxy, sx2, sy2, n)


def calculaR(sx, sy, sxy, sx2, sy2, n):
    return ((n * sxy) - (sx * sy)) / ((((n * sx2) - (sx**2))**(1/2)) * (((n * sy2) - (sy**2))**(1/2)))


def calculaB(sx, sy, sxy, sx2, n):
    return (sy * sx2 - sx * sxy) / ((n * sx2) - (sx**2))


def calculaA(sx, sy, sxy, sx2, n):
    return ((n * sxy) - (sx * sy)) / ((n * sx2) - (sx**2))


def calculaSomatorios(x, y, sx, sy, sxy, sx2, sy2):
    return sx + x, sy + y, sxy + (x*y), sx2 + x**2, sy2 + y**2


def leXY(lista):
    somaX, somaY, somaXY, somaX2, somaY2, n = 0.0, 0.0, 0.0, 0.0, 0.0, 0
    for v in lista:
        if v == "":
            break
        aux = v.split(";")
        x = float(aux[0])
        y = float(aux[1])
        somaX, somaY, somaXY, somaX2, somaY2 = calculaSomatorios(x, y, somaX, somaY, somaXY, somaX2, somaY2)
        n += 1
    return somaX, somaY, somaXY, somaX2, somaY2, n


def lerArquivo(arquivo):
    return [l.rstrip('\n') for l in open(arquivo)]


def main():
    somaX, somaY, somaXY, somaX2, somaY2, n = leXY(lerArquivo("RegressaoLinear.txt"))
    a, b, r = calculaDados(somaX, somaY, somaXY, somaX2, somaY2, n)
    print("a = %.4f, b = %.4f, r = %.4f" % (a, b, r))
    return 0

if __name__ == '__main__':
    main()
