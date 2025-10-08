
from mazo import crear_mazo, repartir_cartas, mostrar_cartas, eliminar_carta_usada, sumar_puntos, mostrar_puntos
from rival import elegir_carta_rival
from truco import comparar_cartas_truco

def jugar_ronda(mano, puntos_jugador, puntos_rival):
    while puntos_jugador < 15 or puntos_rival < 15:
        mano = not mano
        inicia = mano
        num_mano = 0
        resultados_manos = [0]*3
        mazo = crear_mazo()
        cartas_jugador, cartas_rival = repartir_cartas(mazo)
        ronda_finalizada = False
        while ronda_finalizada == False and num_mano < 3:
            resultado = jugar_mano(cartas_jugador, cartas_rival, inicia, num_mano)
            resultados_manos[num_mano] = resultado
            num_mano += 1
            if resultado == 'gana':
                inicia = True
            elif resultado == 'pierde':
                inicia = False
            
            if resultados_manos.count('gana') > 1 or 'emparda' in resultados_manos and 'gana' in resultados_manos or resultados_manos.count('emparda') == 3 and mano:
                puntos_jugador = sumar_puntos(puntos_jugador, 'truco no jugado')
                ronda_finalizada = True
            elif resultados_manos.count('pierde') > 1 or 'emparda' in resultados_manos and 'pierde' in resultados_manos or resultados_manos.count('emparda') == 3 and not mano:
                puntos_rival = sumar_puntos(puntos_rival, 'truco no jugado')
                ronda_finalizada = True
        mostrar_puntos(puntos_jugador, puntos_rival)

def jugar_mano(cartas_jugador, cartas_rival, inicia, num_mano):
    if inicia:
        mostrar_cartas(cartas_jugador, cartas_rival)
        carta_jugador = elegir_carta_jugador(cartas_jugador)
        print(f'\nTiraste {carta_jugador.split()[0]} de {carta_jugador.split()[1]}.')
        
        carta_rival = elegir_carta_rival(carta_jugador,cartas_rival)
        print(f'El rival tira {carta_rival.split()[0]} de {carta_rival.split()[1]}.')
    
    else:
        print()
        mostrar_cartas(cartas_jugador, cartas_rival)
        carta_rival = elegir_carta_rival(False,cartas_rival)
        print(f'\nEl rival tira {carta_rival.split()[0]} de {carta_rival.split()[1]}.')
        
        carta_jugador = elegir_carta_jugador(cartas_jugador)
        print(f'Tiraste {carta_jugador.split()[0]} de {carta_jugador.split()[1]}.')
        
    cartas_jugador = eliminar_carta_usada(cartas_jugador, carta_jugador)
    cartas_rival = eliminar_carta_usada(cartas_rival,carta_rival)    
    resultado = comparar_cartas_truco(carta_jugador,carta_rival)
    return resultado

def elegir_carta_jugador(cartas_jugador):
    while True:
            try:
                opcion_elegida = input('Indice de la carta a tirar: ').lower().strip()
                assert opcion_elegida in ('1','2','3')
                carta_jugador = cartas_jugador[int(opcion_elegida)-1]
                break
            except:
                print('Entrada invalida, intentalo nuevamente.')
    return carta_jugador

def main():
    puntos_jugador = 0
    puntos_rival = 0
    mano = False #Si es True empieza el jugador.
    jugar_ronda(mano, puntos_jugador, puntos_rival)
        
if __name__ == '__main__':
    main()