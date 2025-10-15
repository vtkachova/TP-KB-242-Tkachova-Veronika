print(">>> Пошук позиції для вставки <<<")

# Функція пошуку позиції для вставки
def find_insert_position(sorted_list, x):
    for i in range(len(sorted_list)):
        if x < sorted_list[i]:
            return i  # повертаємо позицію, куди треба вставити
    return len(sorted_list)  # якщо елемент найбільший — в кінець


numbers = [1, 3, 5, 7, 9]
print("Відсортований список:", numbers)

x = int(input("Введіть число для вставки: "))

pos = find_insert_position(numbers, x)
print("Позиція для вставки:", pos)


numbers.insert(pos, x)
print("Новий список:", numbers)
