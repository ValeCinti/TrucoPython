import random
from truco import obtener_valores_truco

def umbral(u): #Tiene u% de probabilidad de devolver True
    num = random.randint(1,10)
    if u <= num:
        return True
    else:
        return False

def elegir_carta_rival(carta_jugador,cartas_rival): #El bot elige una carta segun le conviene.
    valores_cartas_rival = []
    for carta in cartas_rival:
        valores_cartas_rival.append(obtener_valores_truco(carta))

    if carta_jugador == False: #Si el bot es mano...
        carta_elegida = random.choice(valores_cartas_rival)

    else: #Si el bot es pie...
        valor_carta_jugador = obtener_valores_truco(f'{carta_jugador}')
        
        if max(valores_cartas_rival) > valor_carta_jugador: #Si puede, hace primera.
            carta_elegida = max(valores_cartas_rival)
            for carta in valores_cartas_rival: #Si puede, evita usar la mas alta para hacer primera.
                if carta > valor_carta_jugador and carta < carta_elegida:
                    carta_elegida = carta

        elif max(valores_cartas_rival) < valor_carta_jugador: #Si no puede ganar ni empardar, tira la mas baja.
            carta_elegida = min(valores_cartas_rival)
        
        else: 
            for carta in valores_cartas_rival:
                if carta>8 and carta != max(valores_cartas_rival) and umbral(7): #Tiene 70% de probabilidad de empardar si tiene al menos un 2 ademas de la carta que va a usar y no perdio primera.
                    carta_elegida = max(valores_cartas_rival)
                elif carta>7 and carta != max(valores_cartas_rival) and umbral(5): #Tiene 50% de probabilidad de empardar si tiene al menos un 12 ademas de la carta que va a usar y no perdio primera.
                    carta_elegida = max(valores_cartas_rival)
                else:
                    carta_elegida = min(valores_cartas_rival)
    
    return cartas_rival[valores_cartas_rival.index(carta_elegida)]