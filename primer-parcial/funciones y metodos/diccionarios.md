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

###resumen para el parcial 

# Diccionarios 

## Crear

```python
dic = {}
```

Agregar o modificar:

```python
dic[clave] = valor
```

Ejemplo:

```python
dic["Desarrollador"] = [50, 90000]
```

---

## Consultar

```python
dic[clave]
```

Si el valor es una lista:

```python
dic[clave][0]
dic[clave][1]
```

---

## Comprobar si existe

```python
if clave in dic:
```

Muy usado para acumular:

```python
if clave not in dic:
    dic[clave] = [0, 0]

dic[clave][0] += cantidad
dic[clave][1] += total
```

---

## Recorrer

### Solo claves

```python
for clave in dic:
    print(clave)
```

### Clave y valor

```python
for clave, valor in dic.items():
    print(clave, valor)
```

### Solo valores

```python
for valor in dic.values():
    print(valor)
```

---

## Diccionario con listas

Ejemplo:

```python
dic = {
    "A": [10, 20],
    "B": [30, 40]
}
```

```python
dic["A"][0] += 5
```

queda:

```python
"A": [15, 20]
```

---

## Patrón típico de parcial

Cuando te dicen **"agrupar por X y acumular datos"**:

```python
resultado = {}

for elemento in lista:

    clave = elemento[...]

    if clave not in resultado:
        resultado[clave] = [0, 0]

    resultado[clave][0] += ...
    resultado[clave][1] += ...
```

Pensalo como:

**¿Cuál es mi clave? → ¿Qué tengo que guardar? → ¿Qué acumulo?**

---

## Ordenar

Si necesitás ordenar lo que hay en el diccionario, normalmente hacés una lista auxiliar:

```python
listado = []

for clave in dic:
    listado.append([dato, clave])

listado.sort(reverse=True)
```

Como `dato` está primero, ordena por ese dato.

Después:

```python
for elemento in listado:
    print(elemento[1], elemento[0])
```

---

## Funciones que tenés que recordar

```python
clave in dic
clave not in dic

dic[clave]
dic[clave] = valor

for clave in dic:
for clave, valor in dic.items()

len(dic)

dic.keys()
dic.values()
dic.items()
```

### La idea principal

**Lista:** accedés por posición.

```python
lista[0]
```

**Diccionario:** accedés por clave.

```python
dic["Juan"]
```

**Diccionario + lista:** clave → varios datos.

```python
dic["Juan"][0]
```
