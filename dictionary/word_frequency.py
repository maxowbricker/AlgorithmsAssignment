
# -------------------------------------------------
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# -------------------------------------------------

# Class representing a word and its frequency
class WordFrequency:
    def __init__(self, word: str, frequency: int):
        self.word = word
        self.frequency = frequency

    def __lt__(self, other):
        # Compare WordFrequency instances based on the 'word' attribute
        return self.word < other.word

