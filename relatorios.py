from rn import RN
from collections import defaultdict

class RelatorioPrecoMedio:

    rn = None

    def __init__(self, rn):
        self.rn = rn

    def txt(self):
        rn = self.rn
        ativos = rn.ativos()

        mapOperacoes = defaultdict(list)

        for ticker in ativos:
            operacoes = rn.listarOperacoesPorTicker(ticker)        
            
            for o in operacoes:
                mapOperacoes[ticker.upper()].append(o)

        #print("mapOperacoes = " + str(mapOperacoes))

        for ticker in ativos:
            precoMedioCompra = rn.precoMedio(ticker, 'C')
            if precoMedioCompra > 0:
                print(f"Preço médio C {ticker} = {precoMedioCompra}") 

            precoMedioVenda = rn.precoMedio(ticker, 'V')
            if precoMedioVenda > 0:
                print(f"Preço médio V {ticker} = {precoMedioVenda}")

    def pdf(self):
        pass

    def grafico(self):
        pass
