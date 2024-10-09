# Codificador de Huffman

## Stack tecnológico y características

- ⚡ [**FastAPI**](https://fastapi.tiangolo.com) para la API backend en Python.
- 🧰 [**Pydantic**](https://docs.pydantic.dev) para la validación de datos y gestión de configuraciones.
- ✅ [**Pytest**](https://pytest.org) para pruebas automatizadas.
- 📝 [**Jinja2**](https://jinja.palletsprojects.com) para la generación de templates HTML dinámicos.
- 🎨 [**DaisyUI**](https://daisyui.com) como framework CSS basado en Tailwind para el diseño de componentes.
- 🌐 [**htmx**](https://htmx.org) para la interactividad del frontend sin necesidad de JavaScript complejo.
- 🐋 [**Docker**](https://www.docker.com) para desplegar la aplicación.

## Prueba la Aplicación

Puedes probar la aplicación visitando la siguiente URL: [https://huffman-coding.onrender.com/](https://huffman-coding.onrender.com/)

## Ejecución de la Aplicación

Para ejecutar la aplicación, asegúrate de tener instalado [Docker](https://www.docker.com) en tu máquina.

1. Clona el repositorio:

```bash
git clone https://github.com/MontillaTomas/huffman-coding
```

2. Accede al directorio del proyecto:

```bash
cd huffman-coding
```

3. Ejecuta la aplicación con Docker Compose:

```bash
docker-compose up
```

4. Accede a la aplicación en tu navegador web:

```bash
http://localhost:8000
```

## ¿Qué es la Codificación de Huffman?

La codificación de Huffman es una técnica de compresión de datos sin pérdida, desarrollada por David Huffman. Se utiliza para reducir el tamaño de los datos, sin perder ningún detalle o información. Este método es particularmente útil cuando hay caracteres que se repiten con frecuencia en los datos, ya que asigna códigos de longitud variable a los caracteres de entrada, basándose en la frecuencia de aparición de cada uno.

En lugar de utilizar una codificación ingenua (donde cada símbolo recibe un código de la misma longitud), la codificación de Huffman asigna códigos más cortos a los caracteres que ocurren con mayor frecuencia y códigos más largos a los que aparecen con menos frecuencia. Esto asegura una mayor eficiencia en la compresión.

## ¿Cómo funciona?

Para determinar cómo asignar los códigos a cada símbolo, se deben seguir los siguientes pasos:

1. Analizar la frecuencia de cada carácter: Contamos cuántas veces aparece cada símbolo en el conjunto de datos.

2. Construir el árbol binario:
    * Tomamos el par de nodos con la frecuencia más baja.
    * Repetimos este proceso hasta que solo quede un nodo en la estructura.

3. Etiquetar los bordes del árbol: Comenzando desde la raíz, asignamos un 1 al borde que conduce al hijo izquierdo y un 0 al borde que conduce al hijo derecho. Hacemos esto para cada uno de los hijos.

4. Generar los códigos: Recorremos el árbol desde cada hoja hasta la raíz, anotando los números binarios etiquetados a lo largo del camino para crear la palabra de código de cada símbolo.

## Implementación del Algoritmo

El método `encode` de la clase `HuffmanEncoder` se encarga de codificar los símbolos. Este método toma una lista de símbolos no codificados y devuelve un mapa de codificación junto con los símbolos codificados.

```python
class HuffmanEncoder(Encoder):

    def encode(self, list_of_symbols: UnencodedSymbols) -> tuple[EncodingMap, EncodedSymbols]:
        if len(list_of_symbols.unencoded) == 0:
            return EncodingMap(map={}), EncodedSymbols(encoded=[])

        nodes = self._calculate_frequencies(list_of_symbols)
        tree = self._build_huffman_tree(nodes)
        codes = self._huffman_code_tree(tree[0])
        enc_symbols = [codes[symbol] for symbol in list_of_symbols.unencoded]
        return EncodingMap(map=codes), EncodedSymbols(encoded=enc_symbols)

```

La clase `NodeTree` se utiliza para representar un nodo en el árbol de Huffman. Cada nodo tiene dos hijos, `left` y `right`.

```python
class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)
```

El método `_calculate_frequencies` calcula la frecuencia de aparición de cada símbolo en la lista de símbolos no codificados y devuelve una lista ordenada de símbolos según su frecuencia, de mayor a menor.

```python
class HuffmanEncoder(Encoder):

    def _calculate_frequencies(self, list_of_symbols: UnencodedSymbols):
        frequencies = {}
        for symbol in list_of_symbols.unencoded:
            if symbol in frequencies:
                frequencies[symbol] += 1
            else:
                frequencies[symbol] = 1
        return sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

```

El método `_build_huffman_tree` construye el árbol de Huffman a partir de los nodos ordenados por frecuencia. En cada iteración, toma los dos nodos con las frecuencias más bajas, los combina en un nuevo nodo con una frecuencia igual a la suma de ambos, y vuelve a insertar este nuevo nodo en la lista. Este proceso se repite hasta que solo queda un nodo, que representa la raíz del árbol de Huffman.

```python
class HuffmanEncoder(Encoder):

    def _build_huffman_tree(self, nodes):
        while len(nodes) > 1:
            (key1, c1) = nodes[-1]
            (key2, c2) = nodes[-2]
            nodes = nodes[:-2]
            node = NodeTree(key1, key2)
            nodes.append((node, c1 + c2))
            nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
        return nodes[0]
```

El método `_huffman_code_tree` genera de forma recursiva los códigos de Huffman para los símbolos en el árbol utilizando un algoritmo de recorrido en profundidad (Depth-First Search, DFS). A medida que recorre el árbol desde la raíz hasta las hojas, va construyendo las cadenas binarias que representan los códigos de cada símbolo. Si el nodo actual es una hoja (es decir, un símbolo), se asigna el código binario acumulado hasta ese punto. En el recorrido, asigna "1" para los nodos izquierdos y "0" para los nodos derechos. Finalmente, devuelve un diccionario que asocia cada símbolo con su código de Huffman correspondiente.

```python
def _huffman_code_tree(self, node, left=True, bin_string="") -> dict:
        if type(node) is str:
            return {node: bin_string}
        (left, right) = node.children()
        codes = dict()
        codes.update(self._huffman_code_tree(left, True, bin_string + "1"))
        codes.update(self._huffman_code_tree(right, False, bin_string + "0"))
        codes = sorted(codes.items(), key=lambda x: (len(x[1]), x[1]))
        return dict(codes)
```