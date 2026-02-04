from partida import Partida
from colorama import init, Fore
init(autoreset=True)

def main():
    print(Fore.YELLOW + "\n----------Truco----------")
    juego = Partida()
    juego.jugar_partida()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProceso interrumpido por el usuario.")