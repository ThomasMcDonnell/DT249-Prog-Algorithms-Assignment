# Title:

DT249 Programming Paradigms and Data Structures - Analysis of Algorithms


# Objective:

The aim of this report is to accurately compare and contrast the running times of a number of different sorting algorithms when given arrays of varying size (n) and order to sort.  


# Introduction:

We will be comparing the performance of three sorting algorithms when given arrays of varying size and order. 

Insertion Sort ==> The idea of this algorithm is to build your sorted array in place, shifting elements out of the way if necessary to make room as you go. This algorithm has a running worst case of O(n**2), as the key moves takes O(n) and the swaps and comparisons also take O(n).

Merge Sort ==> Divide & Conquer algorithm —> This algorithm has two big ideas, the first is to continually divide the problem until a size of one is achieved, this is done recursively. The second big idea is the merging and sorting of each of the singular elements, sorting as we merge until finally we are left with a sorted array of size n. The time complexity of Merge Sort is 0(n log n) in all three cases (best, average & worst) as the array given is always divided into two halves and the merge operation takes linear time.

Quick Sort ==> Divide and Conquer algorithm —> This algorithm has two main phases, the partition phase and the sort phase. The sorting of the array is a relatively simple recursive function that simply sorts the two smaller problems generated by the partitioning. The partition phase works out where to split the array by picking an element as pivot and partitioning the given array around the pivot. There are many different versions of quickSort that pick a pivot in different ways.
	1.	Always pick first element as pivot.
	2.	Always pick last element as pivot.
	3.	Pick a random element as pivot.
	4.	Pick median as pivot (implemented in this experiment).
The partition function which given an array of size n and an element x of an array as the pivot, it puts x at its correct position in the sorted array by putting all elements (smaller than x) before x, and all elements (greater than x) after x. Quick Sort is the trickiest of all the above sorting algorithms as its time complexity is very much dependent on its implementation (as we will see) and the array given. 



# Methods:

Following the outline of the brief specified through questions 1 - 5, this report found commonality in the reading of integers from text files and calculating an average running time so for this reason two separate functions were written and kept modular (parse_file function & average_run_time function). The parse_file function takes in a file and appends the integers within to an array which can that be passed to be sorted. The average_run_time function takes a cycle number, a function and any number of function arguments and runs the function for specified cycles and out putting the average time taken over the cycles to run the function. These functions were than imported and used in all files Q1, Q2, Q3, Q4 and Q5 as needed. In order to pass the direct path of the file to the parse_file function the path method from the os module was used because of this any wishing to replicate this report may need to alter the path slightly to accommodate Windows paths or older systems.  



## Q1:
The brief was to generate timings for Insertion Sort, sorting the numbers in the six files contained in folder Q. For this the code for Insertion Sort was modified slightly to incorporate the parse_file function and include the time.clock code blocks which generate the times. The function, instead of returning a sorted array, returns the time taken to sort the array as well as the size of the given array. 
A simple loop was used to loop through the different files and given them in turn to Insertion Sort to sort. 

## Q2:
The same code was used here (copy & paste) but run in a file of its own for the shake of cleanliness. Again as in Q1 a simple loop was used to give the Insertion Sort its arrays to be sorted.  

## Q3:
Using the timings generated form Q1 a model was drafted to estimate the running time of Insertion Sort given an array of 102400 integers.

In order to compare this model to Insertion Sorts actual time, the report generated timings  of insertion Sort sorting 102400 integers. The same code was used however with some slight adjustments being made. The code was reverted back to its original state and the average_run_time function was used to run Insertion Sort 5 times and get the average time taken. 

## Q4:
Here the brief was to compare and contrast Merge Sort and Quick Sort by generating timings for both sorting an array of a number of differing sizes. This was probably the trickiest of all the briefs and required a few work arounds in order to implement. 

As with all previous briefs, the code was written for the two sorting algorithms, Merge Sort and Quick Sort. The first problem was to generate a number of smaller arrays from a larger array. A separate function, create_sub_arrays, was created to do this. The create_sub_arrays function takes in an array and a size (n) and then slices the array to the specified size and than returns this array.  A simple loop could than be used to give different sizes to the function and give each new sub array in turn to Merge_Sort and Quick_Sort.

## Q5:
The last of the briefs was to count how many times the recursive function Quick Sort was called given an array of size N. For this the same Quick Sort code (copy & paste) was used with a slight modification, each time the quick_sort function is called a global var counter is incremented by one. The array could then be given and and the counter could be printed to the screen giving the results (how many recursive calls per array size N). 


# Results:


## Q1 & Q2: Timing of insertion sort when sorting n length arrays of integers

