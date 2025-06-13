# CALCULATOR USING FUNCTIONS 
# Addition
def add(a,b):
    return a+b
# Subtraction
def sub(a,b):
    return a-b
# Multilplication
def multiply(a,b):
    return a*b
# Divide
def divide(a,b):
    if b==0:
        return "Error: Cannot divide by Zero!"
    return a/b
# Main calculator function
def calculator():
    while True:
        print("\n---Menu----")
        print("1.Add")
        print("2.Subtract")
        print("3.Multilply")
        print("4.Divide")
        print("5.Exit")
        choice=input("Choose an option:")
        if choice=="5":
            print("\nThank you for using the calculator\n")
            break
        if choice not in("1","2","3","4"):
            print("Invalid choice.Try again")
            continue
        try:
            num1=float(input("Enter first number:"))
            num2=float(input("Enter Second number:"))
        except ValueError:
            print("Invalid input.Please enters numbers only")
            continue
        if choice=="1":
            print("\nResult:",add(num1,num2))
        if choice=="2":
            print("\nResult:",sub(num1,num2))
        if choice=="3":
            print("\nResult:",multiply(num1,num2))
        if choice=="4":
            print("\nResult:",divide(num1,num2))
calculator()