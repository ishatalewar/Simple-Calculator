print("********CALCULATOR********")

num1=int(input("Enter first number"))
num2=int(input("Enter second number"))

print('''choose an operation from the list

      1. Addition(+)
      2. Subtraction(-)
      3. Multiplication(*)
      4. Divison(/)
      5. Floor Divison(//)
      6. Modulo division(%)
      7. Exponentiation(*)''')

op=int(input("Enter Choice of operation"))
if op == 1:
    print("The value of", num1 ,"+", num2 ,"is", num1+num2)
elif op==2:
    print("The value of", num1, "-", num2, "is", num1 - num2)
elif op == 3:
    print("The value of", num1, "*", num2, "is", num1 * num2)
elif op == 4:
    print("The value of", num1, "/", num2, "is", num1 / num2)
elif op == 5:
    print("The value of", num1, "//", num2, "is", num1 // num2)
elif op == 6:
    print("The value of", num1, "%", num2, "is", num1 % num2)
elif op == 7:
    print("The value of", num1, "**", num2, "is", num1 ** num2)
else:
    print("No such choice")