__author__ = "Cauani Castro"
__copyright__ = "Copyright 2015, Cauani Castro"
__credits__ = ["Cauani Castro"]
__license__ = "Apache License 2.0"
__version__ = "1.0"
__maintainer__ = "Cauani Castro"
__email__ = "cauani.castro@hotmail.com"
__status__ = "Examination program"

def ExibeEstatisticas():
    print("##################################")
    print("         REPORT DA FABRICA")
    print("##################################")
    print("Lista de operarios:\n")
    print(listaOperarios)
    print("A folha mensal de pagamento da fabrica e de: R$ %.2f" % totalFolhaPagamento)
    print("A fabricacao mensal foi de %d pecas" % totalPecasFabricadas)
    if operariosHomensA > 0:
        aux = pecasFabricadasHomemA / operariosHomensA
        print("A media de fabricacao de pecas pelos homens da classe A foi de %.2f pecas" % aux)
    if operariosHomensB > 0:
        aux = pecasFabricadasHomemB / operariosHomensB
        print("A media de fabricacao de pecas pelos homens da classe B foi de %.2f pecas" % aux)
    if operariosHomensC > 0:
        aux = pecasFabricadasHomemC / operariosHomensC
        print("A media de fabricacao de pecas pelos homens da classe C foi de %.2f pecas" % aux)
    if operariosMulherA > 0:
        aux = pecasFabricadasMulherA / operariosMulherA
        print("A media de fabricacao de pecas pelas mulheres da classe A foi de %.2f pecas" % aux)
    if operariosMulherB > 0:
        aux = pecasFabricadasMulherB / operariosMulherB
        print("A media de fabricacao de pecas pelas mulheres da classe B foi de %.2f pecas" % aux)
    if operariosMulherC > 0:
        aux = pecasFabricadasMulherC / operariosMulherC
        print("A media de fabricacao de pecas pelas mulheres da classe C foi de %.2f pecas" % aux)
    print("O operario de maior salario foi o operario de numero %d, com um salario de R$ %.2f" % (operarioMaiorSalarioNumero, operarioMaiorSalario))

    return True


def ProcessaOperario(numero, pecas, sexo):
    #declaracao de uso de variaveis globais
    global listaOperarios
    global totalFolhaPagamento
    global totalPecasFabricadas
    global operariosHomensA
    global operariosHomensB
    global operariosHomensC
    global operariosMulherA
    global operariosMulherB
    global operariosMulherC
    global pecasFabricadasHomemA
    global pecasFabricadasHomemB
    global pecasFabricadasHomemC
    global pecasFabricadasMulherA
    global pecasFabricadasMulherB
    global pecasFabricadasMulherC
    global operarioMaiorSalario
    global operarioMaiorSalarioNumero
    global salarioMinimo

    #calcula salario e classe
    salario = salarioMinimo
    classe = "A"
    if pecas > 30 and pecas <= 35:
        salario += (pecas - 30) + ((3 * salarioMinimo) / 100.00)
        classe = "B"
    elif pecas > 35:
        salario += (pecas - 30) + ((5 * salarioMinimo) / 100.00)
        classe = "C"

    #atualiza lista e total de pg e pecas fabricadas
    listaOperarios += "Operario %d - R$ %.2f\n" % (numero, salario)
    totalFolhaPagamento += salario
    totalPecasFabricadas += pecas

    #verifica maior salario
    if operarioMaiorSalario <= salario:
        operarioMaiorSalarioNumero = numero
        operarioMaiorSalario = salario

    #atualiza lista de pecas por sexo e classe
    if classe == "A":
        if (sexo == "m" or sexo == "M"):
            operariosHomensA += 1
            pecasFabricadasHomemA += pecas
        else:
            operariosMulherA += 1
            pecasFabricadasMulherA += pecas
    elif classe == "B":
        if (sexo == "m" or sexo == "M"):
            operariosHomensB += 1
            pecasFabricadasHomemB += pecas
        else:
            operariosMulherB += 1
            pecasFabricadasMulherB += pecas
    elif classe == "C":
        if (sexo == "m" or sexo == "M"):
            operariosHomensC += 1
            pecasFabricadasHomemC += pecas
        else:
            operariosMulherC += 1
            pecasFabricadasMulherC += pecas
    #fim
    return True


def main():
    print("Este programa ira ler uma lista de funcionarios e imprimir os dados em seguida.")
    print("Entre com os dados do funcionario conforme solicitado. Para sair do modo de insercao de funcionarios e exibir os dados, digite 0 para o numero do operario")

    while True:
        numero = int(input("Entre com o numero do operario (ex.: 001)\n"))
        if numero == 0:
            break
        pecas = int(input("Entre com o numero de pecas fabricada pelo operario (ex.: 32)\n"))
        sexo = " "
        sexo = input("Entre com o sexo do operario (M ou F) \n")
        ProcessaOperario(numero, pecas, sexo)
    ExibeEstatisticas()
    return True

#Declaracao de variaveis
salarioMinimo = 2000.00
listaOperarios = ""
totalFolhaPagamento = 0
totalPecasFabricadas = 0
operariosHomensA = 0
operariosHomensB = 0
operariosHomensC = 0
operariosMulherA = 0
operariosMulherB = 0
operariosMulherC = 0
pecasFabricadasHomemA = 0
pecasFabricadasHomemB = 0
pecasFabricadasHomemC = 0
pecasFabricadasMulherA = 0
pecasFabricadasMulherB = 0
pecasFabricadasMulherC = 0
operarioMaiorSalario = 0
operarioMaiorSalarioNumero = 0

if __name__ == '__main__':
    main()
