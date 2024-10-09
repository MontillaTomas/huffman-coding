# Huffman Coding

## Technological Stack and Features

- ⚡ [**FastAPI**](https://fastapi.tiangolo.com) for the backend API in Python.
- 🧰 [**Pydantic**](https://docs.pydantic.dev) for data validation and configuration management.
- ✅ [**Pytest**](https://pytest.org) for automated testing.
- 📝 [**Jinja2**](https://jinja.palletsprojects.com) for generating dynamic HTML templates.
- 🎨 [**DaisyUI**](https://daisyui.com) as a CSS framework based on Tailwind for component design.
- 🌐 [**htmx**](https://htmx.org) for frontend interactivity without complex JavaScript.
- 🐋 [**Docker**](https://www.docker.com) for deploying the application.

## Try it out

You can try out the application by visiting the following URL: [https://huffman-coding.onrender.com/](https://huffman-coding.onrender.com/)

## Running the Application

To run the application, make sure you have [Docker](https://www.docker.com) installed on your machine.

1. Clone the repository:

```bash
git clone https://github.com/MontillaTomas/huffman-coding
```

2. Navigate to the project directory:

```bash
cd huffman-coding
```

3. Run the application with Docker Compose:

```bash
docker-compose up
```

4. Access the application in your web browser:

```bash
http://localhost:8000
```

## What is Huffman Coding?

Huffman coding is a lossless data compression technique developed by David Huffman. It is used to reduce the size of data without losing any details or information. This method is particularly useful when there are characters that frequently repeat in the data, as it assigns variable-length codes to the input characters based on their frequency of occurrence.

Instead of using a naive encoding (where each symbol receives a code of the same length), Huffman coding assigns shorter codes to characters that occur more frequently and longer codes to those that appear less frequently. This ensures greater efficiency in compression.

## How Does It Work?

To determine how to assign codes to each symbol, follow these steps:

1. Analyze the frequency of each character: Count how many times each symbol appears in the dataset.

2. Build the binary tree:
    * Take the pair of nodes with the lowest frequency.
    * Repeat this process until only one node remains in the structure.

3. Label the edges of the tree: Starting from the root, assign a 1 to the edge leading to the left child and a 0 to the edge leading to the right child. Do this for each of the children.

4. Generate the codes: Traverse the tree from each leaf to the root, noting the labeled binary numbers along the way to create the code word for each symbol.

## Algorithm Implementation

The `encode` method of the `HuffmanEncoder` class is responsible for encoding the symbols. This method takes a list of unencoded symbols and returns an encoding map along with the encoded symbols.

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
The `NodeTree` class is used to represent a node in the Huffman tree. Each node has two children, `left` and `right`.

```python
class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)
```

The `_calculate_frequencies` method calculates the frequency of each symbol in the list of unencoded symbols and returns a sorted list of symbols by their frequency, from highest to lowest.

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

The `_build_huffman_tree` method constructs the Huffman tree from the nodes sorted by frequency. In each iteration, it takes the two nodes with the lowest frequencies, combines them into a new node with a frequency equal to the sum of both, and reinserts this new node into the list. This process is repeated until only one node remains, which represents the root of the Huffman tree.

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

The `_huffman_code_tree` method recursively generates the Huffman codes for the symbols in the tree using a Depth-First Search (DFS) algorithm. As it traverses the tree from the root to the leaves, it constructs the binary strings that represent the codes for each symbol. If the current node is a leaf (i.e., a symbol), it assigns the accumulated binary code up to that point. During the traversal, it assigns "1" for left nodes and "0" for right nodes. Finally, it returns a dictionary that associates each symbol with its corresponding Huffman code.

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