university=input("Podaj nazwe uczelni: ")
newUniversity = ""

for i in range(len(university)):
    newUniversity += university[i]+" "

print(newUniversity)