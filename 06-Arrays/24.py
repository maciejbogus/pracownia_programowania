tab=[5, 1, 9, 6, 4, 1]

def grater(arr, num):
    new_arr = []
    for i in range(0, len(arr)):
        if(num<arr[i]): new_arr.append(arr[i])
    return new_arr

print(f"Result: {grater(tab, int(input('Podaj liczbe: ')))}")