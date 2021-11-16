tab=[5, 1, 9, 6, 4, 1]

def separate(arr):
    new_arr=[]
    arr.sort()
    odd = False
    for j in range(0, 2):
        for i in range(0, len(arr)):
            if(odd==False and arr[i]%2==0): new_arr.append(arr[i])
            elif(odd==True and arr[i]%2==1): new_arr.append(arr[i])
        odd = True
    return new_arr

print(f"Result: {separate(tab)}")