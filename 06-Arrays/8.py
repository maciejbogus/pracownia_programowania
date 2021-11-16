import sys

numbers=[-15, 8, -31, 47, -2, 19]
min=numbers[0]
max=numbers[0]

for i in range(0, len(numbers)):
    if(numbers[i]<min): min=numbers[i]
    if(numbers[i]>max): max=numbers[i]

print(f"MIN: {min}, MAX: {max}")