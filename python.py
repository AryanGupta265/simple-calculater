#Simple calculator program
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "DIVIDING BY ZERO IS UNDEFINED"
    return a / b

def run_calculator():
    print("-----Welcome to your Simple calculator-----")
    print("You can choose from addition, subtraction, multiplication, and division.\n")

    while True:
        print("Pick your operation:")
        print("1) Add")
        print("2) Subtract")
        print("3) Multiply")
        print("4) Divide")
        operation = input("Type the number of what operation do you want to perform (1-4): ")

        if operation not in ['1', '2', '3', '4']:
            print("!!! Please choose 1, 2, 3, or 4 !!!\n")
            continue

        try:
            n1 = float(input("ENTER THE FIRST NUMBER: "))
            n2 = float(input("ENTER THE SECOND NUMBER: "))
        except ValueError:
            print("YOU ENTERED \n")
            continue

        if operation == '1':
            answer = add(n1, n2)
            print("SUM OF",n1,"AND",n2,"=",answer)
        elif operation == '2':
            answer = subtract(n1, n2)
            print("SUBSTRACTION OF",n1,"AND",n2,"=",answer)
        elif operation == '3':
            answer = multiply(n1,n2)
            print("MULTIPLICATION OF",n1,"AND",n2,"=",answer)
        elif operation == '4':
            answer = divide(n1, n2)
            print("DIVISION OF",n1,"AND",n2,"=",answer)
        again = input("Want to do another calculation? (yes or no): ").strip().lower()
        if again != 'yes':
            print("-----Thanks for using the calculator Have a great day-----")
            break

run_calculator()



















