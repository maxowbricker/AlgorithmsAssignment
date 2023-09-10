from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency
import time

class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency
        self.next = None

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class LinkedListDictionary(BaseDictionary):

    def __init__(self):
        
        self.head = None
        self.tail = None

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """

        for word in words_frequencies:
            self.add_word_frequency(word)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """

        current = self.head
        while current is not None:
            if current.word_frequency.word == word:
                return current.word_frequency.frequency
            current = current.next
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        if self.search(word_frequency.word) > 0:
            return False
        
        new_node = ListNode(word_frequency)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            self.tail.next = new_node
            self.tail = new_node

        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """

        prev = None
        current = self.head
        while current:
            if current.word_frequency.word == word:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False


    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """

        # Initialize an empty list to hold words that match the prefix
        matches = []

        # Start from the head of the linked list
        current = self.head

        # Loop through the linked list
        while current is not None:
            if current.word_frequency.word.startswith(word):
                # If the word in the current node starts with the prefix, add it to matches
                matches.append(current.word_frequency)

            # Move to the next node
            current = current.next

        # Sort the matching words by frequency, in descending order
        matches.sort(key=lambda x: x.frequency, reverse=True)

        # Take the top 3 most frequent words
        return matches[:3]