students = [
    {'name': 'Анна', 'grade': 85},
    {'name': 'Петро', 'grade': 90},
    {'name': 'Марія', 'grade': 75},
    {'name': 'Олександр', 'grade': 88},
    {'name': 'Микола', 'grade': 67},
    {'name': 'Дмитро', 'grade': 60},
    {'name': 'Марина', 'grade': 100},
    {'name': 'Софія', 'grade': 92},
    {'name': 'Вероніка', 'grade': 98}
]

while True:
    sort_field = input("За яким параметром сортувати студентів (name, grade): ")
    if sort_field in ["name", "grade"]:
        break
    else:
        print("\nПомилка! Спробуйте ще раз.\n")

def sort_students(students, field):
    sorted_list = sorted(students, key=lambda s: s[field])
    
    print(f"\nВідсортовано за {field}:\n")
    for s in sorted_list:
        print(f'{s["name"]}  {s["grade"]}')

sort_students(students, sort_field)
