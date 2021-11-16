tab = ["Red", "Blue", "Green"]

file = open("colors.txt", "w")
for i in range(0, len(tab)):
    file.write(f"{tab[i]} \n")

file.close()