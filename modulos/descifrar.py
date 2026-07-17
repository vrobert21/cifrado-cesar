# Modulo de Descifrado.

"""
-- Este archivo contiene el modulo de descifrado. --
"""

from modulos.caracteres import (
    alfabeto_completo,
)  # Importar lista de caracteres personalizados
from modulos.historial import (
    crear_entrada,
)  # Importar función para crear entradas de historial


alfabeto_caracteres = alfabeto_completo  # Variable Global


def descifrar(alfabeto, entrada, desplasamiento):
    """
    Descifra un texto previamente cifrado con el cifrado César utilizando un alfabeto personalizado.

    Esta función es la operación inversa de `cifrar()`. Recorre cada carácter del texto
    de entrada y lo desplaza hacia atrás un número determinado de posiciones dentro del
    alfabeto proporcionado. Los caracteres que no pertenecen al alfabeto se mantienen
    sin cambios.

    Parameters
    ----------
    alfabeto : str o list
        Conjunto de caracteres válidos para el descifrado. Debe ser una secuencia
        ordenada donde cada índice representa la posición del carácter. Debe ser
        el mismo alfabeto utilizado para cifrar el texto original.
    entrada : str
        Texto cifrado que se desea descifrar. Puede contener caracteres que no estén
        en el alfabeto, los cuales se conservarán tal cual.
    desplasamiento : int
        Número de posiciones que se desplazará cada carácter hacia atrás en el alfabeto.
        Debe ser el mismo valor de desplazamiento utilizado durante el cifrado.
        Puede ser positivo (desplazamiento hacia atrás) o negativo (desplazamiento
        hacia adelante, comportándose como cifrado).

    Returns
    -------
    str
        Texto descifrado resultante. Los caracteres del alfabeto serán desplazados
        hacia atrás, y los caracteres no pertenecientes al alfabeto permanecerán
        inalterados.

    Notes
    -----
    - El desplazamiento aplica de forma circular: si se retrocede más allá del
      principio del alfabeto, continúa desde el final (y viceversa para
      desplazamientos negativos).
    - Esta función es la inversa exacta de `cifrar()` cuando se usa el mismo
      alfabeto y desplazamiento.
    - La función asume que el alfabeto no contiene caracteres duplicados.
    - La búsqueda de la posición de cada carácter se realiza mediante el
      método `index()`, por lo que la complejidad es O(n*m) donde n es la
      longitud de la entrada y m es la longitud del alfabeto.

    Examples
    --------
    >>> alfabeto = "abcdefghijklmnopqrstuvwxyz"
    >>> descifrar(alfabeto, "krod", 3)
    'hola'

    >>> descifrar(alfabeto, "abqbup", 1)
    'zapato'

    >>> # Descifrando un texto con espacios
    >>> descifrar(alfabeto, "krod pxqgr", 3)
    'hola mundo'

    >>> # Con caracteres no alfabéticos
    >>> descifrar(alfabeto, "krod123", 3)
    'hola123'

    >>> # Con desplazamiento negativo (equivale a cifrar)
    >>> descifrar(alfabeto, "hola", -3)
    'krod'

    >>> # Verificando que cifrar y descifrar son inversos
    >>> texto = "hola mundo"
    >>> cifrado = cifrar(alfabeto, texto, 5)
    >>> descifrar(alfabeto, cifrado, 5) == texto
    True

    See Also
    --------
    cifrar : Función complementaria que realiza el cifrado César.

    Warnings
    --------
    La implementación actual tiene una limitación en el manejo de desplazamientos
    negativos. Para desplazamientos negativos que produzcan posiciones menores
    a 0, la función puede no comportarse correctamente. Se recomienda usar
    desplazamientos positivos para descifrar y negativos solo si se comprende
    el comportamiento circular.
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

    Esta función proporciona una interacción por consola que permite al usuario
    ingresar un texto cifrado y un desplazamiento para obtener el texto original.
    La función maneja la entrada del usuario, valida los parámetros, ejecuta el
    descifrado y registra la operación en el historial.

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
        se captura la excepción y se muestra un mensaje de error amigable.
        La función no propaga la excepción.

    Notes
    -----
    - La función asume que existe una variable global `alfabeto_caracteres`
      que contiene el conjunto de caracteres permitidos para el descifrado.
    - La función asume que existe una función `descifrar(alfabeto, entrada, desplasamiento)`
      que realiza el descifrado del texto.
    - La función asume que existe una función `crear_entrada(titulo, entrada, desplasamiento, salida)`
      que guarda el registro en el historial con el título "DESCIFRAR".
    - El título de la entrada se fija como "DESCIFRAR" para identificación en el historial.
    - El desplazamiento debe ser un número entero positivo para descifrar correctamente
      (aunque la función `descifrar()` también soporta valores negativos).

    Workflow
    --------
    1. Muestra un encabezado indicando la operación de descifrado.
    2. Solicita al usuario el texto cifrado.
    3. Solicita al usuario el desplazamiento utilizado en el cifrado.
    4. Llama a `descifrar()` con los parámetros proporcionados.
    5. Muestra el texto descifrado por pantalla.
    6. Registra la operación en el historial mediante `crear_entrada()`.

    Examples
    --------
    >>> funcion_descifrar()
    --- Descifrar Caracteres ---
    Descifrar: krod
    Desplasamiento: 3
    Salida: hola
    # Se registra la entrada en el historial con título "DESCIFRAR"

    >>> funcion_descifrar()
    --- Descifrar Caracteres ---
    Descifrar: abqbup
    Desplasamiento: 1
    Salida: zapato
    # Se registra la entrada en el historial

    >>> funcion_descifrar()  # Con entrada inválida
    --- Descifrar Caracteres ---
    Descifrar: krod
    Desplasamiento: tres
    ¡ERROR PARAMETRO NO VALIDO!
    # No se registra en el historial debido al error

    See Also
    --------
    cifrar : Función que realiza el cifrado César.
    descifrar : Función que realiza el descifrado César.
    crear_entrada : Función que registra operaciones en el historial.
    funcion_cifrar : Función similar para cifrar texto (interfaz de usuario).
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
