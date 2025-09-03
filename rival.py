import random
from truco import obtener_valores_truco

def elegir_carta(carta_jugador,valores_rival,palos_rival):
    valor_truco_carta_jugador = obtener_valores_truco(f'{carta_jugador}')
    cartas_rival, valores_truco_cartas_rival = [], []
    for x in range(len(valores_rival)):
        cartas_rival.append(f'{str(valores_rival[x])} {str(palos_rival[x])}')
        valores_truco_cartas_rival.append(obtener_valores_truco(cartas_rival[x]))
    print(cartas_rival)
    print(valores_truco_cartas_rival)
    if max(valores_truco_cartas_rival) > valor_truco_carta_jugador:
        valor_carta_elegida = max(valores_truco_cartas_rival)
        return cartas_rival[valores_truco_cartas_rival.index(valor_carta_elegida)]