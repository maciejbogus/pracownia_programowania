tab=[0, 1, 2, 3, 5, 7]
num = 8

def occurs(number, array):
    for i in range(0, len(tab)):
        if array[i] == number: return True
    return False


if occurs(num, tab): print(f"Number {num} appears in the array.")
else: print(f"Number {num} doesn't appear in the array.")