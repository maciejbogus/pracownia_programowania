open("file20.txt", "w").close()
file = open('file20.txt','a')

for i in range(1, 51):
    file.write(f"{str(i)}\n")

file.close()