file = open('countries.txt','r')
a=1

for line in file:
    print(f"{a}: {line}", end="")
    a+=1

file.close()