N (size of array) | Time (seconds)
----------------- | ----------------------
1600 | 0.134283
3200 | 0.5562480000000001
6400 | 2.2325399999999997
12800 | 8.833151
25600 | 35.046197
51200 | 140.777436

---

## Q2: Timing of Insertion Sort when sorting arrays of integers varying not in size but order

N (size of array) | Time (seconds)
----------------- | ----------------------
25600 | 0.0044189999999999785
25600 | 35.101984
25600 | 70.163985


---
## Q3 Estimation of Running Time Vs Actual Running Time

N (size of array) | Time (seconds)| Ratio of Times   | Log of Ratio
----------------- | --------------|------------------|-------------------
1600 | 0.134283 |
3200 | 0.5562480000000001| 4.14 |2.05
6400 | 2.2325399999999997| 4.02 |2.02
12800 | 8.833151| 3.96 |1.99
25600 | 35.046197| 3.96 |1.99
51200 | 140.777436 | 4.01 |2.01

### Converging (Log of Ratio) ==>  2

### Average Running Time ==> 	a N**b

b = 2
2.2 = a x 6400**2
a =   2.2 / 6400**2
a = 5.37 x 10** -8

5.37 x 10** -8 N**2

 (size of array) | Time (seconds) | Estimated Time
----------------- | ---------------|-------
102400 | 610.8698190000001 | 563.2

---

## Q4 Average Merge Sort & Quick Sort times generated over 5 cycles for arrays of increasing size

N (size of array) |       Algorithm | Time (seconds)| Algorithm      | Time (seconds)|
----------------- | --------------- |---------------|----------------|---------------|
6400 | merge_sort| 0.0338198 | quick_sort | 0.0156358
12800 |  merge_sort| 0.07173260000000001 | quick_sort | 0.02989200000000001
25600| merge_sort| 0.15169019999999994 | quick_sort | 0.06630799999999999
51200 | merge_sort| 0.3329866 | quick_sort | 0.13717639999999998
102400 | merge_sort| 0.6974495999999999 | quick_sort | 0.30128460000000035

---

## Q5.py

Quick Sort was called 136697 times while sorting 102400 integers


# Discussion:

## Q1, Q2, Q3:

Insertion sort sorts by starting at index 1 (second element in the array) because index 0 (the first element in the array) is a single element and by definition is already sorted and copying the element here to a variable (Key). We then precede to compare the element to the left with the key, if the element to the left is smaller than the key we do nothing and the process repeats moving forward one. If on the other hand the element is larger we shift the element forward one and back to compare to the left again. This process of continually moving left until the condition (Key is no longer larger than the element) holds true is where we start to see the time complexity of this algorithm. Given an array of size n we may need to make n moves in order to place any given element in its correct position in the array.
For this reason Insertion Sort takes a maximum time (O(n**2)) to sort an array in reverse order and a minimum time (O(n)) if the elements are already sorted. Thus fitting in perfectly with our observations here in both Q1 and Q2.
In Q1 as the input array size increases the time taken to sort the array also increases in a quadratic fashion.
In Q2 the first array is already sorted and thus takes a minimum time, the second array is intermixed and thus takes much longer the first and is the average and finally the last array is in reverse order and we see a worst case performance of Insertion Sort.
In Q3 the results generated from Q1 were plotted on a line graph and we see a beautiful example of a quadratic function. In order to estimate the running time of the algorithm given an array of size 102400 the slope of the line was calculated and the formula:

a N ** b
Where a is the constant, N is the size of the array and b is the slope of the line generated. Insertion sort was then given an array of size 102400 and when comparing the result to that of the estimated running time we see that the two are extremly close with only slight variation.

## Q4:

Here we compared both Merge Sort and Quick Sort when given the same input arrays to sort. This is where things got interesting, the Quick Sort algorithm as implemented first by not efficiently picking a pivot was unable to sort arrays larger than 7000 as python has a maximum recursion dept of 1000. In order to combat this the code was altered to be more efficient using the medium of three pivot rule. By doing this Quick Sort was then able to generate timings for all arrays given. By comparing the results seen in table 1.3 we see that although both algorithms are of the same time complexity, Quick Sort emerges the victor. Quick Sort in its general form is an in-place sort (it doesn’t require any extra storage) whereas merge sort requires O(N) extra storage, N denoting the array size which can be quite expensive. Allocating and de-allocating the extra space used for merge sort increases the running time of the algorithm and so comparing average complexity we find that both type of sorts have O(N log N) average complexity but the constants are what set these two apart. For arrays given here in this experiment, merge sort loses due to the use of extra O(N) storage space.

## Q5:
A simple check of how many times Quick Sort calls itself recursively while sorting an array of size N. As can be seen when given an array of size 102400 integers the Quick Sort function was called 136697 times.

