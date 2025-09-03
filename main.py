import random
from mazo import crear_mazo, repartir_cartas, mostrar_cartas

def juego_principal():
    mazo = crear_mazo()
    valores_jugador, palos_jugador, valores_rival, palos_rival = repartir_cartas(mazo)
    mostrar_cartas(valores_jugador, palos_jugador, valores_rival, palos_rival)
juego_principal()