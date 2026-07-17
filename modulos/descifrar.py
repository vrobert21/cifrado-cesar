# Modulo de Descifrado.

"""
-- Este archivo contiene el modulo de descifrado. --
"""

from modulos.caracteres import alfabeto_completo


def descifrar(alfabeto, entrada, desplasamiento):
    """
    Esta funcion se encarga de cifrar los caracteres

    - Obtiene el numero de caracteres del alfabeto
    - Decaramos una variable de salida

    - Si uno de los caracteres de entrada esta dentro de la lista de carcateres
        - Iteramos sofre el string de entrada
        - Obtenemos su posicion en el alfabeto y le restamos el numero de desplazamiento

        - Si la posicion es menor al total de caracteres del alfabeto
            - Sumamos ese caracter a la variable de salida

        - Si la posicion es mayor al total de caracteres del alfabeto
            - Le restamos el total de caracteres del alfabeto y la posicion
              para que quede su equivalente del lado contrario de la lista
            - Y sumamos ese caracter a la variable de salida

        - Si el caracter no esta dentro del alfabeto simplemente se suma a la variable de salida

    - Retornamos la variable de salida
    """

    total_caracteres = len(alfabeto) - 1
    salida = ""

    for caracter in entrada:
        if caracter in alfabeto:
            posicion_caracter = alfabeto.index(caracter) - desplasamiento

            if posicion_caracter < total_caracteres:
                salida = salida + alfabeto[posicion_caracter]

            elif posicion_caracter > total_caracteres:
                posicion_caracter = posicion_caracter - total_caracteres
                salida = salida + alfabeto[posicion_caracter]

        else:
            salida = salida + caracter

    return salida


alfabeto_caracteres = alfabeto_completo


def funcion_descifrar():
    try:
        print("\n--- Descifrar Caracteres ---")
        entrada = str(input("Descifrar: "))
        desplasamiento = int(input("Desplasamiento: "))
        salida = descifrar(alfabeto_caracteres, entrada, desplasamiento)
        print(f"Salida: {salida}\n")

    except ValueError:
        print("¡ERROR PARAMETRO NO VALIDO!\n")
