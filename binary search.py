import random

def bubble_sort(arr):
    lenght = len(arr)
    for i in range(lenght-1):
        for j in range(i+1,lenght):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def binary_search(arr, number):
    counter = 0
    arr = bubble_sort(arr)
    guess = True

    while guess:
        median_index = int(len(arr)/2)
        arr_median = arr[median_index]
        if arr_median > number:
            arr = arr[:median_index]
        if arr_median < number:
            arr = arr[median_index:]
        if arr_median == number:
            guess = False

        counter = counter + 1
        if len(arr) == 1 and arr_median != number:
            print('there is no number in the list')
            break
    return counter

#array = list(map(int, input().split()))

amount_of_values = int(input())
array = [random.randrange(20) for i in range(amount_of_values)]
number = random.choice(array)

print(f'lenght of list is: {amount_of_values}')
print(f'list values: {array}' + f'---->{sorted(array)}')
print(f'random number to guess: {number}')
print(f'quantity of loops: {binary_search(array, number)}')
