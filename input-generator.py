import random

# Read the list of common English words from the "word_list.txt" file
with open('word_list.txt', 'r') as file:
    common_words = [line.strip() for line in file]

# Shuffle the list of common words to ensure randomness
random.shuffle(common_words)

# Generate a random number of lines between 5 and 15
num_lines = random.randint(5, 15)

# List of possible actions: S, AC, D, A
actions = ['S', 'AC', 'D', 'A']

# Create and open the output input file
with open('input.in', 'w') as file:
    for _ in range(num_lines):
        # Ensure that we don't run out of words by looping through the list
        if not common_words:
            random.shuffle(common_words)  # Shuffle the list again if we've used all the words
        # Choose a random word from the list (and remove it to avoid duplicates)
        word = common_words.pop()
        # Choose a random action from the list of actions
        action = random.choice(actions)
        # Write the action and word to the input file
        if action == 'S':
            file.write(f"S {word}\n")
        elif action == 'AC':
            file.write(f"AC {word}\n")
        elif action == 'D':
            file.write(f"D {word}\n")
        elif action == 'A':
            file.write(f"D {word}\n")
