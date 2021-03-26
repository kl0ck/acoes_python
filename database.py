# https://docs.python.org/3/library/sqlite3.html
import sqlite3
import converters

class Database:

    con = sqlite3.connect(':memory:')

    def __init__(self):
        con = self.con
        c = con.cursor()

        c.execute("CREATE TABLE operacao (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT, cv TEXT, qtd TEXT, ticker TEXT, preco TEXT, nota TEXT)")

        con.commit()

    def addOperacao(self, operacao):
        con = self.con
        c = con.cursor()

        p = operacao.data, operacao.cv, operacao.qtd, operacao.ticker, operacao.preco, operacao.nota
        c.execute("INSERT INTO operacao (data, cv, qtd, ticker, preco, nota) VALUES (?, ?, ?, ?, ?, ?)", p)

        con.commit()

    def listarOperacoes(self) -> list:
        con = self.con
        c = con.cursor()

        c.execute("SELECT * FROM operacao")

        rows = c.fetchall()

        i = 0
        for r in rows:
            rows[i] = converters.toOperacao(r)
            i+=1

        return rows

    def listarOperacoesPorTicker(self, ticker) -> list:
        con = self.con
        c = con.cursor()

        c.execute("SELECT * FROM operacao WHERE ticker = ?", (ticker,))

        rows = c.fetchall()

        i = 0
        for r in rows:
            rows[i] = converters.toOperacao(r)
            i+=1

        return rows
