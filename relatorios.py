from rn import RN
from collections import defaultdict
from pathlib import Path

class RelatorioPrecoMedio:

    rn = None

    def __init__(self, rn):
        self.rn = rn

    def txt(self):
        rn = self.rn
        ativos = rn.ativos()
        arquivoSaida = "./output/preco_medio.txt"

        Path("./output").mkdir(parents=True, exist_ok=True)
        f = open(arquivoSaida, "w", encoding="utf-8")
        f.truncate(0)

        mapOperacoes = defaultdict(list)

        for ticker in ativos:
            operacoes = rn.listarOperacoesPorTicker(ticker)        
            
            for o in operacoes:
                mapOperacoes[ticker.upper()].append(o)

        #print("mapOperacoes = " + str(mapOperacoes))

        for ticker in ativos:
            precoMedioCompra = rn.precoMedio(ticker, 'C')
            if precoMedioCompra > 0:
                f.write(f"Preço médio C {ticker} = {precoMedioCompra}\n")
                #print(f"Preço médio C {ticker} = {precoMedioCompra}") 

            precoMedioVenda = rn.precoMedio(ticker, 'V')
            if precoMedioVenda > 0:
                f.write(f"Preço médio V {ticker} = {precoMedioVenda}\n")
                #print(f"Preço médio V {ticker} = {precoMedioVenda}")

        f.close()

        print("Relatório gerado: " + arquivoSaida)

    def pdf(self):
        pass

    def grafico(self):
        pass
