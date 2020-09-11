# Chapter 10 - If statements

a = 6
b = 8

if a < b:
    print("a is less than b")

if a > b:
    print("a is greater than b")

if a <= b:
    print("a is less than or equal to b")

if a >= b:
    print("a is greater than or equal to b")

if a == b:
    print("a is equal to b")

if a != b:
    print("a is not equal to b")

temperature = float(input("What is the temperature in Fahrenheit?"))

print("The temp is", temperature)

if temperature > 90:
    print("It is hot outside!")
elif temperature < 30:
    print("It is cold outside")
else:
    print("It is not so hot outside")


for i in range(5):
    print("I will not chew gum in class.")
