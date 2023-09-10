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

    # Average run time for building a linked list dictionary
    for _ in range(num_trials):
        start_time = time.time()
        linked_list_dict = create_linkedlist_from_txt(filename)
        end_time = time.time()

        total_time += (end_time - start_time)

    avg_time = total_time / num_trials
    print(f"Average time taken over {num_trials} trials =  {avg_time:.5f} sec")

    # Average best case run time for searching a word in the linked list dictionary
    for _ in range(num_trials):
        start_time = time.time()
        freq = linked_list_dict.search('reclassify')
        end_time = time.time()

        total_timeB += (end_time - start_time)

    avg_timeB = total_timeB / num_trials
    print(f"Average time taken over {num_trials} trials =  {avg_timeB:.5f} sec")

    # Average worst case run time for searching a word in the linked list dictionary
    for _ in range(num_trials):
        start_time = time.time()
        freq = linked_list_dict.search('eregjergjerigjio')
        end_time = time.time()

        total_timeW += (end_time - start_time)

    avg_timeW = total_timeW / num_trials
    print(f"Average time taken over {num_trials} trials =  {avg_timeW:.5f} sec")

    # Average best case run time for deleting a word in the linked list dictionary
    for _ in range(num_trials):
        start_time = time.time()
        freq = linked_list_dict.delete_word('reclassify')
        end_time = time.time()

        total_timeDB += (end_time - start_time)

    avg_timeDB = total_timeDB / num_trials
    print(f"Average time taken over {num_trials} trials =  {avg_timeDB:.5f} sec")

    # Average worst case run time for deleting a word in the linked list dictionary
    for _ in range(num_trials):
        start_time = time.time()
        freq = linked_list_dict.delete_word('eregjergjerigjio')
        end_time = time.time()

        total_timeDW += (end_time - start_time)

    avg_timeDW = total_timeDW / num_trials
    print(f"Average time taken over {num_trials} trials =  {avg_timeDW:.5f} sec")