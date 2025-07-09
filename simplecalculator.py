a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
print("Select operation:")
print("1. +  2. -  3. *  4. /")
operation=input("Select between 1/2/3/4: ")
if operation=='1':
    print("Sum:",a+b)
elif operation=='2':
    print("Difference:",a-b)
elif operation=='3':
    print("Product:",a*b)
elif operation=='4':
    if b != 0:
      print("Quotient:",a/b)
    else:
      print("Division by zero is invalid.")
else:
  print("Invalid operation.")
