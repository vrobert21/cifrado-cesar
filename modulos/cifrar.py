# Modulo de cifrado de caracteres

"""
-- Este archivo contiene el algoritmo de cifrado. --
"""

from modulos.caracteres import (
    alfabeto_completo,
)  # Importar lista de caracteres personalizados
from modulos.historial import (
    crear_entrada,
)  # Importar función para crear entradas de historial

alfabeto_caracteres = alfabeto_completo  # Variable Global


def cifrar(alfabeto, entrada, desplasamiento):
    """
    Cifra un texto utilizando el cifrado César con un alfabeto personalizado.

    Esta función recorre cada carácter del texto de entrada y lo desplaza
    un número determinado de posiciones dentro del alfabeto proporcionado.
    Los caracteres que no pertenecen al alfabeto se mantienen sin cambios.
    """

    total_caracteres = len(alfabeto) - 1
    salida = ""

    for caracter in entrada:
        if caracter in alfabeto:
            posicion_caracter = alfabeto.index(caracter) + desplasamiento

            if posicion_caracter < total_caracteres:
                salida = salida + alfabeto[posicion_caracter]

            elif posicion_caracter > total_caracteres:
                posicion_caracter = (posicion_caracter - total_caracteres) - 1
                salida = salida + alfabeto[posicion_caracter]

        else:
            salida = salida + caracter

    return salida


def funcion_cifrar():
    """
    Solicita al usuario un texto y un desplazamiento para cifrar el texto utilizando el cifrado César.
    """

    titulo_entrada = "CIFRAR"  # Titulo de la entrada

    try:  # Intenta
        print("\n--- Cifrar Caracteres ---")

        entrada = str(input("Cifrar: "))  # Texto a cifrar.
        desplasamiento = int(
            input("Desplasamiento: ")
        )  # Cuantos lugares en la lista avanzara.

        salida = cifrar(alfabeto_caracteres, entrada, desplasamiento)  # Texto cifrado.

        print(f"Salida: {salida}\n")

        crear_entrada(
            titulo_entrada, entrada, desplasamiento, salida
        )  # Agrega una entada al historial.

    except ValueError:  # En caso de error
        print("\n¡ERROR PARAMETRO NO VALIDO!\n")

    except KeyboardInterrupt:  # En caso de que el usuario interrumpa la ejecución
        print("\n¡Ejecución interrumpida por el usuario!\n")

    except UnboundLocalError:  # En caso de que el usuario interrumpa la ejecución
        print("\n¡Ejecución interrumpida por el usuario!\n")
