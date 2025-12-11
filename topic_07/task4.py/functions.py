class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return "Помилка: ділення на нуль!"
        return a / b

    def calculate(self, op, a, b):
        if op == '+':
            return self.add(a, b)
        elif op == '-':
            return self.sub(a, b)
        elif op == '*':
            return self.mul(a, b)
        elif op == '/':
            return self.div(a, b)
        else:
            print("Невірна операція!")
            return None
