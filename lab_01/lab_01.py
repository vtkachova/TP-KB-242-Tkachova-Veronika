# Початковий список студентів
students = [
    {"name": "Bob",  "phone": "0631111111", "group": "KB-242", "email": "bob@gmail.com"},
    {"name": "Emma", "phone": "0632222222", "group": "KB-242", "email": "emma@gmail.com"},
    {"name": "Jon",  "phone": "0633333333", "group": "KB-242", "email": "jon@gmail.com"},
    {"name": "Zak",  "phone": "0634444444", "group": "KB-242", "email": "zak@gmail.com"}
]


# Вивід усіх студентів
def printAllList():
    for elem in students:
        print(f"Name: {elem['name']}, Phone: {elem['phone']}, Group: {elem['group']}, Email: {elem['email']}")
    print()


# Додавання нового студента
def addNewElement():
    name = input("Enter student name: ")
    phone = input("Enter student phone: ")
    group = input("Enter student group: ")
    email = input("Enter student email: ")
    newItem = {"name": name, "phone": phone, "group": group, "email": email}
    
    # Знайти місце для вставки (щоб список залишався відсортованим)
    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("New student added!\n")


# Видалення студента
def deleteElement():
    name = input("Enter name to delete: ")
    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break
    if deletePosition == -1:
        print("Student not found\n")
    else:
        del students[deletePosition]
        print("Student deleted\n")


# Оновлення інформації про студента
def updateElement():
    name = input("Enter student name to update: ")
    found = None
    for item in students:
        if name == item["name"]:
            found = item
            break

    if not found:
        print("Student not found\n")
        return

    print("Enter new data (press Enter to leave unchanged):")
    new_name = input(f"Name [{found['name']}]: ") or found['name']
    new_phone = input(f"Phone [{found['phone']}]: ") or found['phone']
    new_group = input(f"Group [{found['group']}]: ") or found['group']
    new_email = input(f"Email [{found['email']}]: ") or found['email']

    # Видаляємо старий запис і вставляємо оновлений у відсортованому порядку
    students.remove(found)
    newItem = {"name": new_name, "phone": new_phone, "group": new_group, "email": new_email}

    insertPosition = 0
    for item in students:
        if new_name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("Student information updated!\n")


# Головне меню
def main():
    while True:
        choice = input("Choose action [C create, U update, D delete, P print, X exit]: ")
        match choice:
            case "C" | "c":
                print("Adding new student:")
                addNewElement()
            case "U" | "u":
                print("Updating student info:")
                updateElement()
            case "D" | "d":
                print("Deleting student:")
                deleteElement()
            case "P" | "p":
                print("Student list:")
                printAllList()
            case "X" | "x":
                print("Exit program.")
                break
            case _:
                print("Wrong choice, try again.\n")


# Запуск програми
main()
