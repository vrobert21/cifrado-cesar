Aquí tienes el contenido completo en formato Markdown para crear el archivo `README.md`:

```markdown
# 🔐 Cifrado César - Programa de Cifrado y Descifrado

Un programa interactivo en Python que implementa el cifrado César con un alfabeto personalizado, permitiendo cifrar y descifrar texto, además de mantener un historial de todas las operaciones realizadas.

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Estructura del Código](#-estructura-del-código)
- [Funciones Principales](#-funciones-principales)
- [Ejemplos de Uso](#-ejemplos-de-uso)
- [Formato del Historial](#-formato-del-historial)
- [Manejo de Errores](#-manejo-de-errores)
- [Limitaciones](#-limitaciones)
- [Mejoras Futuras](#-mejoras-futuras)
- [Correcciones Pendientes](#-correcciones-pendientes)
- [Licencia](#-licencia)

---

## ✨ Características

- **Cifrado César**: Implementación del cifrado César con alfabeto personalizado.
- **Descifrado**: Función inversa para descifrar textos previamente cifrados.
- **Interfaz de Usuario**: Menú interactivo por consola fácil de usar.
- **Historial**: Registro automático de todas las operaciones en un archivo de texto.
- **Manejo de Errores**: Validación de entradas y manejo graceful de excepciones.
- **Soporte UTF-8**: Compatible con caracteres especiales y acentos.

---

## 📦 Requisitos

- **Python 3.10 o superior** (por el uso de `match-case`)
- Sistema operativo: Windows, macOS o Linux

---

## 🚀 Instalación

### Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/cifrado-cesar.git
cd cifrado-cesar
```

### Ejecutar el programa

```bash
python cifrado_cesar.py
```

---

## 💻 Uso

Al ejecutar el programa, se mostrará el siguiente menú interactivo:

```
-- CIFRADO CESAR --
1. Cifrar Caracteres
2. Descifrar Caracteres
3. Leer Historial
4. Terminar Programa

: 
```

### Opciones del Menú

| Opción | Descripción |
|--------|-------------|
| 1 | Cifrar un texto ingresado por el usuario |
| 2 | Descifrar un texto previamente cifrado |
| 3 | Mostrar todo el historial de operaciones |
| 4 | Salir del programa |

### Ejemplo de Cifrado

```
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
```

### Ejemplo de Descifrado

```
-- CIFRADO CESAR --
1. Cifrar Caracteres
2. Descifrar Caracteres
3. Leer Historial
4. Terminar Programa

: 2

--- Descifrar Caracteres ---
Descifrar: krod
Desplasamiento: 3
Salida: hola
```

---

## 🏗️ Estructura del Código

```
cifrado_cesar.py
├── Variables Globales
│   └── alfabeto_caracteres   # Alfabeto personalizado para cifrado
├── Funciones
│   ├── cifrar()              # Cifra un texto
│   ├── descifrar()           # Descifra un texto
│   ├── funcion_cifrar()      # Interfaz de usuario para cifrar
│   ├── funcion_descifrar()   # Interfaz de usuario para descifrar
│   ├── crear_entrada()       # Registra operación en el historial
│   ├── leer_historial()      # Muestra el historial
│   └── main()                # Menú principal
└── Punto de Entrada
    └── if __name__ == "__main__"
```

---

## 🔧 Funciones Principales

### `cifrar(alfabeto, entrada, desplasamiento)`

Cifra un texto utilizando el cifrado César con un alfabeto personalizado.

**Parámetros:**
- `alfabeto` (str/list): Conjunto de caracteres válidos
- `entrada` (str): Texto a cifrar
- `desplasamiento` (int): Número de posiciones a desplazar

**Retorno:** Texto cifrado (str)

### `descifrar(alfabeto, entrada, desplasamiento)`

Descifra un texto previamente cifrado, operación inversa de `cifrar()`.

**Parámetros:**
- `alfabeto` (str/list): Conjunto de caracteres válidos
- `entrada` (str): Texto a descifrar
- `desplasamiento` (int): Número de posiciones a desplazar

**Retorno:** Texto descifrado (str)

### `crear_entrada(titulo, entrada, desplazamiento, salida)`

Registra una operación en el archivo de historial.

**Parámetros:**
- `titulo` (str): "CIFRAR" o "DESCIFRAR"
- `entrada` (str): Texto original
- `desplazamiento` (int): Valor de desplazamiento usado
- `salida` (str): Texto resultante

**Retorno:** None

### `leer_historial()`

Lee y muestra todo el historial de operaciones almacenado.

**Retorno:** None

### `main()`

Función principal que implementa el menú interactivo del programa.

**Retorno:** None

