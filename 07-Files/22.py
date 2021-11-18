open("file22.txt", "w").close()
file = open('file22.txt','a')

for i in range(1, 11):
    file.write(f"{i} {i**2} {i**3}\n")

file.close()