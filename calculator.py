def Addition(x,y):
    return x + y
    
def Subtraction(x,y):
    return x - y
    
def Multiplication(x,y):
    return x * y
    
def Division(x,y):
    if y==0:
        print("denominator is zero,Error")
    return x / y
    
def calculator():
    print("CALCULATOR")
    print("Operations that you can perform: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divison")
    
    choices=int(input("Enter the operation number you want to perform: "))
    if choices not in [1,2,3,4]:
        print("Wrong input")
    number1=float(input("Enter the first number: "))
    number2=float(input("Enter the second number: "))
    
    if choices==1:
        result=Addition(number1,number2)
        operator="+"
    elif choices==2:
        result=Subtraction(number1,number2)
        operator="-"
    elif choices==3:
        result=Multiplication(number1,number2)
        operator="*"
    elif choices==4:
        result=Division(number1,number2)
        operator="/"
    print(f"{number1} {operator} {number2} = {result}")
calculator()
