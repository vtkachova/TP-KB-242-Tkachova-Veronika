print(">>> Тестування функцій списків <<<")

# Створюємо початковий список
numbers = [3, 1, 4]
print("Початковий список:", numbers)

# append() — додає один елемент в кінець списку
numbers.append(5)
print("Після append(5):", numbers)

# extend() — додає кілька елементів
numbers.extend([6, 7])
print("Після extend([6, 7]):", numbers)

# insert() — вставляє елемент у вказане місце
numbers.insert(1, 10)  
print("Після insert(1, 10):", numbers)

# remove() — видаляє зазначений елемент зі списку
numbers.remove(4)
print("Після remove(4):", numbers)

# copy() — створює копію списку
numbers_copy = numbers.copy()
print("Копія списку:", numbers_copy)

# sort() — сортує список
numbers.sort()
print("Після sort():", numbers)

# reverse() — перевертає список
numbers.reverse()
print("Після reverse():", numbers)

# clear() — очищає список
numbers.clear()
print("Після clear():", numbers)


