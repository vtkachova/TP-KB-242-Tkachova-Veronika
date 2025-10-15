# Функції для операцій
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Помилка: ділення на нуль неможливе!"

while True:
    print("\nОберіть операцію: +, -, *, / або 'exit' для виходу")
    op = input("Введіть операцію: ")

    if op.lower() == "exit":
        print("Програма завершена.")
        break

    if op not in ('+', '-', '*', '/'):
        print("Невідома операція. Спробуйте ще раз.")
        continue

    try:
        x = float(input("Введіть перше число: "))
        y = float(input("Введіть друге число: "))

        if op == '+':
            result = add(x, y)
        elif op == '-':
            result = subtract(x, y)
        elif op == '*':
            result = multiply(x, y)
        elif op == '/':
            result = divide(x, y)  

        print(f"Результат: {result}")

    except ValueError:
        print("Помилка: введено не число. Спробуйте ще раз.")
    
