import csv
from sys import argv

student_list = []

# ===== CSV LOAD =====
def load_from_csv(inputfile):
    global student_list
    try:
        with open(inputfile, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file) 
            student_list = list(reader)
        print("Data successfully loaded from CSV.\n")
    except FileNotFoundError:
        print(f"{inputfile} not found, starting with empty list.\n")

# ===== CSV SAVE =====
def save_to_csv(inputfile):
    global student_list
    with open(inputfile, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["name", "phone", "group", "email"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(student_list)
    print("Data saved to CSV.\n")

# ===== PRINT ALL =====
def printAllList():
    for elem in student_list:
        print(f"Name: {elem['name']}, Phone: {elem['phone']}, Group: {elem['group']}, Email: {elem['email']}")
    print()

# ===== ADD NEW =====
def addNewElement():
    name = input("Enter student name: ")
    phone = input("Enter student phone: ")
    group = input("Enter student group: ")
    email = input("Enter student email: ")
    newItem = {"name": name, "phone": phone, "group": group, "email": email}

    # Вставка у відсортований список
    insertPosition = 0
    for item in student_list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    student_list.insert(insertPosition, newItem)
    print("New student added!\n")

# ===== DELETE =====
def deleteElement():
    name = input("Enter name to delete: ")
    deletePosition = -1
    for item in student_list:
        if name == item["name"]:
            deletePosition = student_list.index(item)
            break
    if deletePosition == -1:
        print("Student not found\n")
    else:
        del student_list[deletePosition]
        print("Student deleted\n")

# ===== UPDATE =====
def updateElement():
    name = input("Enter student name to update: ")
    found = None
    for item in student_list:
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

    student_list.remove(found)
    newItem = {"name": new_name, "phone": new_phone, "group": new_group, "email": new_email}

    # Вставка у відсортований список
    insertPosition = 0
    for item in student_list:
        if new_name > item["name"]:
            insertPosition += 1
        else:
            break
    student_list.insert(insertPosition, newItem)
    print("Student information updated!\n")

# ===== MAIN =====
def main():
    if len(argv) < 2:
        print("Usage: py lab_02/lab_02.py lab_02/lab_02.csv")
        return

    inputfile = argv[1]
    load_from_csv(inputfile)

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
                save_to_csv(inputfile)  # перезаписуємо той самий CSV
                print("Exit program.")
                break
            case _:
                print("Wrong choice, try again.\n")

if __name__ == "__main__":
    main()
