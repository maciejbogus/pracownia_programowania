tab=[1, 4, 2, 5, 32, -1, 3, 21, 32, -2]

def bubblesort(tab):
    for i in range(0, len(tab)):
        for j in range(1, len(tab)-i):
            if tab[j-1]>tab[j]: tab[j], tab[j-1] = tab[j-1], tab[j]
    return tab


print(f"Sorted array: {bubblesort(tab)}")