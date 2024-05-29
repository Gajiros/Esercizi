class Prodotto:

    def _init_(self, nome: str, quantita: int) -> None:

        self.nome = nome
        self.quantita = quantita
    
class Magazzino:

    def _init_(self) -> None:

        self.prodotti = {}

    def aggiungi_prodotto(self, prodotto: Prodotto) -> None:

        if (prodotto.nome in self.prodotti):

            self.prodotti[prodotto.nome].quantita += prodotto.quantita

        else:

            self.prodotti[prodotto.nome] = prodotto

    def cerca_prodotto(self, nome: str) -> str:

        if (nome in self.prodotti):

            return self.prodotti[nome]
        
        else:

            return None

    def verifica_disponibilita(self, nome: str):

        if (nome in self.prodotti) and (self.prodotti[nome].quantita > 0):

            return True
        
        else:

            return False