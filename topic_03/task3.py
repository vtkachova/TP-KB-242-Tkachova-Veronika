print(">>> Тестування функцій словників <<<")

student = {"name": "Veronika", "age": 18}
print("Початковий словник:", student)

# update() — оновлює словник 
student.update({"city": "Chernihiv"})
print("Після update():", student)

# keys() — повертає всі ключі
print("Ключі словника:", student.keys())

# values() — повертає всі значення
print("Значення словника:", student.values())

# items() — повертає пари ключ:значення
print("Пари ключ:значення:", student.items())

# del — видаляє зазначений елемент за ключем
del student["city"]
print("Після del:", student)

# clear() — очищає словник
student.clear()
print("Після clear():", student)


