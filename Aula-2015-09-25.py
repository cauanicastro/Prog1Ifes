def main():
    #print(ReOrder()) #program 1
    print(cofCheck()) #program 2

# Program 1 - Reordering 3 variables without using any auxiliary variable
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
    a = float(input("Entre com o valor de a\n"))
    b = float(input("Entre com o valor de b\n"))
    c = float(input("Entre com o valor de c\n"))
    if a == 0:
        return "Os valores inseridos nao formam uma eq. de segundo grau"
    else:
        delta = (b ** 2) - ((4 * a) * c)
        print("delta -> %f" % delta)
        if delta >= 0:
            x1 = (-b + (delta ** (1/2))) / 2 * a
            x2 = (-b - (delta ** (1/2))) / 2 * a
            return "Raiz real encontrada.1" \
                   "\nx' = %f\nx'' = %f " % (x1, x2)
        else:
            m = (b*-1)/(2*a)
            n = ((delta*-1) ** (1/2))
            x1 = "%f + %fni" % (m, n)
            x2 = "%f - %fni" % (m, ((n**2)**(1/2)))
            return "Raiz complexa encontrada, retornando a representacao retangular dela.\nx' = %s\nx''= %s" % (x1, x2)
main()
