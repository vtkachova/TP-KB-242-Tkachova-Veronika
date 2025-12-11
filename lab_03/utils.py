import csv
from student import Student

class Utils:
    @staticmethod
    def load_from_csv(filename):
        students = []
        try:
            with open(filename, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    s = Student(row["name"], row["phone"], row["group"], row["email"])
                    students.append(s)
            print("Data successfully loaded from CSV.\n")
        except FileNotFoundError:
            print(f"{filename} not found. Starting with empty list.\n")

        return students

    @staticmethod
    def save_to_csv(filename, students):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["name", "phone", "group", "email"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for s in students:
                writer.writerow({
                    "name": s.name,
                    "phone": s.phone,
                    "group": s.group,
                    "email": s.email
                })

        print("Data saved to CSV.\n")