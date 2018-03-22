from generic import *
from os import path

counter = 0  # Global var that will be incriminated with each quick_sort call


def get_pivot(arr, low, high):
    """ We have a low index, high index and a middle index. We conpare all
    three and choose the middle"""
    mid = (high + low) // 2  # find the middle
    pivot = high

    if arr[low] < arr[high]:
        if arr[mid] < arr[high]:
            pivot = mid
        elif arr[low] < arr[high]:
            pivot = low
    return pivot


def partition(arr, low, high):
    pivot_index = get_pivot(arr, low, high)
    pivot_val = arr[pivot_index]

    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]  # swap pivot value
    # into leftmost position in the arr
    divider = low  # control point

    for i in range(low, high + 1):
        if arr[i] < pivot_val:
            divider += 1
            arr[i], arr[divider] = arr[divider], arr[i]
    arr[low], arr[divider] = arr[divider], arr[low]

    return divider


"""
 low  --> Starting index,
 high  --> Ending index
"""


# Function to do Quick sort
def quickSort(arr, low, high):
    global counter
    counter += 1

    if low < high:
        # pi is partitioning index
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Function for passing in array
def quick_sort(arr):
    quickSort(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    data = path.relpath('dataForAssignment/Q3to5/102400.txt')
    arr = parse_file(data)
    quick_sort(arr)
    print(f'Quick Sort was called {counter} times while sorting {len(arr)} integers')
