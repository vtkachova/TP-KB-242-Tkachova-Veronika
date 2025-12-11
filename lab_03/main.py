from studentlist import StudentList
from student import Student
from utils import Utils

file = "lab_03/lab_03.csv"

def main():
    group = StudentList()

    # завантаження з файлу
    loaded = Utils.load_from_csv(file)
    for s in loaded:
        group.add_student(s)

    while True:
        choice = input("Choose action [C create, U update, D delete, P print, X exit]: ")

        match choice.lower():
            case "c":
                print("Adding new student:")
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                stud_group = input("Enter group: ")
                email = input("Enter email: ")

                student = Student(name, phone, stud_group, email)
                group.add_student(student)
                print("New student added!\n")

            case "u":
                print("Updating student info:")
                name = input("Enter name to update: ")

                print("Leave empty to keep old value")
                new_name = input("New name: ") or None
                new_phone = input("New phone: ") or None
                new_group = input("New group: ") or None
                new_email = input("New email: ") or None

                if group.update_student(name, new_name, new_phone, new_group, new_email):
                    print("Student updated!\n")
                else:
                    print("Student not found.\n")

            case "d":
                print("Deleting student:")
                name = input("Enter name to delete: ")
                if group.delete_student(name):
                    print("Student deleted!\n")
                else:
                    print("Student not found.\n")

            case "p":
                print("Student list:")
                group.print_all()

            case "x":
                Utils.save_to_csv(file, group.students)
                print("Exit program.")
                break

            case _:
                print("Wrong choice, try again.\n")

if __name__ == "__main__":
    main()
