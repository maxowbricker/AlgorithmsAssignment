from dictionary.word_frequency import WordFrequency
from dictionary.trie_dictionary import TrieDictionary
import time
from collections import namedtuple

def create_triedict_from_txt(filename):
    trie_dict = TrieDictionary()

    with open(filename, 'r') as file:
        for line in file:
            word, freq = line.split()
            wf = WordFrequency(word, int(freq))
            trie_dict.add_word_frequency(wf)

    return trie_dict

def benchmark(func, num_trials, *args):
    total_time = 0
    for _ in range(num_trials):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        total_time += (end_time - start_time)
    return total_time / num_trials

def run_benchmarks_for_file(filename):
    num_trials = 10
    Result = namedtuple('Result', ['action', 'scenario', 'time'])
    small_word = WordFrequency("a", 123)
    big_word = WordFrequency("pneumonoultramicroscopicsilicovolcanoconiosis", 6328739)
    bigger_word = WordFrequency("Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch", 759834)

    trie_dict = create_triedict_from_txt(filename)
    results = []

    results.append(Result('building', 'dictionary', benchmark(create_triedict_from_txt, num_trials, filename)))
    
    results.append(Result('searching', 'best case', benchmark(trie_dict.search, num_trials, 'a')))
    results.append(Result('searching', 'worst case', benchmark(trie_dict.search, num_trials, big_word.word))) 
    results.append(Result('adding', 'best case', benchmark(trie_dict.add_word_frequency, num_trials, small_word)))
    results.append(Result('adding', 'worst case', benchmark(trie_dict.add_word_frequency, num_trials, bigger_word)))
    results.append(Result('deleting', 'best case', benchmark(trie_dict.delete_word, num_trials, 'a')))
    results.append(Result('deleting', 'worst case', benchmark(trie_dict.delete_word, num_trials, big_word.word)))
    results.append(Result('autocompleting', 'best case', benchmark(trie_dict.autocomplete, num_trials, 'alahkazam')))
    results.append(Result('autocompleting', 'worst case', benchmark(trie_dict.autocomplete, num_trials, 'a')))

    print(f"Results for {filename}:")
    for result in results:
        print(f"Average time taken over {num_trials} trials for {result.action} a {result.scenario} = {result.time} sec")
    print("\n")

if __name__ == "__main__":
    filenames = ["500-generated.txt", "2k-generated.txt", "5k-generated.txt", "10k-generated.txt", "20k-generated.txt", "sampleData200k.txt", ]  # Adjust the list of filenames as needed
    for filename in filenames:
        run_benchmarks_for_file(filename)
