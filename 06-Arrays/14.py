tab=["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

def longest_name(arr):
    max=len(arr[0])
    for i in range(1, len(arr)):
        if(len(arr[i])>max):
            max=len(arr[i])
            number=i
    return arr[number]
print(f"Longest name: {longest_name(tab)}")