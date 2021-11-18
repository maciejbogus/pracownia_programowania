tab = [1, 23, 5, 382, 1, 17, 4, 906]

for i in tab:
    print("-----", end="")
print("-")

for i in tab:
    print("|{:>4}".format(i), end="")
print("|")

for i in tab:
    print("-----", end="")
print("-")