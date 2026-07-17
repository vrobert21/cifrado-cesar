# Modulo que controla el historial

"""
Este Modulo se encarga de visualizar el historial, crearlas y borrar todas las entradas.
"""


def crear_entrada(titulo, entrada, desplazamiento, salida):
    with open("historial_texto.txt", "a", encoding="utf-8") as historial:
        historial.write(
            f"""\n==========\n- {titulo} -\n- Entrada: {entrada}\n- Desplasamiento: {desplazamiento}\n- Salida: {salida}\n=========="""
        )


def leer_historial():
    try:
        with open("historial_texto.txt", "r", encoding="utf-8") as historial:
            entradas = historial.read()
            print(f"{entradas}\n")

    except FileNotFoundError:
        print("¡Todavia no hay entradas de historial!\n")
