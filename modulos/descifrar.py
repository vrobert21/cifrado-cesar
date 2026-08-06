# Modulo de Descifrado.

"""
-- Este archivo contiene el modulo de descifrado. --
"""

from modulos.caracteres import (alfabeto_completo,)  # Importar lista de caracteres personalizados
from modulos.historial import (crear_entrada,)  # Importar función para crear entradas de historial


alfabeto_caracteres = alfabeto_completo  # Variable Global


def descifrar(alfabeto, entrada, desplasamiento):
    """
    Descifra un texto previamente cifrado con el cifrado César utilizando un alfabeto personalizado.

    Esta función es la operación inversa de `cifrar()`. Recorre cada carácter del texto
    de entrada y lo desplaza hacia atrás un número determinado de posiciones dentro del
    alfabeto proporcionado. Los caracteres que no pertenecen al alfabeto se mantienen
    sin cambios.
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


def funcion_descifrar():
    """
    Interfaz de usuario para descifrar texto utilizando el cifrado César.
    """

    titulo_entrada = "DESCIFRAR"  # Titulo de la entrada

    try:  # Intenta
        print("\n--- Descifrar Caracteres ---")

        entrada = str(input("Descifrar: "))  # Texto a descifrar
        desplasamiento = int(
            input("Desplasamiento: ")
        )  # Cuantos lugares en la lista avanzara.

        salida = descifrar(
            alfabeto_caracteres, entrada, desplasamiento
        )  # Texto descifrado.

        print(f"Salida: {salida}\n")

        crear_entrada(
            titulo_entrada, entrada, desplasamiento, salida
        )  # Agrega una entada al historial.

    except ValueError:  # En caro de error
        print("¡ERROR PARAMETRO NO VALIDO!\n")
