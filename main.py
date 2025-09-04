
from mazo import crear_mazo, repartir_cartas, mostrar_cartas, eliminar_carta_usada
from rival import elegir_carta

def main(mano):
    mazo = crear_mazo()
    valores_jugador, palos_jugador, valores_rival, palos_rival = repartir_cartas(mazo)
    mostrar_cartas(valores_jugador, palos_jugador, valores_rival, palos_rival)
    ronda = 0
    mano = not mano
    jugar_ronda(valores_jugador,palos_jugador,valores_rival,palos_rival,ronda,mano)

def jugar_ronda(valores_jugador,palos_jugador,valores_rival,palos_rival,ronda,mano):
    ronda += 1
    ronda_finalizada = False
    while mano == True:
        while ronda_finalizada == False:
            carta_elegida = int(input('Numero de la carta a tirar: '))
            while carta_elegida < 1 or carta_elegida > 3:
                carta_elegida = int(input('Error. Numero de la carta a tirar: '))
            
            carta_jugador = str(f'{valores_jugador[carta_elegida-1]} {palos_jugador[carta_elegida-1]}')
            print(f'Tiraste {carta_jugador.split()[0]} de {carta_jugador.split()[1]}.')
            
            carta_rival = elegir_carta(carta_jugador,valores_rival,palos_rival)
            print(f'El rival tira {carta_rival}.')

            valores_jugador, palos_jugador = eliminar_carta_usada(valores_jugador,palos_jugador,carta_jugador)
            valores_rival, palos_rival = eliminar_carta_usada(valores_rival,palos_rival,carta_rival)
            mostrar_cartas(valores_jugador, palos_jugador, valores_rival, palos_rival)


if __name__ == '__main__':
    mano = False #Si es True empieza el jugador.
    main(mano)