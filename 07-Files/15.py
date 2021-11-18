file_name = input("Type file name: ")

file = open(file_name,'r')

i=0
for line in file:
    i+=1

file.close()
print(f"File name: {file_name}")
print(f"Numbers of lines: {i}")