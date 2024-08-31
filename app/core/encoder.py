"""
This module provides an abstract base class `Encoder` and a concrete implementation `HuffmanEncoder`
for encoding symbols using Huffman coding.
"""
from abc import ABC, abstractmethod
from app.schemas import UnencodedSymbols, EncodedSymbols, EncodingMap
from .node_tree import NodeTree


class Encoder(ABC):
    """
    An abstract base class that defines the interface for encoders.
    """
    @abstractmethod
    def encode(self, list_of_symbols: UnencodedSymbols) -> tuple[EncodingMap, EncodedSymbols]:
        """
        Encodes a list of symbols and returns the encoding map and the encoded symbols.

        Args:
            list_of_symbols (UnencodedSymbols): The list of symbols to encode.

        Returns:
            tuple[EncodingMap, EncodedSymbols]: The encoding map and the encoded symbols.
        """
        pass


class HuffmanEncoder(Encoder):
    """
    An encoder that uses the Huffman coding algorithm to encode a list of symbols.
    """

    def _huffman_code_tree(self, node, left=True, bin_string="") -> dict:
        """
        Recursively generates the Huffman codes for the symbols in the tree.

        Args:
            node (NodeTree): The current node in the tree.
            left (bool): A flag indicating whether the current node is the left child of its parent.
            bin_string (str): The binary string representing the code for the current node.

        Returns:
            dict: A dictionary mapping symbols to their Huffman codes.
        """
        if type(node) is str:
            return {node: bin_string}
        (left, right) = node.children()
        codes = dict()
        codes.update(self._huffman_code_tree(left, True, bin_string + "1"))
        codes.update(self._huffman_code_tree(right, False, bin_string + "0"))
        codes = sorted(codes.items(), key=lambda x: (len(x[1]), x[1]))
        return dict(codes)

    def _calculate_frequencies(self, list_of_symbols: UnencodedSymbols):
        """
        Calculates the frequencies of the symbols in the list.

        Args:
            list_of_symbols (UnencodedSymbols): The list of symbols.

        Returns:
            list: A list of tuples containing the symbols and their frequencies.
        """
        frequencies = {}
        for symbol in list_of_symbols.unencoded:
            if symbol in frequencies:
                frequencies[symbol] += 1
            else:
                frequencies[symbol] = 1
        return sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    def _build_huffman_tree(self, nodes):
        """
        Builds a Huffman tree from the list of nodes.

        Args:
            nodes (list): A list of nodes where each node is a tuple containing a symbol and its 
            frequency.

        Returns:
            NodeTree: The root node of the Huffman tree.
        """
        while len(nodes) > 1:
            (key1, c1) = nodes[-1]
            (key2, c2) = nodes[-2]
            nodes = nodes[:-2]
            node = NodeTree(key1, key2)
            nodes.append((node, c1 + c2))
            nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
        return nodes[0]

    def encode(self, list_of_symbols: UnencodedSymbols) -> tuple[EncodingMap, EncodedSymbols]:
        """
        Encodes a list of symbols using the Huffman coding algorithm.

        Args:
            list_of_symbols (UnencodedSymbols): The list of symbols to encode.

        Returns:
            tuple[EncodingMap, EncodedSymbols]: The encoding map and the encoded symbols.
        """
        nodes = self._calculate_frequencies(list_of_symbols)
        tree = self._build_huffman_tree(nodes)
        codes = self._huffman_code_tree(tree[0])
        enc_symbols = [codes[symbol] for symbol in list_of_symbols.unencoded]
        return EncodingMap(map=codes), EncodedSymbols(encoded=enc_symbols)