---

## 📝 Ejemplos de Uso

### Ejemplo 1: Cifrar y Descifrar

```python
from cifrado_cesar import cifrar, descifrar

alfabeto = "abcdefghijklmnopqrstuvwxyz"
texto = "hola mundo"
desplazamiento = 5

# Cifrar
texto_cifrado = cifrar(alfabeto, texto, desplazamiento)
print(texto_cifrado)  # "mtqf rzsit"

# Descifrar
texto_descifrado = descifrar(alfabeto, texto_cifrado, desplazamiento)
print(texto_descifrado)  # "hola mundo"
```

### Ejemplo 2: Caracteres Especiales

```python
alfabeto = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
texto = "Hola Mundo! 123"
desplazamiento = 3

texto_cifrado = cifrar(alfabeto, texto, desplazamiento)
# Los caracteres no alfabéticos se mantienen igual
print(texto_cifrado)  # "Krod Pxqgr! 123"
```

---

## 📄 Formato del Historial

El historial se guarda en el archivo `historial_texto.txt` con el siguiente formato:

```
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
```

Cada entrada está separada por una línea de guiones para facilitar la lectura.

---

## 🛡️ Manejo de Errores

El programa maneja los siguientes errores:

| Error | Manejo |
|-------|--------|
| Valor no numérico en desplazamiento | Muestra mensaje: "¡ERROR PARAMETRO NO VALIDO!" |
| Archivo de historial no existe | Muestra: "¡Todavia no hay entradas de historial!" |
| Opción de menú inválida | Muestra: "-- ¡Opcion no valida! --" |

**Nota:** El programa no maneja interrupciones por teclado (Ctrl+C) ni problemas de permisos de archivos.

---

## ⚠️ Limitaciones

1. **Desplazamientos Negativos**: El manejo de desplazamientos negativos es limitado y puede no funcionar correctamente en todos los casos.

2. **Sin Paginación**: La función `leer_historial()` muestra todo el historial sin paginación, lo que puede saturar la consola con historiales grandes.

3. **Crecimiento del Historial**: El archivo de historial crece indefinidamente sin mecanismos de rotación o limpieza.

4. **Sin Persistencia de Configuración**: No guarda preferencias del usuario (como el alfabeto personalizado).

5. **Dependencia de Python 3.10+**: El uso de `match-case` limita la compatibilidad con versiones anteriores.

---

## 🔮 Mejoras Futuras

- [ ] Soporte para desplazamientos negativos completo
- [ ] Paginación del historial
- [ ] Sistema de rotación del archivo de historial
- [ ] Configuración de alfabeto personalizado por el usuario
- [ ] Interfaz gráfica (GUI)
- [ ] Soporte para diferentes idiomas
- [ ] Exportar historial a otros formatos (CSV, JSON)
- [ ] Cifrado con clave múltiple
- [ ] Modo por lotes (cifrar/descifrar archivos completos)

---

## 📋 Correcciones Pendientes

### Errores Ortográficos

- `Desplasamiento` → `Desplazamiento`
- `Todavia` → `Todavía`
- `entada` → `entrada`
- `Opcion` → `Opción`

### Mejoras en el Código

- Mejorar manejo de desplazamientos negativos
- Agregar validación de entrada en el menú principal
- Manejar `KeyboardInterrupt` para salir gracefulmente
- Implementar pruebas unitarias

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 📞 Contacto

- **Autor**: [Tu Nombre]
- **Email**: [tu.email@ejemplo.com]
- **GitHub**: [https://github.com/tu-usuario](https://github.com/tu-usuario)

---

## 🙏 Agradecimientos

- Inspirado en el clásico cifrado César utilizado por Julio César en la antigua Roma.
- Documentación generada siguiendo las mejores prácticas de Python.

---

## 📊 Estado del Proyecto

![Estado](https://img.shields.io/badge/Estado-En%20Desarrollo-yellow)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Licencia](https://img.shields.io/badge/Licencia-MIT-green)

---

**¡Disfruta cifrando y descifrando tus mensajes!** 🔐
```

Este archivo README.md está completamente formateado en Markdown y contiene:

1. **Estructura completa** con títulos, subtítulos y tablas
2. **Emojis** para mejor legibilidad visual
3. **Bloques de código** con sintaxis resaltada
4. **Tablas** para información estructurada
5. **Listas** de características, limitaciones y mejoras
6. **Enlaces internos** para navegación en la tabla de contenidos
7. **Badges** de estado del proyecto
8. **Formato profesional** para presentación en GitHub

Para usarlo, simplemente copia todo el contenido y pégalo en un archivo llamado `README.md` en la raíz de tu proyecto.