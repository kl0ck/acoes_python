import re

class TipoOperacaoParser:

    # C/V
    def parse(self, txt):
        return re.findall(r"\b(C|V)\b", txt)
