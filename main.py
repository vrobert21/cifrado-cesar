# Archivo principal del programa

from modulos.cifrar import funcion_cifrar  # Importa la función cifrar
from modulos.descifrar import funcion_descifrar  # Importa la función descifrar
from modulos.historial import (
    leer_historial,
)  # Importa la funnción que muestra el historial


def main():
    """
    Función principal que implementa el menú interactivo del programa Cifrado César.

    Esta función ejecuta un bucle infinito que muestra un menú con las opciones
    disponibles (cifrar, descifrar, leer historial y salir), procesa la selección
    del usuario y ejecuta la función correspondiente. El programa continúa
    ejecutándose hasta que el usuario selecciona la opción de salir.

    Parameters
    ----------
    No recibe parámetros.

    Returns
    -------
    None
        La función no retorna ningún valor. Finaliza su ejecución cuando el
        usuario selecciona la opción de salir (opción 4), rompiendo el bucle.

    Raises
    ------
    KeyboardInterrupt
        Si el usuario presiona Ctrl+C, el programa podría interrumpirse.
        Esta excepción no está manejada explícitamente.
    EOFError
        Si se alcanza el final del archivo en la entrada estándar (por ejemplo,
        al redirigir la entrada), podría ocurrir un error no manejado.

    Notes
    -----
    - La función utiliza la estructura `match-case` (Python 3.10+), por lo que
      requiere Python 3.10 o superior para ejecutarse correctamente.
    - Las funciones llamadas desde el menú (`funcion_cifrar`, `funcion_descifrar`,
      `leer_historial`) deben estar definidas en el ámbito global.
    - El menú se muestra en un bucle infinito hasta que el usuario elige salir.
    - Cada opción del menú ejecuta una función específica:
      * Opción 1: `funcion_cifrar()` - Interfaz para cifrar texto
      * Opción 2: `funcion_descifrar()` - Interfaz para descifrar texto
      * Opción 3: `leer_historial()` - Muestra el historial de operaciones
      * Opción 4: Termina el programa
    - Cualquier otra entrada se considera inválida y se muestra un mensaje de error.

    Workflow
    --------
    1. Muestra el título "CIFRADO CESAR" y las opciones disponibles.
    2. Solicita al usuario que ingrese una opción.
    3. Evalúa la opción ingresada mediante `match-case`:
       - "1": Llama a `funcion_cifrar()`
       - "2": Llama a `funcion_descifrar()`
       - "3": Llama a `leer_historial()`
       - "4": Rompe el bucle y termina el programa
       - Otro: Muestra mensaje de error
    4. Vuelve al paso 1 hasta que el usuario selecciona la opción 4.

    Examples
    --------
    Ejemplo de ejecución interactiva:

    >>> # (Simulación de ejecución)
    -- CIFRADO CESAR --
    1. Cifrar Caracteres
    2. Descifrar Caracteres
    3. Leer Historial
    4. Terminar Programa

    : 1
    --- Cifrar Caracteres ---
    Cifrar: hola
    Desplasamiento: 3
    Salida: krod

    -- CIFRADO CESAR --
    1. Cifrar Caracteres
    2. Descifrar Caracteres
    3. Leer Historial
    4. Terminar Programa

    : 4
    # El programa termina

    >>> # Con opción inválida
    -- CIFRADO CESAR --
    1. Cifrar Caracteres
    2. Descifrar Caracteres
    3. Leer Historial
    4. Terminar Programa

    : 5
    -- ¡Opcion no valida! --
    # El menú se vuelve a mostrar

    See Also
    --------
    funcion_cifrar : Interfaz de usuario para cifrar texto.
    funcion_descifrar : Interfaz de usuario para descifrar texto.
    leer_historial : Función que muestra el historial de operaciones.

    Requirements
    ------------
    Python 3.10 o superior (por el uso de match-case).

    Warnings
    --------
    - El programa no maneja la interrupción por teclado (Ctrl+C).
    - Las funciones llamadas deben manejar sus propias excepciones para
      evitar que el programa principal falle inesperadamente.
    - No hay validación del tipo de entrada más allá del match-case,
      por lo que cualquier texto que no sea "1", "2", "3" o "4" se considera inválido.
    """

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
                print("-- ¡Opción no valida! --")


if __name__ == "__main__":
    main()
