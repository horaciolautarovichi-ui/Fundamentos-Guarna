# 🔤 Trabajo con Cadenas de Caracteres en Python

Guía rápida y de referencia sobre el uso de **funciones incorporadas** y **métodos de string** comunes.

---

## 🛠️ Funciones Incorporadas (Built-in Functions)

Las funciones reciben la cadena como argumento: `funcion(cadena)`.

| Función | Descripción | Ejemplo de Uso | Resultado |
| :--- | :--- | :--- | :--- |
| **`len()`** | Devuelve la cantidad total de caracteres (longitud). | `len("Python")` | `6` |
| **`int()`** | Convierte la cadena a un número entero (*lanza error si no es un número válido*). | `int("123")` | `123` |
| **`min()`** | Devuelve el caracter con menor valor en la tabla **ASCII** (las mayúsculas van antes que las minúsculas). | `min("Zebra")` | `'Z'` |
| **`max()`** | Devuelve el caracter con mayor valor en la tabla **ASCII**. | `max("Algoritmo")` | `'t'` |

---

## ⚙️ Métodos de Cadenas (String Methods)

Los métodos se invocan directamente sobre la variable o literal de cadena: `cadena.metodo()`.

### 🔍 Busqueda y Conteo

| Método | Descripción | Ejemplo (`s = "Algoritmo"`) | Resultado |
| :--- | :--- | :--- | :--- |
| **`.count(sub)`** | Cuenta cuántas veces aparece una subcadena o caracter. | `s.count("o")` | `2` |
| **`.index(sub)`** | Devuelve el índice de la primera aparición (*lanza `ValueError` si no existe*). | `s.index("o")` | `3` |
| **`.find(sub)`** | Devuelve el índice de la primera aparición o `-1` si no la encuentra. | `s.find("ori")` | `3` |

### 🔡 Transformación de Formato

> 💡 **Nota:** Las cadenas en Python son *inmutables*. Estos métodos **no modifican** la cadena original, sino que devuelven una nueva.

| Método | Descripción | Ejemplo (`s = "Hola"`) | Resultado |
| :--- | :--- | :--- | :--- |
| **`.upper()`** | Convierte todos los caracteres a mayúsculas. | `s.upper()` | `"HOLA"` |
| **`.lower()`** | Convierte todos los caracteres a minúsculas. | `s.lower()` | `"hola"` |

### 📊 Validación de Contenido (Devuelven `True` o `False`)

| Método | Condición para devolver `True` |
| :--- | :--- |
| **`.isupper()`** | **Todos** los caracteres alfabéticos están en mayúsculas. |
| **`.islower()`** | **Todos** los caracteres alfabéticos están en minúsculas. |
| **`.isalpha()`** | La cadena contiene **únicamente letras** (sin números, espacios ni símbolos). |
| **`.isnumeric()`** | La cadena contiene **únicamente dígitos numéricos**. |
| **`.isalnum()`** | La cadena contiene **únicamente letras y/o números** (alfanumérico). |

---

## 💻 Ejemplo Integrador en Código

```python
texto = "Algoritmo123"

# Funciones
print(f"Longitud: {len(texto)}")  # Output: 12
print(f"Caracter mayor (ASCII): {max(texto)}")  # Output: 'r'

# Métodos de validación
print(f"¿Es alfanumérico?: {texto.isalnum()}")  # Output: True
print(f"¿Es solo texto?: {texto.isalpha()}")  # Output: False

# Transformación y Búsqueda
mayusculas = texto.upper()
print(f"En mayúsculas: {mayusculas}")  # Output: ALGORITMO123
print(f"Posición de 'ORI': {mayusculas.find('ORI')}")  # Output: 3