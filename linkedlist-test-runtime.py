from dictionary.word_frequency import WordFrequency
from dictionary.linkedlist_dictionary import LinkedListDictionary
import time

def create_linkedlist_from_txt(filename):
    lld = LinkedListDictionary()

    with open(filename, 'r') as file:
        for line in file:
            word, freq = line.split()
            wf = WordFrequency(word, int(freq))
            lld.add_word_frequency(wf)  

    return lld

if __name__ == "__main__":

    filename = "sampleData.txt"
    num_trials = 10
    total_time = 0
    total_timeB = 0
    total_timeW = 0
    total_timeDB = 0
    total_timeDW = 0
    total_timeAB = 0 
    
    # Average run time for building a linked list dictionary
    for _ in range(num_trials):
        start_time = time.time()
        linked_list_dict = create_linkedlist_from_txt(filename)
        end_time = time.time()

        total_time += (end_time - start_time)

    avg_time = total_time / num_trials
    print(f"Average time taken over {num_trials} trials for building a dictionary =  {avg_time:.5f} sec")

    lld_first = linked_list_dict.head.word_frequency.word
    lld_first_auto = lld_first[:4]

    # Average best case run time for searching a word in the linked list dictionary
    for _ in range(num_trials):
        start_time = time.time()
        freq = linked_list_dict.search(lld_first)
        end_time = time.time()

        total_timeB += (end_time - start_time)

    avg_timeB = total_timeB / num_trials
    print(f"Average best time taken over {num_trials} trials for searching for a word =  {avg_timeB:.5f} sec")

    # Average worst case run time for searching a word in the linked list dictionary
    for _ in range(num_trials):
        start_time = time.time()
        freq = linked_list_dict.search('eregjergjerigjio')
        end_time = time.time()

        total_timeW += (end_time - start_time)

    avg_timeW = total_timeW / num_trials
    print(f"Average worst time taken over {num_trials} trials for searching for a word =  {avg_timeW:.5f} sec")

    # Average best case run time for deleting a word in the linked list dictionary
    for _ in range(num_trials):
        start_time = time.time()
        freq = linked_list_dict.delete_word(lld_first)
        end_time = time.time()

        total_timeDB += (end_time - start_time)

    avg_timeDB = total_timeDB / num_trials
    print(f"Average best time taken over {num_trials} trials for deleting a word =  {avg_timeDB:.5f} sec")

    # Average worst case run time for deleting a word in the linked list dictionary
    for _ in range(num_trials):
        start_time = time.time()
        freq = linked_list_dict.delete_word('eregjergjerigjio')
        end_time = time.time()

        total_timeDW += (end_time - start_time)

    avg_timeDW = total_timeDW / num_trials
    print(f"Average worst time taken over {num_trials} trials for deleting a word =  {avg_timeDW:.5f} sec")

    # Average best case run time for autocompleting a word in the linked list dictionary
    for _ in range(num_trials):
        start_time = time.time()
        suggestions = linked_list_dict.autocomplete(lld_first_auto)  # Use a prefix expected to be common for best case
        end_time = time.time()

        total_timeAB += (end_time - start_time)

    avg_timeAB = total_timeAB / num_trials
    print(f"Average best time taken for autocomplete over {num_trials} trials = {avg_timeAB:.5f} sec")

    # Average worst case run time for autocompleting a word in the linked list dictionary
    total_timeAW = 0  # Total time for autocomplete worst case
    for _ in range(num_trials):
        start_time = time.time()
        suggestions = linked_list_dict.autocomplete('eregjergjerigjio')  # Use a prefix not expected to be in the data for worst case
        end_time = time.time()

        total_timeAW += (end_time - start_time)

    avg_timeAW = total_timeAW / num_trials
    print(f"Average worst time taken for autocomplete over {num_trials} trials = {avg_timeAW:.5f} sec")