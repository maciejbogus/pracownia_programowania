read_file = open("file.txt", "r")
write_file = open("copylines.txt", "w")

for line in read_file:
    write_file.write(line)

read_file.close()
write_file.close()