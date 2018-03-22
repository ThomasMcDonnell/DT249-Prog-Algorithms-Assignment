import time


"""
modular function for reading a .txt file of integers and out putting the result
into a global variable array

"""


def parse_file(file):
    with open(file, 'r') as f:  # open and read the file
        data = f.read()

    array = [int(i) for i in data.split()]  # append integer in file to array
    return array


def average_run_time(run_cycle, function, *args):
    """Function calculates the average run time over the cycles given"""
    total_time = 0
    for _ in range(run_cycle):
        start_time = time.clock()
        result = function(*args)
        total_time += time.clock() - start_time
    average_time = total_time / run_cycle
    print(f'Average {function} time: {average_time}')


if __name__ == '__main__':
    main()
