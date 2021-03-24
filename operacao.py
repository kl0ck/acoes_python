class Operacao:

    def __init__(self, data, cv, qtd, ticker, preco, nota):
        self.data = data if isinstance(data, str) else data[0]
        self.cv = cv if isinstance(cv, str) else cv[0]
        self.qtd = qtd if isinstance(qtd, str) else qtd[0]
        self.ticker = ticker if isinstance(ticker, str) else ticker[0]
        self.preco = preco if isinstance(preco, str) else preco[0]
        self.nota = nota if isinstance(nota, str) else nota[0]

    def __str__(self):
        return str(self.data) + " " + str(self.cv) + " " + str(self.qtd) + " " + str(self.ticker) + " " + str(self.preco) + " " + str(self.nota)
