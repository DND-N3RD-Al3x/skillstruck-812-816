num1 = int(input("Give me a number: "))

num2 = int(input("Give me a second number: "))

num3 = int(input("Give me a third number: "))

if num2 < num1 < num3 or num2 < num3 < num1:
    print(num2)

elif num1 < num2 < num3 or num1 < num3 < num2:
    print(num1)

elif num3 < num1 < num2 or num3 < num2 < num1:
    print(num3)