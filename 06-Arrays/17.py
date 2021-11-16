tab1=[4, 36, 12, 28, 9, 44, 5] 
tab2=[5, 1, 36]

def f(arr1, arr2):
    a=0
    for i in range(0, len(arr1)):
        for j in range(0, len(arr2)):
            if(arr1[i]==arr2[j]): a+=1
        if a==0: print(arr1[i], end=", ")
        a=0

f(tab1, tab2)