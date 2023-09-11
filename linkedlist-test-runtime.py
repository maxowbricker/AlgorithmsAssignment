from dictionary.word_frequency import WordFrequency
from dictionary.linkedlist_dictionary import LinkedListDictionary
import time
from collections import namedtuple

def create_linkedlist_from_txt(filename):
    lld = LinkedListDictionary()

    with open(filename, 'r') as file:
        for line in file:
            word, freq = line.split()
            wf = WordFrequency(word, int(freq))
            lld.add_word_frequency(wf)

    return lld

def benchmark(func, num_trials, *args):
    total_time = 0
    for i in range(num_trials):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        total_time += (end_time - start_time)
    return total_time / num_trials

if __name__ == "__main__":
    filename = "sampleData.txt"
    num_trials = 10

    Result = namedtuple('Result', ['action', 'scenario', 'time'])

    linked_list_dict = create_linkedlist_from_txt(filename)
    results = []

    results.append(Result('building', 'dictionary', benchmark(create_linkedlist_from_txt, num_trials, filename)))

    lld_first = linked_list_dict.head.word_frequency.word
    lld_first_auto = lld_first[:4]

    results.append(Result('searching', 'best case', benchmark(linked_list_dict.search, num_trials, lld_first)))
    results.append(Result('searching', 'worst case', benchmark(linked_list_dict.search, num_trials, 'eregjergjerigjio')))
    results.append(Result('deleting', 'best case', benchmark(linked_list_dict.delete_word, num_trials, lld_first)))
    results.append(Result('deleting', 'worst case', benchmark(linked_list_dict.delete_word, num_trials, 'eregjergjerigjio')))
    results.append(Result('autocompleting', 'best case', benchmark(linked_list_dict.autocomplete, num_trials, lld_first_auto)))
    results.append(Result('autocompleting', 'worst case', benchmark(linked_list_dict.autocomplete, num_trials, 'eregjergjerigjio')))

    for result in results:
        print(f"Average time taken over {num_trials} trials for {result.action} {result.scenario} = {result.time:.5f} sec")