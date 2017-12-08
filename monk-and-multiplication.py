"""
The Monk learned about priority queues recently and asked his teacher for an interesting problem. So his teacher came up with a simple problem. He now has an integer array A. For each index i, he wants to find the product of the largest, second largest and the third largest integer in the range [1,i].
Note: Two numbers can be the same value-wise but they should be distinct index-wise.

Input:
The first line contains an integer N, denoting the number of elements in the array A.
The next line contains N space separated integers, each denoting the ith integer of the array A.

Output:
Print the answer for each index in each line. If there is no second largest or third largest number in the array A upto that index, then print "-1", without the quotes
"""
from functools import reduce
import time


# Decorator for calculating function processing time
def timeit(method):
    def wrapper(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print("______________________________________________")
        print(te - ts)
        print("______________________________________________")
        return result
    return wrapper


@timeit
def calc(sample_input):
    print(-1)
    print(-1)
    max_sample = sorted(sample_input[0:3], reverse=True)
    prod = reduce(lambda x, y: int(x) * int(y), max_sample[:3])
    print(prod)
    for i, elem in enumerate(sample_input):
        if i > 2:
            if sample_input[i] > max_sample[2]:
                max_sample = sorted(sample_input[0:i + 1], reverse=True)
                prod = reduce(lambda x, y: int(x) * int(y), max_sample[:3])
                print(prod)
            else:
                print(prod)


sample_input = list()
# Taking input from a file.
file_object = open("input.txt", "r")
for line in file_object:
    record = line.split()
    sample_input.extend(record)
    record = ''

# sample_input = '1 2 3 4 5'.split()
sample_input = [int(i) for i in sample_input]

# Calling Function
calc(sample_input)
