from dictionary.word_frequency import WordFrequency
from dictionary.array_dictionary import ArrayDictionary
import time

def create_arraydict_from_txt(filename):
    arr_dict = ArrayDictionary()

    with open(filename, 'r') as file:
        for line in file:
            word, freq = line.split()
            wf = WordFrequency(word, int(freq))
            arr_dict.add_word_frequency(wf)  

    return arr_dict

if __name__ == "__main__":
    filename = "sampleData.txt"
    num_trials = 10
    total_time_build = 0
    total_time_search_best = 0
    total_time_search_worst = 0
    total_time_delete_best = 0
    total_time_delete_worst = 0

    # Average run time for building an array dictionary
    for _ in range(num_trials):
        start_time = time.time()
        array_dict = create_arraydict_from_txt(filename)
        end_time = time.time()
        total_time_build += (end_time - start_time)

    avg_time_build = total_time_build / num_trials
    print(f"Average time taken for building over {num_trials} trials =  {avg_time_build:.5f} sec")

    # Average best case run time for searching a word in the array dictionary
    for _ in range(num_trials):
        start_time = time.time()
        freq = array_dict.search('reclassify')
        end_time = time.time()
        total_time_search_best += (end_time - start_time)

    avg_time_search_best = total_time_search_best / num_trials
    print(f"Average time taken for best case search over {num_trials} trials =  {avg_time_search_best:.5f} sec")

    # Average worst case run time for searching a word in the array dictionary
    for _ in range(num_trials):
        start_time = time.time()
        freq = array_dict.search('eregjergjerigjio')
        end_time = time.time()
        total_time_search_worst += (end_time - start_time)

    avg_time_search_worst = total_time_search_worst / num_trials
    print(f"Average time taken for worst case search over {num_trials} trials =  {avg_time_search_worst:.5f} sec")

    # Average best case run time for deleting a word in the array dictionary
    for _ in range(num_trials):
        start_time = time.time()
        freq = array_dict.delete_word('reclassify')
        end_time = time.time()
        total_time_delete_best += (end_time - start_time)

    avg_time_delete_best = total_time_delete_best / num_trials
    print(f"Average time taken for best case delete over {num_trials} trials =  {avg_time_delete_best:.5f} sec")

    # Average worst case run time for deleting a word in the array dictionary
    for _ in range(num_trials):
        start_time = time.time()
        freq = array_dict.delete_word('eregjergjerigjio')
        end_time = time.time()
        total_time_delete_worst += (end_time - start_time)

    avg_time_delete_worst = total_time_delete_worst / num_trials
    print(f"Average time taken for worst case delete over {num_trials} trials =  {avg_time_delete_worst:.5f} sec")