import random

def crear_mazo(): #Genera un mazo mezclado aleatoriamente.
    palos = ['espada','oro','basto','copa']
    valores = ['1','2','3','4','5','6','7','10','11','12']
    mazo = [f'{valor} {palo}' for palo in palos for valor in valores]
    random.shuffle(mazo)
    return mazo

def repartir_cartas(mazo): #Reparte 3 cartas a cada jugador.
    cartas_jugador, cartas_rival = [], []
    for x in range(3):
        cartas_jugador.append(mazo[-1])
        mazo.pop()
        cartas_rival.append(mazo[-1])
        mazo.pop()
    return cartas_jugador, cartas_rival

def mostrar_cartas(cartas_jugador, cartas_rival): #Imprime las cartas restantes.
    print('\n-----------')
    print('Tus cartas:')
    for x in range(len(cartas_jugador)):
        print(f'{x+1}: {cartas_jugador[x].split()[0]} de {cartas_jugador[x].split()[1]}')
    print('\nCartas del rival:')
    for x in range(len(cartas_rival)):
        print(f'{x+1}: {cartas_rival[x].split()[0]} de {cartas_rival[x].split()[1]}')
    print('-----------')

def eliminar_carta_usada(cartas, carta_usada): #Elimina la carta usada
    cartas.remove(carta_usada)
    return cartas

def sumar_puntos(puntos,resultado):
    referencia_puntos = {'truco no jugado': 1, 'truco': 2, 'retruco': 3, 'valecuatro': 4,
                         'envido no querido': 1, 'envido': 2, 'realenvido': 3, 'envido envido': 4, 'envido realenvido': 5, 'envido envido realenvido': 7}
    puntos += referencia_puntos[resultado]
    return puntos

def mostrar_puntos(puntos_jugador, puntos_rival):
    print('\n---------')
    print('Puntajes:')
    print(f'Jugador: {puntos_jugador}')
    print(f'Rival: {puntos_rival}')
    print('---------')