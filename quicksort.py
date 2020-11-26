# 1 2 3 4 1 ----> 1 1 2 3 4
# 15 20 4 14 33 5 2 ---> 2 4 5 14 15 20 33
import random

def quicksort(arr):

    if len(arr) < 2:
        return arr

    pivot = random.choice(arr)
    less = [i for i in arr if i < pivot]
    greater = [i for i in arr if i > pivot]
    same = [i for i in arr if i == pivot]
    return quicksort(less) + same + quicksort(greater)

example_1 = [1, 2, 3, 4, 1]
result_1 = quicksort(example_1)
print(result_1)

example_2 = [15, 20, 4, 14, 33, 5, 2]
result_2 = quicksort(example_2)
print(result_2)