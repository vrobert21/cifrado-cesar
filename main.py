# Archivo principal del programa

from modules.cifrar import funcion_cifrar  # Importa la función cifrar
from modules.descifrar import funcion_descifrar  # Importa la función descifrar
from modules.historial import (
    leer_historial,
)  # Importa la funnción que muestra el historial


def main():
    """
    Función principal que implementa el menú interactivo del programa Cifrado César.

    Esta función ejecuta un bucle infinito que muestra un menú con las opciones
    disponibles (cifrar, descifrar, leer historial y salir), procesa la selección
    del usuario y ejecuta la función correspondiente. El programa continúa
    ejecutándose hasta que el usuario selecciona la opción de salir.
    """

    while True:
        print("-- CIFRADO CESAR --")
        print("1. Cifrar Caracteres")
        print("2. Descifrar Caracteres")
        print("3. Leer Historial")
        print("4. Terminar Programa\n")

        try:
            opcion = input(": ")

        except KeyboardInterrupt:  # En caso de que el usuario interrumpa la ejecución
            print("\n¡Ejecución interrumpida por el usuario!")
            break

        except UnboundLocalError: # En caso de que el usuario interrumpa la ejecución
            print("\n¡Ejecución interrumpida por el usuario!")
            break

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
                print("-- ¡Opción no valida! --\n")


if __name__ == "__main__":
    main()
