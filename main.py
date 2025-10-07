
from mazo import crear_mazo, repartir_cartas, mostrar_cartas, eliminar_carta_usada
from rival import elegir_carta_rival
from truco import comparar_cartas_truco

def jugar_ronda(mano):
    mano = not mano
    num_mano = 0
    resultados_manos = [0]*3
    mazo = crear_mazo()
    cartas_jugador, cartas_rival = repartir_cartas(mazo)
    ronda_finalizada = False
    while ronda_finalizada == False and num_mano < 3:
        resultado = jugar_mano(cartas_jugador, cartas_rival, mano, num_mano)
        resultados_manos[num_mano] = resultado
        num_mano += 1
        if resultados_manos.count('gana') > 1 or 'emparda' in resultados_manos and 'gana' in resultados_manos or resultados_manos.count('emparda') == 3 and mano:
            print('Gana el jugador.')
            ronda_finalizada = True
        elif resultados_manos.count('pierde') > 1 or 'emparda' in resultados_manos and 'pierde' in resultados_manos or resultados_manos.count('emparda') == 3 and not mano:
            print('Gana el rival.')
            ronda_finalizada = True

def jugar_mano(cartas_jugador, cartas_rival, mano, num_mano):
    if mano:
        mostrar_cartas(cartas_jugador, cartas_rival)
        carta_jugador = elegir_carta_jugador(cartas_jugador)
        print(f'\nTiraste {carta_jugador.split()[0]} de {carta_jugador.split()[1]}.')
        
        carta_rival = elegir_carta_rival(carta_jugador,cartas_rival)
        print(f'El rival tira {carta_rival.split()[0]} de {carta_rival.split()[1]}.')
    
    else:
        mostrar_cartas(cartas_jugador, cartas_rival)
        carta_rival = elegir_carta_rival(False,cartas_rival)
        print(f'El rival tira {carta_rival.split()[0]} de {carta_rival.split()[1]}.')
        
        carta_jugador = elegir_carta_jugador(cartas_jugador)
        print(f'\nTiraste {carta_jugador.split()[0]} de {carta_jugador.split()[1]}.')
        
    cartas_jugador = eliminar_carta_usada(cartas_jugador, carta_jugador)
    cartas_rival = eliminar_carta_usada(cartas_rival,carta_rival)    
    resultado = comparar_cartas_truco(carta_jugador,carta_rival)
    return resultado

def elegir_carta_jugador(cartas_jugador):
    while True:
            try:
                opcion_elegida = input('\nIndice de la carta a tirar: ').lower().strip()
                assert opcion_elegida in ('1','2','3')
                carta_jugador = cartas_jugador[int(opcion_elegida)-1]
                break
            except:
                print('Entrada invalida, intentalo nuevamente.')
    return carta_jugador

def main():
    mano = False #Si es True empieza el jugador.
    jugar_ronda(mano)
        
if __name__ == '__main__':
    main()