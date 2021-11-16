tab=[1,2,3,4]

def sum(array):
    suma=0
    for i in range(0, len(array)): suma+=array[i]
    return suma

def array2str(array):
    strarray=""
    for i in range(0, len(array)): strarray+=str(f"{array[i]}, ")
    return strarray

print(f"Array: {array2str(tab)}")
print(f"Sum of array: {sum(tab)}")