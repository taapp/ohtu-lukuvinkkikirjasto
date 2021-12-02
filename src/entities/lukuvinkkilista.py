class Lukuvinkkilista:
    def __init__(self):
        self.lista = []

    def lisaa(self, lukuvinkki):
        self.lista.append(lukuvinkki)

    def listaa(self):
        for lukuvinkki in self.lista:
            print(lukuvinkki)