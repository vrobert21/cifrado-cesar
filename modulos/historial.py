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
    """

    try:
        with open("historial_texto.txt", "r", encoding="utf-8") as historial:
            entradas = historial.read()
            print(f"{entradas}\n")

    except FileNotFoundError:
        print("¡Todavia no hay entradas de historial!\n")
