import stack

def binary(n):
    while(n>0):
        stack.push(n%2)
        n=int((n/2))
binary(18)
while(True):
    n = stack.pop()
    if(n==None): break
    print(n, end="")