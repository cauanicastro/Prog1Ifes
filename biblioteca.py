__author__ = "cauanicastro"
__copyright__ = "Copyright 2016, cauanicastro"
__credits__ = ["Cauani Castro"]
__license__ = "Apache License 2.0"
__version__ = "1.0"
__created_on__ = "16-04-13"
__maintainer__ = "cauanicastro"
__email__ = "cauani.castro@hotmail.com"


def contaPalavras(linha):
    aux = ""
    separadores = ['-']
    palavras = 0
    for letra in linha:
        if letra.isalpha() or (aux and letra in separadores):
            aux += letra
        else:
            if aux:
                palavras += 1
            aux = ""

    if aux:
        palavras += 1
    return palavras

def separaPal(texto):
    lista = []
    #diferentes teclados podem ter diferentes inputs aceitos como "aspas". Incluindo todos eles.
    aspas = ["'", '"', "`"]
    aux = ""
    citacao = False
    for i in texto:
        if not i.isalnum():
            if citacao:
                if i == citacao:
                    aux += i
                    citacao = False
                    lista.append(aux)
                    aux = ""
                else:
                    aux += i
            else:
                if aux:
                    lista.append(aux)
                    aux = ""
                if i in aspas:
                    citacao = i
                    aux = i
        else:
            aux += i
    if aux:
        lista.append(aux)
    return lista

def extraiTokens(texto):
    auxLista = []
    auxToken = ""
    auxTipo = ""
    for l in texto:
        tipo = checaCampo(l)
        if (not tipo) or (auxTipo and tipo != auxTipo):
            if auxToken:
                auxLista.append(auxToken)
                if (not l.isspace()):
                    auxToken = l
                else:
                    auxToken = ""
        else:
            auxToken += l
        auxTipo = tipo
    if auxToken:
        auxLista.append(auxToken)

    return auxLista

'''
def abreArquivoLista(nome):
    arquivo = open(nome, 'rt')
    return [linha.strip() for linha in arquivo]
'''

def abreArquivoLista(nome):
    listRetorno = []
    with open(nome, 'rt') as arquivo:
        aux = arquivo.readline()
        while aux:
            listRetorno.append(aux.strip())
            aux = arquivo.readline()
    return listRetorno or False


def abreListaArquivo(nomes):
    return [open(nome, 'rt') for nome in nomes]


def abreArquivoCallback(nome, callback):
    with open(nome, 'rt') as arquivo:
        return [callback(linha.strip()) for linha in arquivo]


def salvaArquivo(nome, dados):
    with open(nome, 'wt') as arquivo:
        arquivo.write("\n".join(dados))
        return arquivo.close()


def reverteLinha(linha):
    return "".join([l for l in linha[::-1]])


def coparq(nome, novo_nome):
    return salvaArquivo(novo_nome, abreArquivoLista(nome))


def concatarq(arquivos):
    aux = []
    for index in range(len(arquivos)):
        arquivo = arquivos[index]
        if index == len(arquivos) - 1:
            salvaArquivo(arquivo, aux)
            break
        aux.extend(abreArquivoLista(arquivo))
    return True


def interarq(arquivos):
    aux = []
    novaLista = []
    maxEl = 0
    for index in range(len(arquivos)):
        arquivo = arquivos[index]
        if index == len(arquivos) - 1:
            for i in range(maxEl):
                for a in aux:
                    if i >= len(a):
                        continue
                    novaLista.append(a[i])
            salvaArquivo(arquivo, novaLista)
            break
        arquivoAux = abreArquivoLista(arquivo)
        maxEl = maxEl > len(arquivoAux) and maxEl or len(arquivoAux)
        aux.append(abreArquivoLista(arquivo))
    return True


def interarq_noaux(arquivos):
    novaLista = []
    nome_arquivo = arquivos[-1]
    arquivos = abreListaArquivo(arquivos[:-1])
    cont = 0
    while arquivos:
        if cont >= len(arquivos):
            cont = 0
        el = arquivos[cont]
        aux = el.readline()
        if aux:
            novaLista.append(aux.strip())
        else:
            del arquivos[cont]
        cont += 1

    return salvaArquivo(nome_arquivo, novaLista)

def separaPalavraCompara(linha, valor):
    aux = ""
    separadores = ['-']
    palavras = 0
    for letra in linha:
        if letra.isalpha() or (aux and letra in separadores):
            aux += letra
        else:
            if aux and aux == valor:
                palavras += 1
            aux = ""
    if aux and aux == valor:
        palavras += 1
    return palavras

def separaPalavraDicionario(linha, dicionario):
    aux = ""
    separadores = ['-']
    for letra in linha:
        if letra.isalpha() or (aux and letra in separadores):
            aux += letra
        else:
            if aux and len(aux) > 2:
                dicionario[aux] = aux in dicionario and dicionario[aux] + 1 or 1
            aux = ""
    if aux and len(aux) > 2:
        dicionario[aux] = aux in dicionario and dicionario[aux] + 1 or 1
    return dicionario


def geraDicionario(arquivo):
    dicionario = dict()
    with open(arquivo, 'rt') as arq:
        linha = arq.readline()
        while linha:
            aux = separaPalavraDicionario(linha.strip().lower(), dicionario)
            linha = arq.readline()
    return dicionario


def comparaDicionarios(dic1, dic2):
    listaRetorno = []
    for chave in dic1:
        if chave in dic2:
            listaRetorno.append((chave, (dic1[chave] + dic2[chave]) // 2))
    return listaRetorno


def intersec(arquivo1, arquivo2):
    dic1 = geraDicionario(arquivo1)
    dic2 = geraDicionario(arquivo2)
    return comparaDicionarios(dic1,dic2)


def ordenaCrescente(lista):
    nova_lista = []
    for l in lista:
        pos = 0
        for nl in nova_lista:
            if l[1] <= nl[1]:
                break
            pos += 1
        nova_lista.insert(pos, l)
    return nova_lista


def ordenaCrescenteDividirConquistar(lista):
    nova_lista = []
    for l in lista:
        pos = 0
        for nl in nova_lista:
            if l[1] <= nl[1]:
                break
            pos += 1
        nova_lista.insert(pos, l)
    return nova_lista

