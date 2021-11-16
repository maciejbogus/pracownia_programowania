def display_reverse_array(arr):
    for i in range(len(arr)-1, -1, -1):
        print(arr[i], end=" ")
        
tab=[1, 2, 3, 4]
display_reverse_array(tab)