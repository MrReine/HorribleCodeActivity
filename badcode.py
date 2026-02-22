#DRY Violation: Each function asks for input from the user and each prints to the console
#Single Responsibility Violation: Each function should only compute the mathematical operations
def add():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    res = num1 + num2
    print(f"The sum is {res}")

def sub():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    res = num1 - num2
    print(f"The difference is {res}")

def mul():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    res = num1 * num2
    print(f"The product is {res}")

def div():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    res = num1 / num2
    print(f"The division is {res}")

def main():
    choice = input("1. Add, 2. Sub, 3. Mult, 4. Div: ")
    if choice == "1": add()
    elif choice == "2": sub()
    elif choice == "3": mul()
    elif choice == "4": div()

if __name__ == "__main__":
    main()