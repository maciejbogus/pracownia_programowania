import random

open("file21.txt", "w").close()
file = open('file21.txt','a')

for i in range(1, 51):
    file.write(f"{random.randint(100,999)}\n")

file.close()