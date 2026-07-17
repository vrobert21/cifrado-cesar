# Modulo que controla el historial

"""
-- Este Modulo se encarga de visualizar el historial, crearlas y borrar todas las entradas. --
"""


def crear_entrada(titulo, entrada, desplazamiento, salida):
    """
    Registra una operación de cifrado/descifrado en el archivo de historial.

    Esta función toma los datos de una operación realizada (título, entrada,
    desplazamiento y salida) y los escribe en un archivo de texto plano llamado
    "historial_texto.txt" en formato legible, agregando cada nueva entrada al
    final del archivo.

    Parameters
    ----------
    titulo : str
        Título o tipo de operación realizada. Generalmente "CIFRAR" o "DESCIFRAR".
        Se utiliza como encabezado de la entrada en el historial.
    entrada : str
        Texto original proporcionado por el usuario antes de la operación.
        Puede ser el texto a cifrar o el texto cifrado a descifrar.
    desplazamiento : int
        Número de posiciones utilizadas en el desplazamiento para la operación.
        Este valor debe ser el mismo que se usó para cifrar o descifrar.
    salida : str
        Texto resultante después de aplicar la operación de cifrado o descifrado.

    Returns
    -------
    None
        La función no retorna ningún valor. Su efecto es exclusivamente la
        escritura en el archivo de historial.

    Raises
    ------
    FileNotFoundError
        Puede ocurrir si no se tienen permisos para crear o escribir en el archivo.
        Sin embargo, al usar el modo 'a' (append), el archivo se crea automáticamente
        si no existe.
    IOError
        Puede ocurrir si hay problemas de permisos o de escritura en el disco.

    Notes
    -----
    - El archivo se guarda en el directorio de trabajo actual con el nombre
      "historial_texto.txt".
    - Se utiliza codificación UTF-8 para soportar caracteres especiales y acentos.
    - El modo 'a' (append) asegura que las nuevas entradas se agreguen al final
      del archivo sin sobrescribir el historial existente.
    - Cada entrada está separada por una línea de guiones ("==========") para
      facilitar la lectura y diferenciación entre operaciones.
    - El formato de cada entrada es:

      ==========
      - TITULO -
      - Entrada: texto_original
      - Desplasamiento: numero
      - Salida: texto_resultante
      ==========

    - El archivo se cierra automáticamente al salir del bloque `with`,
      garantizando que todos los datos se escriban correctamente.

    Examples
    --------
    >>> crear_entrada("CIFRAR", "hola", 3, "krod")
    # Se agrega al archivo historial_texto.txt:
    # ==========
    # - CIFRAR -
    # - Entrada: hola
    # - Desplasamiento: 3
    # - Salida: krod
    # ==========

    >>> crear_entrada("DESCIFRAR", "krod", 3, "hola")
    # Se agrega al archivo historial_texto.txt:
    # ==========
    # - DESCIFRAR -
    # - Entrada: krod
    # - Desplasamiento: 3
    # - Salida: hola
    # ==========

    >>> # Múltiples entradas se acumulan en el archivo
    >>> crear_entrada("CIFRAR", "zapato", 1, "abqbup")
    >>> crear_entrada("DESCIFRAR", "abqbup", 1, "zapato")
    # El archivo contendrá ambas entradas secuencialmente

    See Also
    --------
    cifrar : Función que realiza el cifrado y llama a crear_entrada.
    descifrar : Función que realiza el descifrado y llama a crear_entrada.
    funcion_cifrar : Interfaz de usuario que utiliza crear_entrada.
    funcion_descifrar : Interfaz de usuario que utiliza crear_entrada.

    Warnings
    --------
    El archivo "historial_texto.txt" crecerá indefinidamente con cada llamada
    a esta función. En aplicaciones de larga duración, considere implementar
    un sistema de rotación o limpieza del archivo.
    """

    with open("historial_texto.txt", "a", encoding="utf-8") as historial:
        historial.write(
            f"""\n==========\n- {titulo} -\n- Entrada: {entrada}\n- Desplazamiento: {desplazamiento}\n- Salida: {salida}\n=========="""
        )


def leer_historial():
    """
    Lee y muestra todo el historial de operaciones de cifrado/descifrado almacenado.

    Esta función abre el archivo de historial "historial_texto.txt" en modo lectura,
    muestra todo su contenido por pantalla y maneja gracefulmente el caso en que
    el archivo aún no existe (no hay operaciones registradas).

    Parameters
    ----------
    No recibe parámetros.

    Returns
    -------
    None
        La función no retorna ningún valor. Su efecto es mostrar el contenido
        del historial por consola o un mensaje informativo si no hay registros.

    Raises
    ------
    FileNotFoundError
        Se captura internamente y se maneja mostrando un mensaje amigable al
        usuario. La excepción no se propaga.
    PermissionError
        Puede ocurrir si el usuario no tiene permisos de lectura para el archivo.
        Esta excepción no está manejada explícitamente y podría propagarse.
    UnicodeDecodeError
        Puede ocurrir si el archivo no está codificado en UTF-8. Esto podría
        suceder si el archivo fue modificado externamente con otra codificación.

    Notes
    -----
    - La función asume que el archivo "historial_texto.txt" existe en el
      directorio de trabajo actual.
    - Se utiliza codificación UTF-8 para leer correctamente caracteres especiales
      y acentos guardados previamente.
    - El archivo se abre en modo 'r' (lectura) y se cierra automáticamente
      al salir del bloque `with`.
    - Si el archivo está vacío, se mostrará una línea en blanco (sin mensaje
      de error, ya que no se considera una excepción).
    - El formato de visualización es el mismo que se guardó en el archivo,
      incluyendo los separadores "==========" entre entradas.

    Workflow
    --------
    1. Intenta abrir el archivo "historial_texto.txt" en modo lectura.
    2. Lee todo el contenido del archivo.
    3. Muestra el contenido por pantalla, seguido de una línea en blanco.
    4. Si el archivo no existe, muestra un mensaje informativo indicando que
       no hay entradas en el historial.

    Examples
    --------
    >>> leer_historial()
    ==========
    - CIFRAR -
    - Entrada: hola
    - Desplasamiento: 3
    - Salida: krod
    ==========
    ==========
    - DESCIFRAR -
    - Entrada: krod
    - Desplasamiento: 3
    - Salida: hola
    ==========

    >>> leer_historial()  # Cuando no hay historial
    ¡Todavia no hay entradas de historial!

    >>> leer_historial()  # Cuando el archivo está vacío
    # (No muestra nada, solo un salto de línea)

    See Also
    --------
    crear_entrada : Función que escribe entradas en el historial.
    funcion_cifrar : Interfaz de usuario que utiliza crear_entrada.
    funcion_descifrar : Interfaz de usuario que utiliza crear_entrada.

    Warnings
    --------
    - Esta función muestra todo el historial sin filtros ni paginación.
      Para historiales muy grandes, podría saturar la consola.
    - No existe un mecanismo de limpieza o rotación del archivo, por lo que
      el historial puede crecer indefinidamente.
    - Los mensajes de error no especifican problemas de permisos o codificación,
      solo maneja el caso específico de archivo no encontrado.
    """

    try:
        with open("historial_texto.txt", "r", encoding="utf-8") as historial:
            entradas = historial.read()
            print(f"{entradas}\n")

    except FileNotFoundError:
        print("¡Todavia no hay entradas de historial!\n")
