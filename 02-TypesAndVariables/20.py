import math

height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kg: "))

height=height/100

bmi = round(weight/(height**2), 2)

print(f"Your BMI: {bmi}")