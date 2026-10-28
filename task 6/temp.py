def convert_temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

c = float(input("Enter temperature in Celsius: "))

f = convert_temperature(c)
print(f"Temperature in Fahrenheit: {f:.2f}")
