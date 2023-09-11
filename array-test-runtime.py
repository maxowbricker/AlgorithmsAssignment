from dictionary.word_frequency import WordFrequency
from dictionary.array_dictionary import ArrayDictionary
import time
from collections import namedtuple

def create_arraydict_from_txt(filename):
    arr_dict = ArrayDictionary()

    with open(filename, 'r') as file:
        for line in file:
            word, freq = line.split()
            wf = WordFrequency(word, int(freq))
            arr_dict.add_word_frequency(wf)  

    return arr_dict

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

    array_dict = create_arraydict_from_txt(filename)
    results = []

    results.append(Result('building', 'dictionary', benchmark(create_arraydict_from_txt, num_trials, filename)))

    results.append(Result('searching', 'best case', benchmark(array_dict.search, num_trials, 'btvinfo')))
    results.append(Result('searching', 'worst case', benchmark(array_dict.search, num_trials, 'badWord')))
    results.append(Result('deleting', 'best case', benchmark(array_dict.delete_word, num_trials, 'btvinfo')))
    results.append(Result('deleting', 'worst case', benchmark(array_dict.delete_word, num_trials, 'badWord')))
    results.append(Result('autocompleting', 'best case', benchmark(array_dict.autocomplete, num_trials, 'alahkazam')))
    results.append(Result('autocompleting', 'worst case', benchmark(array_dict.autocomplete, num_trials, 'a')))

    print(f"Results for {filename}:")
    for result in results:
        print(f"Average time taken over {num_trials} trials for {result.action} a {result.scenario} = {result.time} sec")
    print("\n")

if __name__ == "__main__":
    filename = "sampleData200k.txt"
    run_benchmarks_for_file(filename)
