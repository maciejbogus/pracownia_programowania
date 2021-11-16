import random

def rand_elem(arr):
    return arr[random.randint(0, len(arr)-1)]

tab = [1, 2, 32, 4, 6, 2, 7, 5, 43, 54]
print(f"Result: {rand_elem(tab)}")