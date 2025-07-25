from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculator_operations ={'+': add, '-': subtract, '*': multiply, '/': divide}
calculator_run = True
result = 0
retry = 'n'
while True:
    if retry == 'n':
        first_number = int(input("What is your first number ?"))
        operation = input("choose any of the below operation \n * \n / \n - \n +")
        second_number = int(input("What is your second number ?"))
        result = calculator_operations[operation](first_number, second_number)
    else:
        second_number = int(input("What is your next number ?"))
        operation = input("choose any of the below operation \n * \n / \n - \n +")
        result = calculator_operations[operation](result, second_number)
    print(result)
    retry = input("Press y to continue the calculating, press n to reset the calculator")

    if retry == 'n':
        result = 0

    print("\n" * 40)

