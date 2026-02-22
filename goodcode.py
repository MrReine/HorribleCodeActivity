def add(a,b): return a+b
def sub(a,b): return a-b
def mult(a,b): return a*b
def div(a,b):
    if b == 0:
        return "Cannot divide by zero."
    return a/b

def get_nums():
    while True:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            break
        except ValueError:
            print("Please enter a numbers.")
    return num1, num2