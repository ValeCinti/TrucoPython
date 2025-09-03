
from mazo import crear_mazo, repartir_cartas, mostrar_cartas
from rival import elegir_carta

ronda = 0
mano = False

def juego_principal(ronda,mano):
    mazo = crear_mazo()
    valores_jugador, palos_jugador, valores_rival, palos_rival = repartir_cartas(mazo)
    mostrar_cartas(valores_jugador, palos_jugador, valores_rival, palos_rival)
    ronda += 1
    mano = not mano
    if mano == True:
        carta_elegida = int(input('Numero de la carta a tirar: '))
        while carta_elegida < 1 or carta_elegida > 3:
            carta_elegida = int(input('Error. Numero de la carta a tirar: '))
        carta_jugador = str(f'{valores_jugador[carta_elegida-1]} {palos_jugador[carta_elegida-1]}')
        print(f'Tiraste {carta_jugador.split()[0]} de {carta_jugador.split()[1]}.')
        carta_rival = elegir_carta(carta_jugador,valores_rival,palos_rival)
        print(f'El rival tira {carta_rival}')




juego_principal(ronda,mano)