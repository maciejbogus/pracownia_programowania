tab=[5, 1, 9, 6, 4, 1]

def array_as_string(arr):
    str_array=""
    
    for i in range(0, len(arr)):
        str_array+=str(arr[i])
        if(i < len(arr)-1): str_array+=", "

    return str_array

print(f"Result: {array_as_string(tab)}")