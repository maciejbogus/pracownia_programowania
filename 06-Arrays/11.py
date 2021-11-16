def compare(arr1, arr2):
    if len(arr1)!=len(arr2): return False
    for i in range(0, len(arr1)):
        if(arr1[i]!=arr2[i]): return False
    return True

a1=[1, 2, 3]
a2=[1, 2, "3"]

print(compare(a1, a2))