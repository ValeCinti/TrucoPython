from random import shuffle

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo
        self.valor_truco = self.asignar_valor_truco(valor, palo)

    def asignar_valor_truco(self, valor, palo):
        jerarquia = {(1, 'Espada'): 14, (1, 'Basto'): 13, (7, 'Espada'): 12, (7, 'Oro'): 11,
                     (3, 'Espada'): 10, (3, 'Basto'): 10, (3, 'Oro'): 10, (3, 'Copa'): 10,
                     (2, 'Espada'): 9, (2, 'Basto'): 9, (2, 'Oro'): 9, (2, 'Copa'): 9,
                     (1, 'Oro'): 8, (1, 'Copa'): 8,
                     (12, 'Espada'): 7, (12, 'Basto'): 7, (12, 'Oro'): 7, (12, 'Copa'): 7,
                     (11, 'Espada'): 6, (11, 'Basto'): 6, (11, 'Oro'): 6, (11, 'Copa'): 6,
                     (10, 'Espada'): 5, (10, 'Basto'): 5, (10, 'Oro'): 5, (10, 'Copa'): 5,
                     (7, 'Basto'): 4, (7, 'Copa'): 4,
                     (6, 'Espada'): 3, (6, 'Basto'): 3, (6, 'Oro'): 3, (6, 'Copa'): 3,
                     (5, 'Espada'): 2, (5, 'Basto'): 2, (5, 'Oro'): 2, (5, 'Copa'): 2,
                     (4, 'Espada'): 1, (4, 'Basto'): 1, (4, 'Oro'): 1, (4, 'Copa'): 1,}
        return jerarquia[valor,palo]

    def __str__(self):
        return f"{self.valor} de {self.palo}"

    def __repr__(self):
        return f"{self.valor} de {self.palo}"

class Mazo:
    def __init__(self):
        palos = ('Espada', 'Basto', 'Oro', 'Copa')
        valores = (1, 2, 3, 4, 5, 6, 7, 10, 11, 12)
        self.cartas = [Carta(valor, palo) for valor in valores for palo in palos]

    def mezclar(self):
        shuffle(self.cartas)

    def repartir(self):
        mano = []
        for i in range(3):
            mano.append(self.cartas[-1])
            self.cartas.pop()
        return mano
