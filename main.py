# Archivo principal del programa

from modulos.cifrar import funcion_cifrar
from modulos.descifrar import funcion_descifrar
from modulos.historial import leer_historial


def main():
    while True:
        print("-- CIFRADO CESAR --")
        print("1. Cifrar Caracteres")
        print("2. Descifrar Caracteres")
        print("3. Leer Historial")
        print("4. Terminar Programa\n")

        opcion = input(": ")

        match opcion:
            case "1":
                funcion_cifrar()
            case "2":
                funcion_descifrar()
            case "3":
                leer_historial()
            case "4":
                break
            case _:
                print("-- ¡Opcion no valida! --")


if __name__ == "__main__":
    main()
