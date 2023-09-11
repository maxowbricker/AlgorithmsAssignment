from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency

class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency
        self.next = None

class LinkedListDictionary(BaseDictionary):

    def __init__(self):
        self.head = None
        self.tail = None

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        for word in words_frequencies:
            self.add_word_frequency(word)

    def search(self, word: str) -> int:
        current = self.head
        while current is not None:
            if current.word_frequency.word == word:
                return current.word_frequency.frequency
            current = current.next
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        if self.search(word_frequency.word) > 0:
            return False
        
        new_node = ListNode(word_frequency)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        return True

    def delete_word(self, word: str) -> bool:
        prev = None
        current = self.head
        while current:
            if current.word_frequency.word == word:
                if prev:
                    prev.next = current.next
                    # If we delete the last element, update the tail pointer
                    if not current.next:
                        self.tail = prev
                else:
                    self.head = current.next
                    # If the head is now None, the list is empty, so update tail to None
                    if not self.head:
                        self.tail = None
                return True
            prev = current
            current = current.next
        return False

    def autocomplete(self, word: str) -> [WordFrequency]:
        matches = []
        current = self.head
        while current is not None:
            if current.word_frequency.word.startswith(word):
                matches.append(current.word_frequency)
            current = current.next
        matches.sort(key=lambda x: x.frequency, reverse=True)
        return matches[:3]
