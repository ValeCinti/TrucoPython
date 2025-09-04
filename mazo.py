import random

def crear_mazo(): #Genera un mazo mezclado aleatoriamente.
    palos = ['espada','oro','basto','copa']
    valores = ['1','2','3','4','5','6','7','10','11','12']
    mazo = [f'{valor} {palo}' for palo in palos for valor in valores]
    random.shuffle(mazo)
    return mazo

def repartir_cartas(mazo): #Reparte 3 cartas a cada jugador.
    valores_jugador, palos_jugador, valores_rival, palos_rival = [], [], [], []
    for x in range(3):
        valores_jugador.append(mazo[len(mazo)-1].split()[0])
        palos_jugador.append(mazo[len(mazo)-1].split()[1])
        mazo.pop()
        valores_rival.append(mazo[len(mazo)-1].split()[0])
        palos_rival.append(mazo[len(mazo)-1].split()[1])
        mazo.pop()
    return valores_jugador, palos_jugador, valores_rival, palos_rival

def mostrar_cartas(valores_jugador, palos_jugador, valores_rival, palos_rival): #Imprime las cartas restantes.
    print('Tus cartas:')
    for x in range(len(valores_jugador)):
        print(f'{x+1}: {valores_jugador[x]} de {palos_jugador[x]}')
    print()
    print('Cartas del rival:')
    for x in range(len(valores_rival)):
        print(f'{x+1}: {valores_rival[x]} de {palos_rival[x]}')

def eliminar_carta_usada(valores,palos,carta): #Elimina la carta tirada
    
    for x in range(len(valores)-1):
        if (f'{valores[x]} {palos[x]}') == carta:
            valores.pop(x)
            palos.pop(x)
    
    return valores, palos