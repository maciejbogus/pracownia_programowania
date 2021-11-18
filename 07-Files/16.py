file = open('file.txt','r')
a=0
for line in file:
    print(line, end="")
    a+=1
    if(a==5):
        input("type smth: ")
        a=0
file.close()