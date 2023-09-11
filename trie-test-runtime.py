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

    trie_dict = create_triedict_from_txt(filename)
    results = []

    results.append(Result('building', 'dictionary', benchmark(create_triedict_from_txt, num_trials, filename)))
    
    results.append(Result('searching', 'best case', benchmark(trie_dict.search, num_trials, 'reclassify')))
    results.append(Result('searching', 'worst case', benchmark(trie_dict.search, num_trials, 'badWord')))
    results.append(Result('deleting', 'best case', benchmark(trie_dict.delete_word, num_trials, 'reclassify')))
    results.append(Result('deleting', 'worst case', benchmark(trie_dict.delete_word, num_trials, 'badWord')))
    results.append(Result('autocompleting', 'best case', benchmark(trie_dict.autocomplete, num_trials, 'alahkazam')))
    results.append(Result('autocompleting', 'worst case', benchmark(trie_dict.autocomplete, num_trials, 'a')))

    print(f"Results for {filename}:")
    for result in results:
        print(f"Average time taken over {num_trials} trials for {result.action} a {result.scenario} = {result.time} sec")
    print("\n")

if __name__ == "__main__":
    filenames = ["sampleData.txt"]  # Adjust the list of filenames as needed
    for filename in filenames:
        run_benchmarks_for_file(filename)
