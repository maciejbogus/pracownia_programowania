numbers=[15, 8, 31, 47, 2, 19]

sum=0

for i in range(0, len(numbers)):
    sum+=numbers[i]

print(f"Arithmetic mean: {sum/len(numbers)}")