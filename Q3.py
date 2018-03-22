from os import path
from generic import *


def sort_array(arr):
    for i in range(1, len(arr)):  # start with index 1 because the first element is a single element
        position = i  # position moves forward through the iteration
        key = arr[i]  # the key is the current element to be compared

        while position > 0 and arr[position - 1] > key:  # keeping in the array & comparing the element to the
            # left of the key
            arr[position] = arr[position - 1]  # swapping the element to the left of the key with the key
            position -= 1  # decrement the position by 1 step so as to keep track of current position
        arr[position] = key  # break out of while loop and start again from next element
    return arr


if __name__ == '__main__':
    data = parse_file(path.relpath('dataForAssignment/Q3to5/102400.txt'))
    average_run_time(5, sort_array, data)
    print(f'Sorting array of {len(data)} integers')
