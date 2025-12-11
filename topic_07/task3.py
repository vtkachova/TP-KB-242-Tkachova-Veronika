class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} років"

students = [
    Student("Вероніка", 18),
    Student("Микола", 20),
    Student("Ірина", 19),
    Student("Андрій", 17)
]

sorted_students = sorted(students, key=lambda s: s.age)

for st in sorted_students:
    print(st)