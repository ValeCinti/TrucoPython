valores_truco = {'4 espada': 1, '4 oro': 1, '4 basto': 1, '4 copa': 1,
                 '5 espada': 2, '5 oro': 2, '5 basto': 2, '5 copa': 2,
                 '6 espada': 3, '6 oro': 3, '6 basto': 3, '6 copa': 3,
                 '7 espada': 12, '7 oro': 11, '7 basto': 4, '7 copa': 4,
                 '10 espada': 5, '10 oro': 5, '10 basto': 5, '10 copa': 5,
                 '11 espada': 6, '11 oro': 6, '11 basto': 6, '11 copa': 6,
                 '12 espada': 7, '12 oro': 7, '12 basto': 7, '12 copa': 7,
                 '2 espada': 9, '2 oro': 9, '2 basto': 9, '2 copa': 9,
                 '3 espada': 10, '3 oro': 10, '3 basto': 10, '3 copa': 10,
                 '1 espada': 14, '1 oro': 8, '1 basto': 13, '1 copa': 8}

def obtener_valores_truco(carta): #Devuelve el valor asociado a la carta.
    valor_truco_carta = valores_truco[carta]
    return valor_truco_carta

def comparar_cartas_truco(carta_jugador, carta_rival): #Devuelve True si gana la mano, False si la pierde, o None si emparda.
    if obtener_valores_truco(carta_jugador) > obtener_valores_truco(carta_rival):
        return 'gana'
    elif obtener_valores_truco(carta_jugador) < obtener_valores_truco(carta_rival):
        return 'pierde'
    else:
        return 'emparda'