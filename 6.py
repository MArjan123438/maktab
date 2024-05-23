#Question 2:
#Recommended time: 5 min
# Write tow separate Python programs to convert temperatures to and from
# celsius, fahrenheit.
# [ Formula : c/5 = f-32/9 [ c = temperature in celsius and f = temperature in
# fahrenheit ]
# Example of the program 1 (C to F):
# input: 60 -> result: 140
# Example of the program 2 (F to C)
# input: 45 -> result: 7


far = float(input("farenheit:"))

cel = (far - 32) * (5/9)

print("celsius :", cel)