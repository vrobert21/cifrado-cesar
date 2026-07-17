# Archivo principal del programa

from modulos.cifrar import funcion_cifrar
from modulos.descifrar import funcion_descifrar


def main():
    while True:
        print("-- CIFRADO CESAR --")
        print("1. cifrar")
        print("2. Descifrar")
        print("3. Terminar programa\n")

        opcion = input(": ")

        match opcion:
            case "1":
                funcion_cifrar()
            case "2":
                funcion_descifrar()
            case "3":
                break
            case _:
                print("-- ¡Opcion no valida! --")


if __name__ == "__main__":
    main()
