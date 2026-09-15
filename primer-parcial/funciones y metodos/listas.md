---

## 📋 Listas (`list`)

Colecciones ordenadas y mutables de elementos. Se definen con corchetes `[]`.

### 🛠️ Funciones Incorporadas
| Función | Descripción | Ejemplo (`l = [4, 2, 8]`) | Resultado |
| :--- | :--- | :--- | :--- |
| **`len()`** | Devuelve la cantidad total de elementos. | `len(l)` | `3` |
| **`min()`** | Devuelve el elemento de menor valor. | `min(l)` | `2` |
| **`max()`** | Devuelve el elemento de mayor valor. | `max(l)` | `8` |
| **`sum()`** | Suma todos los elementos numéricos de la lista. | `sum(l)` | `14` |
| **`sorted()`** | Devuelve una **nueva** lista con los elementos ordenados sin modificar la original. | `sorted(l)` | `[2, 4, 8]` |

---

### ⚙️ Métodos Principales de Listas

#### ➕ Agregar y Eliminar
| Método | Descripción | Ejemplo (`l = [1, 2]`) | Estado Final |
| :--- | :--- | :--- | :--- |
| **`.append(x)`** | Agrega el elemento `x` al **final** de la lista. | `l.append(3)` | `[1, 2, 3]` |
| **`.insert(i, x)`** | Inserta el elemento `x` en la posición del índice `i`. | `l.insert(0, 9)` | `[9, 1, 2]` |
| **`.extend(iterable)`** | Agrega todos los elementos de otro iterable al final. | `l.extend([3, 4])` | `[1, 2, 3, 4]` |
| **`.pop(i)`** | Elimina y **devuelve** el elemento en el índice `i` (por defecto el último). | `elem = l.pop()` | `elem = 2`, `l = [1]` |
| **`.remove(x)`** | Elimina la **primera aparición** del valor `x` (*error si no existe*). | `l.remove(2)` | `[1]` |
| **`.clear()`** | Elimina **todos** los elementos de la lista. | `l.clear()` | `[]` |

#### 🔍 Orden y Búsqueda
| Método | Descripción | Ejemplo (`l = [3, 1, 3]`) | Resultado |
| :--- | :--- | :--- | :--- |
| **`.sort()`** | Ordena la lista **en el lugar** (modifica la lista original). | `l.sort()` | `l = [1, 3, 3]` |
| **`.reverse()`** | Invierte el orden de los elementos en la lista. | `l.reverse()` | `l = [3, 1, 3]` |
| **`.count(x)`** | Cuenta cuántas veces aparece el valor `x`. | `l.count(3)` | `2` |
| **`.index(x)`** | Devuelve el índice de la primera aparición de `x`. | `l.index(1)` | `1` |

---