# 📚 Apunte: Diccionarios, Listas y Tuplas (FIUBA - Algo I)

Resumen de métodos, funciones y conceptos clave explicados en la clase de **Algoritmos y Programación I**.

---

## 🔑 Diccionarios (`dict`)

Los diccionarios permiten almacenar pares de **clave: valor**[cite: 1]. 
* **Claves:** Son únicas e inmutables (números, strings, booleanas, etc.)[cite: 1].
* **Valores:** Pueden ser de cualquier tipo (mutables o inmutables, como enteros, listas, tuplas).
* **Orden:** Son conjuntos no ordenables de elementos.

---

### 🛠️ Funciones Incorporadas Aplicables

| Función | Descripción | Ejemplo de Uso |
| :--- | :--- | :--- |
| **`len()`** | Devuelve la cantidad de pares clave-valor. | `len(torneos)` |
| **`type()`** | Muestra el tipo de dato (retorna `<class 'dict'>`)[cite: 1]. | `type(torneos)` |
| **`sorted()`** | Ordena las claves, valores o tuplas de pares. | `sorted(alumnos.keys())` |
| **`zip()`** | Empareja elementos de dos o más iterables (retorna tuplas). | `zip(precios, stock)` |
| **`dict()`** | Transforma un iterable de pares (como un `zip`) en un diccionario. | `dict(zip(producto, codigo))` |

---

### ⚙️ Sintaxis y Métodos Principales

#### 📝 Operaciones Básicas por Sintaxis
* **Acceder a un valor:** `torneos['ROSARIO']` *(si la clave no existe, lanza `KeyError`)*[cite: 1].
* **Guardar / Modificar un valor:** `torneos['FERRO'] = 2` o `torneos['ROSARIO'] += 1`.
* **Eliminar un par clave-valor:** `del torneos['VELEZ']`.
* **Verificar existencia de clave:** `if 'BOCA' in torneos:` o `if 'BOCA' not in torneos:`.

#### 🔍 Métodos del Tipo `dict`
| Método | Descripción | Ejemplo |
| :--- | :--- | :--- |
| **`.keys()`** | Devuelve un iterable con todas las **claves**. | `for k in alumnos.keys():` |
| **`.values()`** | Devuelve un iterable con todos los **valores**. | `for v in alumnos.values():` |
| **`.items()`** | Devuelve un iterable con tuplas de **(clave, valor)**. | `for k, v in alumnos.items():` |
| **`.get(clave, defecto)`** | Busca una clave. Si no la encuentra, devuelve el valor por defecto sin lanzar error. | `alumnos.get(6, 'no existe')` |
| **`.pop(clave)`** | Extrae y elimina del diccionario el elemento indicado por su clave. | `elem = alumnos.pop(6338)` |
| **`.clear()`** | Limpia o vacía completamente el diccionario. | `alumnos.clear()` |

---

## 📋 Comparativa Rápida de Estructuras (Listas vs Tuplas vs Diccionarios)

> Basado en el cuadro resumen oficial de la materia:

| Estructura | Sintaxis | Tipo de Índice / Acceso | Inmutabilidad / Mutabilidad |
| :--- | :--- | :--- | :--- |
| **Diccionarios** | `{k: v}` | Indexa por **Clave** (clave inmutable y única)[cite: 1] | **Mutable** |
| **Listas** | `[...]` | Indexa por **Posición numérica** | **Mutable** |
| **Tuplas** | `(...)` | Indexa por **Posición numérica** | **Inmutable** |

---

## ⚡ Conceptos y Funciones Auxiliares Vistas en Clase

### 🔄 Funciones Anónimas (`lambda`)
Sintaxis abreviada para definir funciones mínimas en una sola línea:
```python
# Sintaxis: lambda argumento: resultado
suma = lambda x, y: x + y  # Equivalente a def suma(x, y): return x + y

