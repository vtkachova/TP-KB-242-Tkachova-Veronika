a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
op = input("Введіть дію (+, -, *, /): ")

match op:
    case "+":
        print("Результат:", a + b)
    case "-":
        print("Результат:", a - b)
    case "*":
        print("Результат:", a * b)
    case "/":
        if b != 0:
            print("Результат:", a / b)
        else:
            print("Помилка: ділення на нуль!")
    case _:
        print("Невірний оператор!")