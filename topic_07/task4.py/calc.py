from operations import OperationManager
from functions import Calculator

print("=== КАЛЬКУЛЯТОР ===")

op_manager = OperationManager()
calc = Calculator()

op = op_manager.get_operation()
a, b = op_manager.get_numbers()

result = calc.calculate(op, a, b)

if result is not None:
    print("Результат:", result)
