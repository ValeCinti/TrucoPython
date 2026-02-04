from random import choice
from utilidades import tirar_dado

class Jugador:
    def __init__(self):
        self.puntos = 0
    
    def recibir_cartas(self, mazo):
        self.cartas = []
        self.cartas = mazo.repartir()
    
    def jugar_carta(self, carta_jugada):
        self.cartas.remove(carta_jugada)

class Rival(Jugador):
    def elegir_carta(self, carta_jugador):
        if carta_jugador == False: #Si el bot es mano
            carta_elegida = choice(self.cartas)

        else: #Si el bot es pie
            cartas_ganan, cartas_empardan, cartas_pierden = [], [], []
            for carta in self.cartas:
                if carta.valor_truco > carta_jugador.valor_truco:
                    cartas_ganan.append(carta)
                elif carta.valor_truco == carta_jugador.valor_truco:
                    cartas_empardan.append(carta)
                else:
                    cartas_pierden.append(carta)

            if len(cartas_ganan) > 0:
                carta_elegida = cartas_ganan[0] #Si puede, hace primera.
                for carta in cartas_ganan:
                    if carta.valor_truco < carta_elegida.valor_truco: #Intenta usar la mas baja que aun gane.
                        carta_elegida = carta
                print(f"Puedo ganar. Voy a jugar un {carta_elegida}.")

            elif len(cartas_empardan) > 0:
                carta_elegida = cartas_empardan[0]
                cartas_restantes = []
                for carta in self.cartas:
                    if carta != carta_elegida:
                        cartas_restantes.append(carta)
                match len(cartas_restantes):
                    case 0:
                        decision_empardar = True
                        print(f"No me queda otra que empardar. Voy a jugar un {carta_elegida}.")
                    case 1:
                        mejor_restante = cartas_restantes[0]
                    case 2:
                        mejor_restante = cartas_restantes[0].valor_truco if cartas_restantes[0].valor_truco > cartas_restantes[1].valor_truco else cartas_restantes[1].valor_truco
                probabilidad = mejor_restante * 0.07
                decision_empardar = tirar_dado(probabilidad)
                
                if not decision_empardar:
                    for carta in cartas_restantes:
                        if carta.valor_truco < carta_elegida.valor_truco:
                            carta_elegida = carta
                    print(f"Decidi no empardar ({probabilidad*100})%. Tiro la mas bajita. Voy a jugar un {carta_elegida}.")
                else:
                    print(print(f"Decidi empardar ({probabilidad*100}%). Voy a jugar un {carta_elegida}."))

            else:
                carta_elegida = self.cartas[0]
                for carta in self.cartas:
                    if carta.valor_truco < carta_elegida.valor_truco:
                        carta_elegida = carta
                print(f"No puedo ganar ni empardar. Voy a jugar un {carta_elegida}.")

        return carta_elegida