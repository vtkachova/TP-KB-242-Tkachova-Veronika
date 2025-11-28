import unittest
import lab_02

class TestLab02(unittest.TestCase):

    def setUp(self):
        lab_02.student_list = [
            {"name": "Bob",  "phone": "0631111111", "group": "KB-242", "email": "bob@gmail.com"},
            {"name": "Emma", "phone": "0632222222", "group": "KB-242", "email": "emma@gmail.com"},
            {"name": "Jon",  "phone": "0633333333", "group": "KB-242", "email": "jon@gmail.com"},
            {"name": "Zak",  "phone": "0634444444", "group": "KB-242", "email": "zak@gmail.com"}
        ]

    def test_add_student_direct(self):
        # Додаємо нового студента
        new_student = {"name": "Alice", "phone": "0635555555", "group": "KB-242", "email": "alice@gmail.com"}
        lab_02.student_list.append(new_student)  
        self.assertIn(new_student, lab_02.student_list)
        self.assertEqual(len(lab_02.student_list), 5)

    def test_delete_student_direct(self):
        # Видаляємо студента Emma
        lab_02.student_list = [s for s in lab_02.student_list if s["name"] != "Emma"]
        names = [s["name"] for s in lab_02.student_list]
        self.assertNotIn("Emma", names)
        self.assertEqual(len(lab_02.student_list), 3)

    def test_update_student_direct(self):
        # Оновлюємо дані студента Bob
        for s in lab_02.student_list:
            if s["name"] == "Bob":
                s.update({"name": "Bobby", "phone": "0639999999", "email": "bobby@gmail.com"})
                break
        names = [s["name"] for s in lab_02.student_list]
        self.assertIn("Bobby", names)
        student = next(s for s in lab_02.student_list if s["name"] == "Bobby")
        self.assertEqual(student["phone"], "0639999999")
        self.assertEqual(student["email"], "bobby@gmail.com")

if __name__ == "__main__":
    unittest.main()
