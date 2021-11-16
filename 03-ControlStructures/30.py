a = 0
b = 1
n=int(input("Podaj n: "))
  
for i in range (0, n):
    print(b, end=", ")
    b += a
    a = b-a