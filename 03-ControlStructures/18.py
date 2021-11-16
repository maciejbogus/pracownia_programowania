kwota = int(input("Podaj kwote: "))

print(f"The amount of PLN {kwota} in coins: ")

zl1=0
zl2=0
zl5=0
while kwota >= 5:
    zl5+=1
    kwota-=5

while kwota >= 2:
    zl2+=1
    kwota-=2

zl1 = kwota

print(f"5 zł: {zl5}")
print(f"2 zł: {zl2}")
print(f"1 zł: {zl1}")