from mazo import Mazo
from jugadores import Rival, Jugador
from utilidades import elegir_opcion

class Partida:
    def jugar_partida(self):
        jugador = Jugador()
        rival = Rival()
        self.jugador_es_mano = False
        while jugador.puntos < 15 or rival.puntos < 15:
            self.jugador_es_mano = not self.jugador_es_mano
            ronda = Ronda(jugador, rival, self.jugador_es_mano)
            ronda.jugar_ronda(jugador, rival)

class Ronda:
    def __init__(self, jugador, rival, jugador_es_mano):
        mazo = Mazo()
        mazo.mezclar()
        jugador.recibir_cartas(mazo)
        rival.recibir_cartas(mazo)
        self.mano_actual = 0
        self.jugador_empieza = jugador_es_mano
    
    def jugar_ronda(self, jugador, rival):
        print("\n---Comienza una nueva ronda---\n")
        while self.mano_actual<3:
            self.mano_actual += 1
            print("Tus cartas:")
            for indice, carta in enumerate(jugador.cartas, start=1):
                print(f"{indice}. {carta}")
            print("\nCartas del Rival:")
            for indice, carta in enumerate(rival.cartas, start=1):
                print(f"{indice}. {carta}")
            
            match self.jugador_empieza:
                case True:
                    eleccion = elegir_opcion(jugador.cartas,self.mano_actual)
                    jugador.carta_jugada = jugador.cartas[eleccion-1]
                    jugador.jugar_carta(jugador.carta_jugada)
                    print(f"Jugaste {jugador.carta_jugada}.")
                    
                    rival.carta_jugada = rival.elegir_carta(jugador.carta_jugada)
                    rival.jugar_carta(rival.carta_jugada)
                    print(f"El Rival juega {rival.carta_jugada}.\n")
                    
                case False: 
                    rival.carta_jugada = rival.elegir_carta(False)
                    rival.jugar_carta(rival.carta_jugada)
                    print(f"\nEl Rival juega {rival.carta_jugada}.\n")
                    
                    eleccion = elegir_opcion(jugador.cartas,self.mano_actual)
                    jugador.carta_jugada = jugador.cartas[eleccion-1]
                    jugador.jugar_carta(jugador.carta_jugada)
                    print(f"Jugaste {jugador.carta_jugada}.\n")