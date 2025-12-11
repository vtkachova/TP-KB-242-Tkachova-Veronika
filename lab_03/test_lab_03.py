import unittest
from student import Student
from studentlist import StudentList

class TestStudentSystem(unittest.TestCase):

    def setUp(self):
        self.student_list_manager = StudentList()

    def test_add_student(self):
        student = Student(
            "Bob",
            "0631234567",
            "KB-242",
            "bob@gmail.com"
        )
        self.student_list_manager.add_student(student)

        added_student = self.student_list_manager.students[0]

        self.assertEqual(len(self.student_list_manager.students), 1)
        self.assertEqual(added_student.phone, "0631234567")
        self.assertEqual(added_student.name, "Bob")

    def test_delete_student(self):
        initial_student = Student(
            "Bob",
            "0631234567",
            "KB-242",
            "bob@gmail.com"
        )
        self.student_list_manager.students = [initial_student]

        self.assertEqual(len(self.student_list_manager.students), 1)

        result = self.student_list_manager.delete_student("Bob")
        self.assertTrue(result)
        self.assertEqual(len(self.student_list_manager.students), 0)

    def test_update_student(self):
        initial_student = Student(
            "Alice",
            "0630000000",
            "KB-242",
            "alice@gmail.com"
        )
        self.student_list_manager.students = [initial_student]

        result = self.student_list_manager.update_student(
            "Alice",
            new_phone="0999999999",
            new_group="KB-222"
        )

        self.assertTrue(result)
        updated_student = self.student_list_manager.students[0]
        self.assertEqual(updated_student.phone, "0999999999")
        self.assertEqual(updated_student.group, "KB-222")

if __name__ == '__main__':
    unittest.main()
