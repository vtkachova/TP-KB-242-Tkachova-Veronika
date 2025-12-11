from student import Student

class StudentList:
    def __init__(self):
        self.students = []

    # додати нового студента 
    def add_student(self, student: Student):
        insert_pos = 0
        for s in self.students:
            if student.name > s.name:
                insert_pos += 1
            else:
                break
        self.students.insert(insert_pos, student)

    # видалення студента
    def delete_student(self, name: str):
        for s in self.students:
            if s.name == name:
                self.students.remove(s)
                return True
        return False

    # оновлення даних
    def update_student(self, name: str,
                       new_name=None, new_phone=None, new_group=None, new_email=None):
        for s in self.students:
            if s.name == name:
                s.name = new_name if new_name else s.name
                s.phone = new_phone if new_phone else s.phone
                s.group = new_group if new_group else s.group
                s.email = new_email if new_email else s.email
                return True
        return False

    # виведення усіх
    def print_all(self):
        for s in self.students:
            print(s)
        print()
