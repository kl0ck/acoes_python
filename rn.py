from database import Database
import converters

class RN:

    db = None

    def __init__(self, operacoes):
        self.db = Database()
        for o in operacoes:
            self.db.add(o)

    def precoMedio(self, ticker, cv):
        db = self.db
        l = db.listarPorTicker(ticker)

        somatorio = 0

        for o in l:
            if (o.isCompra() and cv.upper() == 'C'):
                somatorio += converters.toDecimal(o.preco)
                print(o)
            elif (o.isVenda() and cv.upper() == 'V'):
                somatorio += converters.toDecimal(o.preco)
                print(o)
        
        return round(somatorio / l.__len__(), 2)
