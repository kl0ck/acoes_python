from database import Database
from collections import defaultdict
import converters

class RN:

    db = None

    def __init__(self, operacoes):
        self.db = Database()
        for o in operacoes:
            self.db.addOperacao(o)

    # Preço médio de compra ou de venda de um ativo.
    def precoMedio(self, ticker, cv) -> float:
        db = self.db
        l = db.listarOperacoesPorTicker(ticker)

        somatorio = 0

        for o in l:
            if (o.isCompra() and cv.upper() == 'C'):
                somatorio += converters.toDecimal(o.preco)
                print(o)
            elif (o.isVenda() and cv.upper() == 'V'):
                somatorio += converters.toDecimal(o.preco)
                print(o)
        
        return round(somatorio / l.__len__(), 2)

    def listarOperacoes(self) -> list:
        return self.db.listarOperacoes()

    def listarOperacoesPorTicker(self, ticker) -> list:
        return self.db.listarOperacoesPorTicker(ticker)

    # Lista todos os ativos existentes nas operações.
    def ativos(self) -> list:
        operacoes = self.listarOperacoes()
        myset = set()

        for o in operacoes:
            myset.add(o.ticker)

        sortedList = list(myset)
        sortedList.sort()
        
        return sortedList

    # Lista todas as operações feitas com um ativo.
    def operacoes(self, ticker):
        pass
        #operacoes = self.listarOperacoes()
        #map = defaultdict(list)
        #for o in operacoes:
        #    map[ticker.upper()].append(o)
        

    # Saldo do ativo (quantidade em carteira).
    def saldo(self, ticker):
        pass
