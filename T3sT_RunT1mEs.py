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

    start_time = time.time()
    linked_list_dict = create_linkedlist_from_txt(filename)
    end_time = time.time()


    print(f"Time taken =  {(end_time - start_time):.2f} sec")

    # If you wish to test whether the LinkedListDictionary has been populated correctly:
    # word = "skywalker"
    # print(f"Frequency of '{word}' is: {linked_list_dict.search(word)}")