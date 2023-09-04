from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import bisect


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import bisect


class ArrayDictionary(BaseDictionary):

    def __init__(self):
        # Initialize an empty list to store WordFrequency objects
        self.dictionary = []

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        Construct the data structure to store nodes.
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # Sort the input list of WordFrequency objects alphabetically
        self.dictionary = sorted(words_frequencies, key=lambda wf: wf.word)

    def search(self, word: str) -> int:
        """
        Search for a word.
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # Use binary search to find the word in the sorted list
        index = bisect.bisect_left(self.dictionary, WordFrequency(word, 0))
        
        # Check if the word is found and return its frequency if found
        if index < len(self.dictionary) and self.dictionary[index].word == word:
            return self.dictionary[index].frequency
        else:
            return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        Add a word and its frequency to the dictionary.
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # Use binary search to find the correct position to insert the word
        index = bisect.bisect_left(self.dictionary, word_frequency)
        
        # Check if the word is already in the dictionary
        if index < len(self.dictionary) and self.dictionary[index].word == word_frequency.word:
            return False
        
        # Insert the word at the correct position to maintain alphabetical order
        self.dictionary.insert(index, word_frequency)
        return True

    def delete_word(self, word: str) -> bool:
        """
        Delete a word from the dictionary.
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # Use binary search to find the position of the word
        index = bisect.bisect_left(self.dictionary, WordFrequency(word, 0))
        
        # Check if the word is found and delete it if found
        if index < len(self.dictionary) and self.dictionary[index].word == word:
            del self.dictionary[index]
            return True
        else:
            return False

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        Return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix.
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        # Find all words in the dictionary that have the given prefix
        prefix_length = len(prefix_word)
        matching_words = [wf for wf in self.dictionary if wf.word.startswith(prefix_word)]
        
        # Sort the matching words by frequency in descending order and return at most 3
        sorted_words = sorted(matching_words, key=lambda wf: wf.frequency, reverse=True)
        return sorted_words[:3]
