from generic import *
from os import path


def create_sub_arrays(data, n):
    arr = parse_file(data)
    data_chunks = list(arr[:n:])  # slice the array & append to list
    return data_chunks


####################################################################################################################
####################################################################################################################


"""
MergeSort --> Divide & Conquer --> This algorithm has two big ideas, the first is to continually divide the problem
until a size of one is achieved, this is done recursively. The second big idea is the merging and sorting
of each of the singular elements, sorting as we merge until finally we are left with a sorted array of
size n.
"""


def merge_sort(arr):
    """
    Recursive function that calls itself until the input is an array of size 1
    :param arr: unsorted array of size n
    :return: calls the merge function when the array dept is (1+log n) and we have n number of leaves
    """

    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


def merge(left, right):
    i, j = 0, 0  # i (left array index), j (right array index)
    sorted_arr = []  # initialized empty array to which we can append elements in order of size

    while i < len(left) and j < len(right):  # ensure we don't over shoot the arrays
        if left[i] < right[j]:  # conditionally sort the elements based on size and add to the empty list
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    if i == len(left) or j == len(right):  # which ever array we sort through first i.e left or right
        sorted_arr.extend(left[i:] or right[j:])  # join the left overs from the other to the end as they will by
    # default be larger and already sorted
    return sorted_arr


########################################################################################################################
########################################################################################################################


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
 The main function that implements QuickSort
 low  --> Starting index,
 high  --> Ending index
"""


# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Function for passing in array
def quick_sort(arr):
    quickSort(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    data_txt = path.relpath('dataForAssignment/Q3to5/102400.txt')
    sizes = [6400, 12800, 25600, 51200, 102400]

    for n in sizes:
        arr = create_sub_arrays(data_txt, n)

        average_run_time(5, merge_sort, arr)
        print(f'Sorting array of {len(arr)} integers')

        average_run_time(5, quick_sort, arr)
        print(f'Sorting array of {len(arr)} integers')
