celsius = float(input("Type temperature in celsius: "))

kelvin = celsius + 273.15
fahrenheit = celsius * 9 / 5 + 32


tekst = "{}*C = {}*F = {}*K"

print(f"{celsius}*C = {fahrenheit}*F = {kelvin}*K")