## 🔑 Diccionarios (`dict`)

Colecciones de pares **clave-valor** mutables y desordenadas (mantienen orden de inserción a partir de Python 3.7+). Se definen con llaves `{}`.

### 🛠️ Funciones Incorporadas
| Función | Descripción | Ejemplo (`d = {"a": 1, "b": 2}`) | Resultado |
| :--- | :--- | :--- | :--- |
| **`len()`** | Devuelve la cantidad de pares clave-valor. | `len(d)` | `2` |
| **`max()` / `min()`** | Devuelve la clave mayor o menor alfabéticamente/numéricamente. | `max(d)` | `'b'` |

---

### ⚙️ Métodos Principales de Diccionarios

#### 🔍 Obtención y Recorrido
| Método | Descripción | Ejemplo (`d = {"a": 10, "b": 20}`) | Resultado |
| :--- | :--- | :--- | :--- |
| **`.get(key, default)`** | Devuelve el valor de la clave. Si no existe, devuelve `None` o el valor por defecto. | `d.get("c", 0)` | `0` |
| **`.keys()`** | Devuelve una vista con todas las **claves** del diccionario. | `d.keys()` | `dict_keys(['a', 'b'])` |
| **`.values()`** | Devuelve una vista con todos los **valores** del diccionario. | `d.values()` | `dict_values([10, 20])` |
| **`.items()`** | Devuelve una vista con tuplas **`(clave, valor)`**. Útil para iterar. | `d.items()` | `dict_items([('a', 10), ...])` |

#### ➕ Edición y Eliminación
| Método | Descripción | Ejemplo (`d = {"a": 1}`) | Estado Final |
| :--- | :--- | :--- | :--- |
| **`.update(otro_dict)`** | Actualiza el diccionario con las claves y valores de otro. | `d.update({"b": 2})` | `{"a": 1, "b": 2}` |
| **`.pop(key)`** | Elimina la clave y **devuelve** su valor. | `val = d.pop("a")` | `val = 1`, `d = {}` |
| **`.popitem()`** | Elimina y devuelve el **último** par `(clave, valor)` insertado. | `item = d.popitem()` | `item = ('a', 1)` |
| **`.clear()`** | Elimina todos los elementos del diccionario. | `d.clear()` | `{}` |

---