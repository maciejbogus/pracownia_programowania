tab=[5, 1, 9, 6, 4, 1]

def median(arr):
    arr.sort()
    medi=0
    lenght = len(arr)

    if lenght%2==1: medi=arr[int(lenght/2)]

    # średnia z dwóch liczb środkowych, gdy ilość liczb w liście jest parzysta
    else:
        index1 = int((lenght-1)/2)
        index2 = int((lenght+1)/2)
        sum = arr[index1]+arr[index2]
        medi=sum/2
    return medi

print(f"Result: {median(tab)}")