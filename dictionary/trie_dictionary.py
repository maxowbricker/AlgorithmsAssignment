from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


# Class representing a node in the Trie
from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency

# Class representing a node in the Trie
class TrieNode:

    def __init__(self, letter=None, frequency=None, is_last=False):
        self.letter = letter            # letter stored at this node
        self.frequency = frequency      # frequency of the word if this letter is the end of a word
        self.is_last = is_last          # True if this letter is the end of a word
        self.children: dict[str, TrieNode] = {}     # a hashtable containing children nodes, key = letter, value = child node


class TrieDictionary(BaseDictionary):

    def __init__(self):
        self.root = TrieNode()  # Initialize an empty Trie

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        Construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        for word, frequency in words_frequencies:
            self.add_word_frequency(WordFrequency(word, frequency))

    def search(self, word: str) -> int:
        """
        Search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        node = self._find_node(word)
        if node and node.is_last:
            return node.frequency
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        Add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        word = word_frequency.word
        frequency = word_frequency.frequency
        node = self.root

        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode(letter)
            node = node.children[letter]

        if node.is_last:
            return False  # Word already exists in the dictionary

        node.is_last = True
        node.frequency = frequency
        return True

    def delete_word(self, word: str) -> bool:
        """
        Delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when word not found
        """
        node = self._find_node(word)
        if node and node.is_last:
            node.is_last = False
            node.frequency = None
            return True
        return False

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        Return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        completions = []
        node = self._find_node(word)

        if node:
            self._find_completions(node, word, completions)

        completions.sort(key=lambda x: x.frequency, reverse=True)
        return completions[:3]

    def _find_node(self, word: str) -> TrieNode:
        node = self.root
        for letter in word:
            if letter not in node.children:
                return None
            node = node.children[letter]
        return node

    def _find_completions(self, node: TrieNode, prefix: str, completions: [WordFrequency]):
        if node.is_last:
            completions.append(WordFrequency(prefix, node.frequency))

        for letter, child_node in node.children.items():
            self._find_completions(child_node, prefix + letter, completions