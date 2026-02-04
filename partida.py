from mazo import Mazo
from jugadores import Rival, Jugador
from utilidades import elegir_opcion
from colorama import init, Fore
init(autoreset=True)

class Partida:
    def jugar_partida(self):
        jugador = Jugador()
        rival = Rival()
        self.jugador_es_mano = False
        while jugador.puntos < 15 and rival.puntos < 15:
            self.jugador_es_mano = not self.jugador_es_mano
            print(Fore.YELLOW+"Puntos Jugador:",jugador.puntos)
            print(Fore.YELLOW+"Puntos Rival:",rival.puntos)
            ronda = Ronda(jugador, rival, self.jugador_es_mano)
            ronda.jugar_ronda(jugador, rival, self.jugador_es_mano)

class Ronda:
    def __init__(self, jugador, rival, jugador_es_mano):
        mazo = Mazo()
        mazo.mezclar()
        jugador.recibir_cartas(mazo)
        rival.recibir_cartas(mazo)
        self.estado_truco = [1, None]  # [cantidad de puntos a sumar , True = ganado/False = Perdido]
        self.estado_envido = [0, None] # [cantidad de puntos a sumar , True = ganado/False = Perdido]
        self.mano_actual = 0
        self.manos_ganadas = ['primera', 'segunda', 'tercera'] #None = Parda, True = Ganada, False = Perdida
        self.jugador_empieza = jugador_es_mano
    
    def jugar_ronda(self, jugador, rival, jugador_es_mano):
        print(Fore.YELLOW+"\n---Comienza una nueva ronda---\n")
        
        while self.mano_actual<3 and self.estado_truco[1] == None:
            print(Fore.BLUE+"Tus cartas:")
            for indice, carta in enumerate(jugador.cartas, start=1):
                print(Fore.BLUE+f"{indice}. {carta}")
            print(Fore.RED+"\nCartas del Rival:")
            for indice, carta in enumerate(rival.cartas, start=1):
                print(Fore.RED+f"{indice}. {carta}")
            
            self.mano_actual += 1
            if self.mano_actual > 1 and self.manos_ganadas[self.mano_actual-2] != None:
                self.jugador_empieza = self.manos_ganadas[self.mano_actual-2]
            else:
                self.jugador_empieza = jugador_es_mano
            
            match self.jugador_empieza:
                case True:
                    eleccion = elegir_opcion(jugador.cartas,self.mano_actual)
                    jugador.carta_jugada = jugador.cartas[eleccion-1]
                    jugador.jugar_carta(jugador.carta_jugada)
                    print(Fore.GREEN+f"Jugaste {jugador.carta_jugada}.")
                    
                    rival.carta_jugada = rival.elegir_carta(jugador.carta_jugada)
                    rival.jugar_carta(rival.carta_jugada)
                    print(Fore.GREEN+f"El Rival juega {rival.carta_jugada}.\n")
                    
                case False:
                    rival.carta_jugada = rival.elegir_carta(False)
                    rival.jugar_carta(rival.carta_jugada)
                    print(Fore.GREEN+f"\nEl Rival juega {rival.carta_jugada}.")
                    
                    eleccion = elegir_opcion(jugador.cartas, self.mano_actual)
                    jugador.carta_jugada = jugador.cartas[eleccion-1]
                    jugador.jugar_carta(jugador.carta_jugada)
                    print(Fore.GREEN+f"Jugaste {jugador.carta_jugada}.\n")
            
            self.decidir_ganador_mano(jugador.carta_jugada, rival.carta_jugada) 
            self.decidir_ganador_truco(jugador_es_mano)
            print(self.manos_ganadas,'\n')
        self.sumar_puntos(jugador, rival)
    
    def decidir_ganador_mano(self, carta_jugador, carta_rival):
        self.manos_ganadas[self.mano_actual-1] = carta_jugador.valor_truco > carta_rival.valor_truco if carta_jugador.valor_truco != carta_rival.valor_truco else None

    def decidir_ganador_truco(self, jugador_es_mano):
        if self.manos_ganadas.count(True) > 1 or self.manos_ganadas[0] == None and self.manos_ganadas[1] == True or self.manos_ganadas[0] == None and self.manos_ganadas[1] == None and self.manos_ganadas[2] == True or self.manos_ganadas.count(None) == 3 and jugador_es_mano or self.manos_ganadas[0] == True and None in self.manos_ganadas:
            self.estado_truco[1] = True
        elif self.manos_ganadas.count(False) > 1 or self.manos_ganadas[0] == None and self.manos_ganadas[1] == False or self.manos_ganadas[0] == None and self.manos_ganadas[1] == None and self.manos_ganadas[2] == False or self.manos_ganadas.count(None) == 3 and not jugador_es_mano or self.manos_ganadas[0] == False and None in self.manos_ganadas:
            self.estado_truco[1] = False
        
    def sumar_puntos(self, jugador, rival):
        match self.estado_envido[1]:
            case True:
                jugador.puntos += self.estado_envido[0]
            case False:
                rival.puntos += self.estado_envido[0]
        
        match self.estado_truco[1]:
            case True:
                jugador.puntos += self.estado_truco[0]
            case False:
                rival.puntos += self.estado_truco[0]