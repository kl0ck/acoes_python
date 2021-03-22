import re

class NumeroParser:

    def parse(self, txt):
        return re.findall(r"\b(\d*\,*\d+)\b", txt)
