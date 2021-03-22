import re

class DataParser:

    # DD/MM/YYYY
    def parse(self, txt):
        return re.findall(r"\b\d{2}/\d{2}/\d{4}\b", txt)
