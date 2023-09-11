from dictionary.word_frequency import WordFrequency
from dictionary.array_dictionary import ArrayDictionary
import timeit
from collections import namedtuple

def create_arraydict_from_txt(filename):
    arr_dict = ArrayDictionary()

    with open(filename, 'r') as file:
        for line in file:
            word, freq = line.split()
            wf = WordFrequency(word, int(freq))
            arr_dict.add_word_frequency(wf)

    return arr_dict

def find_middle_word_from_dict(array_dict):
    # Get the sorted list of WordFrequency objects from your dictionary
    sorted_word_frequencies = array_dict.dictionary

    # Find the middle word in the sorted list
    middle_index = len(sorted_word_frequencies) // 2
    middle_word = sorted_word_frequencies[middle_index].word

    return middle_word

def search_operation(array_dict, word):
    return array_dict.search(word)

def delete_operation(array_dict, word):
    return array_dict.delete_word(word)

def add_word_frequency_best_case(array_dict, word, frequency):
    wf = WordFrequency(word, frequency)
    return array_dict.add_word_frequency(wf)

def add_word_frequency_worst_case(array_dict, word):
    wf = WordFrequency(word, 0)  # Frequency doesn't matter; it's worst case
    return array_dict.add_word_frequency(wf)

def autocomplete_operation(array_dict, prefix):
    return array_dict.autocomplete(prefix)

def benchmark(func, num_trials, *args):
    total_time = timeit.timeit(lambda: func(*args), number=num_trials)
    return total_time / num_trials

def run_benchmarks_for_file(filename):
    num_trials = 10
    Result = namedtuple('Result', ['action', 'scenario', 'time'])

    array_dict = create_arraydict_from_txt(filename)
    middle_word = find_middle_word_from_dict(array_dict)
    print(f"The word in the middle of the sorted dictionary is: {middle_word}")

    results = []

    results.append(Result('building', 'dictionary', benchmark(create_arraydict_from_txt, num_trials, filename)))

    results.append(Result('searching', 'best case', benchmark(search_operation, num_trials, array_dict, middle_word)))
    results.append(Result('searching', 'worst case', benchmark(search_operation, num_trials, array_dict, 'badWord')))
    results.append(Result('adding', 'best case', benchmark(add_word_frequency_best_case, num_trials, array_dict, 'newWord', 10)))
    results.append(Result('adding', 'worst case', benchmark(add_word_frequency_worst_case, num_trials, array_dict, 'zzzWord')))
    results.append(Result('deleting', 'best case', benchmark(delete_operation, num_trials, array_dict, middle_word)))
    results.append(Result('deleting', 'worst case', benchmark(delete_operation, num_trials, array_dict, 'badWord')))
    results.append(Result('autocompleting', 'best case', benchmark(autocomplete_operation, num_trials, array_dict, 'alahkazam')))
    results.append(Result('autocompleting', 'worst case', benchmark(autocomplete_operation, num_trials, array_dict, 'a')))


    print(f"Results for {filename}:")
    for result in results:
        print(f"Average time taken over {num_trials} trials for {result.action} a {result.scenario} = {result.time} sec")
    print("\n")

if __name__ == "__main__":
    filename = "sampleData200k.txt"
    run_benchmarks_for_file(filename)
