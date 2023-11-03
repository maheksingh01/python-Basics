a = float(input("Enter first number : "))
b = float(input("Enter second number : "))
op = input("Enter the operator : ")

#calculatiom

#addition
if(op == "+"):
    print(a+b)

#substraction
elif(op == "-"):
    print(a-b)

#multiplication
elif(op == "*"):
    print(a*b)

#divison
elif(op == "/" and b != 0):
    print (a/b)

#else
else:
    print("invalid operator")