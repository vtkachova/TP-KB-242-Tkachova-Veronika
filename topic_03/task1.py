print(">>> Калькулятор <<<")

while True:
    op = input("Введіть дію (+, -, *, /) або 'вихід' для завершення: ")
    
    if op == "вихід":
        print("Програма завершена.")
        break

    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    
    

    if op == "вихід":
        print("Програма завершена.")
        break

    if op == "+":
        print("Результат:", a + b)
    elif op == "-":
        print("Результат:", a - b)
    elif op == "*":
        print("Результат:", a * b)
    elif op == "/":
        if b != 0:
            print("Результат:", a / b)
        else:
            print("Помилка: ділення на нуль!")
    else:
        print("Невірний оператор!")

    print()  
