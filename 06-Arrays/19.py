arr=[1, 5, 2, 3, 2, 3, 4, 5, -1]

def unique(tab):
    unique_el=[]
    n=0

    for i in range(0, len(tab)):

        for j in range(0, len(tab)):
            if tab[i]==tab[j]: n+=1

        if n==1: unique_el.append(tab[i])
        n=0

    return unique_el

print(f"Unique elements: {unique(arr)}")