def main():
#uncomment the program you wish to use
#    print(ReOrder()) #program 1
    print(cofCheck()) #program 2

# Program 1 - Reordering 3 variables without using any auxiliary variable or any kind of loop
def ReOrder():
    print("Este programa ira ordenar 3 variaveis\n")
    a = float(input("Entre com o primeiro numero\n"))
    b = float(input("Entre com o segundo numero\n"))
    if (b > a):
        a = a + b
        b = a - b
        a = a - b
    c = float(input("Entre com o terceiro numero\n"))
    if (c > b):
        b = b + c
        c = b - c
        b = b - c
        if (b > a):
            a = a + b
            b = a - b
            a = a - b
    return "Os numeros (em ordem) sao: %f, %f e %f" % (a, b, c)

# Program 2 - Read 3 floats that will represent the coefficients of a second degree equation
def cofCheck():
    print("Este programa ira montar e resolver uma equacao de segundo ou primeiro grau, no formato: ax^2 + bx + c.\n")
    a = float(input("Entre com o valor de a\n"))
    b = float(input("Entre com o valor de b\n"))
    c = float(input("Entre com o valor de c\n"))
    if a == 0:
        print("Os valores inseridos nao formam uma eq. de segundo grau.\n")
        if b == 0:
            print("Os valores inseridos nao formam uma eq. de primeiro grau.\n")
            return "Nenhuma eq. foi encontrada, retornando o valor de c.\nc = %.2f" % c
        else:
            x = -c / b
            return "Eq. de primeiro grau encontrada.\nx = %.2f" % x
    else:
        delta = (b ** 2) - ((4 * a) * c)
        if delta >= 0:
            root = delta ** (1/2.0)
            x1 = (-b + root) / (2*a)
            x2 = (-b - root) / (2*a)
            return "Raiz real encontrada.\nx'  = %.2f\nx'' = %.2f " % (x1, x2)
        else:
            m = (b*-1)/(2*a)
            n = ((delta*-1) ** (1/2.0))
            x1 = "%.2f + %.2fni" % (m, n)
            x2 = "%.2f - %.2fni" % (m, ((n**2)**(1/2.0)))
            return "Raiz complexa encontrada, retornando a representacao retangular dela.\nx'  = %s\nx'' = %s" % (x1, x2)
main()
