class OperationManager:
    def get_numbers(self):
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        return a, b

    def get_operation(self):
        operation = input("Оберіть операцію (+, -, *, /): ")
        return operation