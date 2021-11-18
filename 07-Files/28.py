import re

with open("grades.txt", "r") as file:
    text = file.read()
    grades = re.findall("\d[.]\d",text)

sum=  0
for grade in grades:
    sum += float(grade)
mean = round(sum/len(grades),2)

print(f"Mean of grades: {mean}")