tab=[5, 1, 9, 6, 4, 1]

def minmax(arr):
    new_arr=[]
    new_arr.extend([min(arr), max(arr)])
    return new_arr

print(f"Result: {minmax(tab)}")