class Documento:
    def __init__(self) -> None:
        self.testo = ''
    
    def getText(self) -> str:
        return self.testo
    
    def setText(self, testo: str):
        self.testo = testo

    def isInText(self, keyword: str) -> bool:
         