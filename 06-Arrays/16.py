numbers=[2,4,3, 21]

def stars(arr):
    for i in range(0, len(arr)):
        print(arr[i], end=": ")
        for j in range(0, arr[i]):
            print("*", end="")
        print()

stars(numbers)