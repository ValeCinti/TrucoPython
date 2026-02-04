from random import random

def elegir_opcion(cartas, mano_actual):
    while True:
        if mano_actual == 1:
            opciones = ['envido', 'real envido', 'falta envido']
        try:
            eleccion = input("\nÍndice de la carta a jugar: ").lower().strip()
            if eleccion.isnumeric():
                eleccion = int(eleccion)
                if eleccion < 1 or eleccion > len(cartas):
                    raise IndexError
            else:
                if eleccion not in opciones:
                    raise IndexError
            break
        except IndexError:
            print("Entrada invalida. Intente nuevamente.")
    return eleccion

def tirar_dado(prob): #Tiene (100 * prob)% de probabilidad de devolver True
    if prob >= random():
        return True
    else:
        return False