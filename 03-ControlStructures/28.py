import math

n = int(input("Podaj n: "))
factors = 0

for i in range (2, n+1):
    for j in range (1, int(math.ceil(math.sqrt(i)))+1):
        if(i%j == 0): factors+=1
        if(factors>1): break
    if(factors == 1): print(i, end=", ")
    factors = 0

# n = int(input("Podaj n: "))
# factors = 0

# for i in range (2, n+1):
#     for j in range (1, i):
#         if(i%j == 0): factors+=1
#     if(factors == 1): print(i, end=", ")
#     factors = 0
