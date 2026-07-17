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

    Parameters
    ----------
    alfabeto : str o list
        Conjunto de caracteres válidos para el cifrado. Debe ser una secuencia
        ordenada donde cada índice representa la posición del carácter.
    entrada : str
        Texto que se desea cifrar. Puede contener caracteres que no estén
        en el alfabeto, los cuales se conservarán tal cual.
    desplasamiento : int
        Número de posiciones que se desplazará cada carácter en el alfabeto.
        Puede ser positivo (desplazamiento hacia adelante) o negativo
        (desplazamiento hacia atrás).

    Returns
    -------
    str
        Texto cifrado resultante. Los caracteres del alfabeto serán reemplazados
        por sus correspondientes desplazados, y los caracteres no pertenecientes
        al alfabeto permanecerán inalterados.

    Notes
    -----
    - El desplazamiento aplica de forma circular: si se supera el final del
      alfabeto, continúa desde el principio (y viceversa para desplazamientos
      negativos).
    - La función asume que el alfabeto no contiene caracteres duplicados.
    - La búsqueda de la posición de cada carácter se realiza mediante el
      método `index()`, por lo que la complejidad es O(n*m) donde n es la
      longitud de la entrada y m es la longitud del alfabeto.

    Examples
    --------
    >>> alfabeto = "abcdefghijklmnopqrstuvwxyz"
    >>> cifrar(alfabeto, "hola", 3)
    'krod'

    >>> cifrar(alfabeto, "zapato", 1)
    'abqbup'

    >>> cifrar(alfabeto, "hola mundo", 3)
    'krod pxqgr'

    >>> # Con caracteres no alfabéticos
    >>> cifrar(alfabeto, "hola123", 3)
    'krod123'

    >>> # Con desplazamiento negativo
    >>> cifrar(alfabeto, "krod", -3)
    'hola'
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

    Esta función interactúa con el usuario a través de la consola para:
    1. Pedir un texto a cifrar.
    2. Pedir un número de desplazamiento (entero).
    3. Aplicar la función `cifrar()` utilizando el alfabeto de caracteres predefinido.
    4. Mostrar el texto cifrado por pantalla.
    5. Registrar la operación en el historial mediante `crear_entrada()`.

    Parameters
    ----------
    No recibe parámetros explícitos. Todas las entradas se obtienen mediante input().

    Returns
    -------
    None
        La función no retorna ningún valor. Los resultados se muestran por consola
        y se almacenan en el historial.

    Raises
    ------
    ValueError
        Si el usuario ingresa un valor no numérico para el desplazamiento,
        se captura y se muestra un mensaje de error.

    Notes
    -----
    - La función asume que existe una variable global `alfabeto_caracteres`
      que contiene el conjunto de caracteres permitidos.
    - La función asume que existe una función `cifrar(alfabeto, texto, desplazamiento)`
      que realiza el cifrado.
    - La función asume que existe una función `crear_entrada(titulo, entrada, desplazamiento, salida)`
      que guarda el registro en el historial.

    Example
    -------
    >>> cifrar_texto()
    --- Cifrar Caracteres ---
    Cifrar: hola
    Desplasamiento: 3
    Salida: krod
    # Se registra la entrada en el historial
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
        print("¡ERROR PARAMETRO NO VALIDO!\n")
