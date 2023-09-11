import random

# Read the list of common English words from the "word_list.txt" file
with open('word_list.txt', 'r') as file:
    common_words = [line.strip() for line in file]

# Shuffle the list of common words to ensure randomness
random.shuffle(common_words)

# Generate a number of lines
num_lines = 20000

# Create and open the output file
with open('generated-txt.txt', 'w') as file:
    for _ in range(num_lines):
        # Ensure that we don't run out of words by looping through the list
        if not common_words:
            random.shuffle(common_words)  # Shuffle the list again if we've used all the words
        # Choose a word from the list (and remove it to avoid duplicates)
        word = common_words.pop()
        # Generate a random number between 1000 and 1000000
        number = random.randint(1000, 1000000)
        # Write the word and number to the file
        file.write(f"{word}  {number}\n")
