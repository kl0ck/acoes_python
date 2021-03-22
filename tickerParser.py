import re

class TickerParser:

    def parse(self, txt):
        return re.findall(r"\b([A-Za-z]\w*)\b", txt)
