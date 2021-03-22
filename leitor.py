import sys
from numeroParser import NumeroParser
from tipoOperacaoParser import TipoOperacaoParser
from dataParser import DataParser
from tickerParser import TickerParser
from operacao import Operacao

#print(sys.argv)

if len(sys.argv) == 1:
    print("Parâmetro [arquivo] não encontrado.")
    sys.exit(0)

arquivo = sys.argv[1]

print()
print("Lendo arquivo " + arquivo + "...")
print()

f = open(arquivo, "r", encoding="utf-8")

lines = f.readlines()
#print(*lines)

print("Extraindo operações...\n")

dataParser = DataParser()
tipoOperacaoParser = TipoOperacaoParser()
numeroParser = NumeroParser()
tickerParser = TickerParser()

def isComentario(txt):
    if txt.startswith("#"):
        return True

def isEmBranco(txt):
    if txt.strip() == "":
        return True

operacoes = []
operacoesMap = {}

i = 0

for line in lines:
    # 17/03/2021 C 50 B3SA3 52,68    * Clear
    line = line.strip()
    i+=1

    print(str(i).zfill(3), line)

    if isEmBranco(line):
        continue

    if isComentario(line):
        continue

    a = line.split()

    data = dataParser.parse(a[0])
    cv = tipoOperacaoParser.parse(a[1])
    qtd = numeroParser.parse(a[2])
    ticker = tickerParser.parse(a[3])
    preco = numeroParser.parse(a[4])

    if len(data) == 0:
        print("Data inválida na linha", str(i) + ":", line)
        sys.exit(0)
    if len(cv) == 0:
        print("Tipo de operação inválida na linha", str(i) + ":", line)
        sys.exit(0)
    if len(qtd) == 0:
        print("Quantidade inválida na linha", str(i) + ":", line)
        sys.exit(0)
    if len(ticker) == 0:
        print("Ticker/código inválido na linha", str(i) + ":", line)
        sys.exit(0)
    if len(preco) == 0:
        print("Preço inválido na linha", str(i) + ":", line)
        sys.exit(0)

    operacoes.append(Operacao(data, cv, qtd, ticker, preco))

print()
print("Leitura do arquivo " + arquivo + " concluída.")
print()

print("Operações: ")
print()

for o in operacoes:
    print(o)

print()
