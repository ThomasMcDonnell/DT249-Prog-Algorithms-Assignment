from os import path
import time
from generic import *


def sort_array(file):
    arr = parse_file(file)
    time_0 = time.clock()
    for i in range(1, len(arr)):  # start with index 1 because the first element is a single element
        position = i  # position moves forward through the iteration
        key = arr[i]  # the key is the current element to be compared

        while position > 0 and arr[position - 1] > key:  # keeping in the array & comparing the element to the
                                                        # left of the key
            arr[position] = arr[position - 1]  # swapping the element to the left of the key with the key
            position -= 1  # decrement the position by 1 step so as to keep track of current position
        arr[position] = key  # break out of while loop and start again from next element
    time_1 = time.clock() - time_0
    print(f'It took {time_1} seconds to sort {len(arr)} integers')


if __name__ == '__main__':
    """ Set each of the file paths and save to an iterable list. Iterate over
    the list and feed each of the files to be sorted by insertion sort"""
    file_1 = path.relpath('dataForAssignment/Q1/1600.txt')
    file_2 = path.relpath('dataForAssignment/Q1/3200.txt')
    file_3 = path.relpath('dataForAssignment/Q1/6400.txt')
    file_4 = path.relpath('dataForAssignment/Q1/12800.txt')
    file_5 = path.relpath('dataForAssignment/Q1/25600.txt')
    file_6 = path.relpath('dataForAssignment/Q1/51200.txt')
    text_files = [file_1, file_2, file_3, file_4, file_5, file_6]
    for _file in text_files:
        sort_array(_file)
