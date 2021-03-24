import re

class DataParser:

    # DD/MM/YYYY
    def parse(self, txt):
        return re.findall(r"\b\d{2}/\d{2}/\d{4}\b", txt)

class TickerParser:

    def parse(self, txt):
        return re.findall(r"\b([A-Za-z]\w*)\b", txt)

class TipoOperacaoParser:

    # C/V
    def parse(self, txt):
        return re.findall(r"\b(C|V)\b", txt)

class NumeroParser:

    def parse(self, txt):
        return re.findall(r"\b(\d*\,*\d+)\b", txt)
