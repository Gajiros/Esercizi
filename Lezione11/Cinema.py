class Film:

    def _init_(self, titolo: str, durata: int) -> None:

        self.titolo = titolo
        self.durata = durata

class Sala:

    def _init_(self, num_sala: int, film: Film, postiT: int) -> None:

        self.num_sala = num_sala
        self.film = film
        self.postiT = postiT
        self.postiP = 0

    def posti_disponibili(self):

        return self.postiT - self.postiP

    def prenota_posti(self, num_posti: int):

        self.num_posti = num_posti
        if (self.num_posti > self.posti_disponibili()):

            print("Posti non disponibili")

        else:

            print(f"{self.num_posti} Posti prenotati")
            self.postiP += self.num_posti
            print(f"Posti disponibili: {self.posti_disponibili()}")

class Cinema:

    def _init_(self)->None:

        self.sale = []

    def aggiungi_sala(self, sala):

        self.sale.append(sala)
    
    def prenota_film(self, titolo_film, num_posti):

        for i in self.sale:

            if (titolo_film == i.film.titolo):

                return i.prenota_posti(num_posti)

film1: Film = Film("Titolo1",90)
film2: Film = Film("Titolo2",100)
film3: Film = Film("Titolo3",110)

sala1: Sala = Sala(1,film1,100)
sala2: Sala = Sala(2,film2,100)
sala3: Sala = Sala(3,film3,100)

cinema: Cinema = Cinema()
cinema.aggiungi_sala(sala1)
cinema.aggiungi_sala(sala2)
cinema.aggiungi_sala(sala3)

cinema.prenota_film("Titolo1",50)
cinema.prenota_film("Titolo1",51)