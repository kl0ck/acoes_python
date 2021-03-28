import sys
import parsers
from rn import RN
from operacao import Operacao
from database import Database
import relatorios

dollar = """
░███████╗
██╔██╔══╝
╚██████╗░  Ações Python
░╚═██╔██╗
███████╔╝
╚══════╝░
"""

print(dollar)

#print(sys.argv)

if len(sys.argv) == 1:
    print("Parâmetro [arquivo] não encontrado.")
    sys.exit(0)

arquivo = sys.argv[1]

print("Lendo arquivo " + arquivo + "...")
print()

lines = None
try:
    f = open(arquivo, "r", encoding="UTF-8")
    lines = f.readlines()
    #print(*lines)
except UnicodeDecodeError:
    f = open(arquivo, "r", encoding="ISO-8859-1")
    lines = f.readlines()
except:
    print("Não foi possível ler o arquivo [" + arquivo + "].")
    sys.exit(0)

print("Extraindo operações...")
print()

dataParser = parsers.DataParser()
tipoOperacaoParser = parsers.TipoOperacaoParser()
numeroParser = parsers.NumeroParser()
tickerParser = parsers.TickerParser()

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

    #print(str(i).zfill(4), line)

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

    operacoes.append(Operacao(None, data, cv, qtd, ticker, preco, ""))

print(operacoes.__len__(), "operações extraídas.")
print()
print("Leitura do arquivo " + arquivo + " concluída.")
print()

rn = RN(operacoes)
relatorio = relatorios.RelatorioPrecoMedio(rn)
relatorio.txt()

print()
print("Fim.")

#C:\Users\Carlos\Desktop\operacoes-2019-2021.txt
