import random

def crear_mazo():
    palos = ['espada','oro','basto','copa']
    valores = ['1','2','3','4','5','6','7','10','11','12']
    mazo = [f'{valor} {palo}' for palo in palos for valor in valores]
    random.shuffle(mazo)
    return mazo

def repartir_cartas(mazo):
    valores_jugador, palos_jugador, valores_rival, palos_rival = [], [], [], []
    for x in range(3):
        valores_jugador.append(mazo[len(mazo)-1].split()[0])
        palos_jugador.append(mazo[len(mazo)-1].split()[1])
        mazo.pop()
        valores_rival.append(mazo[len(mazo)-1].split()[0])
        palos_rival.append(mazo[len(mazo)-1].split()[1])
        mazo.pop()
    return valores_jugador, palos_jugador, valores_rival, palos_rival

def mostrar_cartas(valores_jugador, palos_jugador, valores_rival, palos_rival):
    print('Tus cartas:')
    for x in range(len(valores_jugador)):
        print(f'{x+1}: {valores_jugador[x]} de {palos_jugador[x]}')
    print()
    print('Cartas del rival:')
    for x in range(len(valores_rival)):
        print(f'{x+1}: {valores_rival[x]} de {palos_rival[x]}')