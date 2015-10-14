__author__ = "Cauani Castro"
__copyright__ = "Copyright 2015, Cauani Castro"
__credits__ = ["Cauani Castro"]
__license__ = "Apache License 2.0"
__version__ = "1.0"
__maintainer__ = "Cauani Castro"
__email__ = "cauani.castro@hotmail.com"
__status__ = "Examination program"

#funcao recursiva que acumula o resultado em variavel auxiliar, para melhorar a legibilidade do codigo
def base3Para10(b3, exp, b10):
    if b3 % 10 > 2:
        print("O numero inserido nao esta na base 10!")
        return False
    aux = (b3 % 10)*(3**exp)
    if b3 < 10:
        return b10 + aux
    return base3Para10(b3//10, exp+1, b10+aux)

def main():
    print("Este programa ira receber uma serie de numeros na base 3, e ira converte-lo para a base 10, e imprimir o resultado.")
    print("Caso o usuario entre um numero fora da base 3, o programa ira alertar erro.")
    while True:
        b3 = int(input("Insira um numero na base 3 (Dominio {0, 1, 2}) [digite 0 para sair]\n"))
        if b3 == 0:
            break
        b10 = base3Para10(b3,0,0)
        if b10:
            print("O numero na base 3: %d, convertido para a base 10: %d" % (b3, b10))
    print("\n#####################################")
    print("           FIM DO PROGRAMA")
    print("#####################################")
    return True

if __name__ == '__main__':
    main()