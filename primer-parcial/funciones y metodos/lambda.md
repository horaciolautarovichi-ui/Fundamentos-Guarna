# Funciones `lambda`

Una función `lambda` es una **función anónima** que permite definir funciones simples en una sola expresión, sin utilizar `def`.

## Sintaxis

```python
lambda parametros: expresion
```

Ejemplo:

```python
lambda x: x * 2
```

Es equivalente a:

```python
def duplicar(x):
    return x * 2
```

La diferencia es que `lambda` suele utilizarse para funciones **pequeñas y de uso puntual**.

---

## Usos comunes

### Con `sorted()`

Permite indicar el criterio de ordenamiento:

```python
personas = [("Juan", 25), ("Ana", 20), ("Pedro", 30)]

ordenadas = sorted(personas, key=lambda persona: persona[1])
```

Ordena las personas según su edad.

### Con `map()`

Aplica una operación a cada elemento:

```python
numeros = [1, 2, 3, 4]

resultado = list(map(lambda x: x * 2, numeros))
```

Resultado:

```python
[2, 4, 6, 8]
```

### Con `filter()`

Permite seleccionar elementos según una condición:

```python
numeros = [1, 2, 3, 4, 5, 6]

pares = list(filter(lambda x: x % 2 == 0, numeros))
```

Resultado:

```python
[2, 4, 6]
```

---

## Buenas prácticas

* Usar `lambda` para **operaciones simples y fáciles de leer**.
* Si la lógica es compleja, preferir una función con `def`.
* Si la función se reutiliza o necesita un nombre descriptivo, preferir `def`.
* Utilizar nombres representativos para los parámetros cuando sea necesario.
* No utilizar `lambda` únicamente para evitar escribir `def`.

Ejemplo claro:

```python
sorted(personas, key=lambda persona: persona[1])
```

Si la expresión se vuelve difícil de entender, es preferible:

```python
def obtener_edad(persona):
    return persona[1]

sorted(personas, key=obtener_edad)
```

## Relación con el PEP de la cátedra

El **PEP 75.40 no establece reglas específicas sobre `lambda`**. Sin embargo, sus recomendaciones generales priorizan la claridad, los nombres representativos, la responsabilidad única y evitar código difícil de seguir.
Por eso, la regla práctica es:

> **`lambda` para funciones simples y puntuales; `def` para funciones complejas, reutilizables o que necesiten un nombre.**
