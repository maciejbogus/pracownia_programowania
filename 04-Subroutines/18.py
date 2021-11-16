def sum_of_digits(num):
    suma=0
    while(num>0):
        suma+=num%10
        num-=num%10
        num/=10
    
    return int(suma)
  
print(sum_of_digits(2323))