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

def main():
    operations = {
        "1": (add, "sum"),
        "2": (sub, "difference"),
        "3": (mult, "product"),
        "4": (div, "quotient"),
    }

    while True:
        print("\n--- Calculator ---")
        print("1: Add\n2: Sub\n3: Mult\n4: Div")
        choice = input("Enter your choice: ")

        if choice in operations:
            num1, num2 = get_nums()
            calc_func, op_name = operations[choice]

            result = calc_func(num1, num2)
            print(f"The {op_name} of {num1} and {num2} is {result} ")
            break
        else:
            print("Please enter a valid choice.")

if __name__ == "__main__":
    main()