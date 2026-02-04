from partida import Partida

def main():
    print("\n----------Truco----------")
    juego = Partida()
    juego.jugar_partida()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProceso interrumpido por el usuario.")