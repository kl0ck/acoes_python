from operacao import Operacao
from decimal import Decimal

def toOperacao(tuple):
    return Operacao(tuple[0], tuple[1], tuple[2], tuple[3], tuple[4], tuple[5], tuple[6])

def toDateYMD(dataDMY):
    a = str(dataDMY).split('/')
    y = a[2]
    m = a[1]
    d = a[0]
    return y + '-' + m + '-' + d

def toDecimal(str):
    if (',' in str and '.' in str):
        raise Exception("Número inválido: [" + str + "]. Use vírgula para decimais.")
    str = str.replace(',', '.')
    return Decimal(str)

#print(toDateYMD("23/01/2021"))
#print(toNumber("1.024,68"))
