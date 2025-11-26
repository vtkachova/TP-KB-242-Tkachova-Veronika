import functions     
import operations 
import logger  

print("=== КАЛЬКУЛЯТОР ===")

op = operations.get_operation()   
a, b = operations.get_numbers()  

if op == '+':
    result = functions.add(a, b)
elif op == '-':
    result = functions.sub(a, b)
elif op == '*':
    result = functions.mul(a, b)
elif op == '/':
    result = functions.div(a, b)
else:
    print("Невірна операція!")
    result=None
    
if result is not None:
    print("Результат:", result)
    logger.log_action(a, b, op, result) #логування 