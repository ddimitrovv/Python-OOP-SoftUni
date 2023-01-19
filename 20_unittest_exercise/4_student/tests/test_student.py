from unittest import TestCase, main

from project import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.name = 'Nikodim'
        self.courses = {'Python': ['note 1']}
        self.student = Student(self.name, self.courses)

    def test_student_init__should_return_correct_obj(self):
        student = Student(self.name)
        self.assertEqual(self.name, student.name)
        self.assertEqual(dict(), student.courses)

    def test_student_init_with_dict__should_return_correct_obj(self):
        self.assertEqual(self.name, self.student.name)
        self.assertEqual(self.courses, self.student.courses)

    def test_student_enroll_course_not_in_dict__expected_to_return_correct_string(self):
        course_name = 'Java'
        notes = ['note 1', 'note 2']
        add_course_notes = "z"
        expected = "Course has been added."
        actual = self.student.enroll(course_name, notes, add_course_notes)
        self.assertEqual(expected, actual)
        self.assertEqual(list(), self.student.courses[course_name])

    def test_student_enroll_course_in_dict_keys__expected_to_return_correct_string(self):
        course_name = 'Python'
        course = {'Python': ['note 1', 'note 2']}
        expected = "Course already added. Notes have been updated."
        student = Student(self.name, course)
        actual = student.enroll(course_name, ['note 3'])
        self.assertEqual(expected, actual)
        self.assertEqual(['note 1', 'note 2', 'note 3'], student.courses[course_name])

    def test_student_enroll_add_course_notes_equal_to_Y_or_empty_str__expected_to_return_correct_string(self):
        course_name = 'C++'
        notes = ['Note 1']
        add_course_notes = "Y"
        expected = "Course and course notes have been added."
        actual = self.student.enroll(course_name, notes, add_course_notes)
        self.assertEqual(expected, actual)
        self.assertEqual(notes, self.student.courses[course_name])

    def test_student_add_notes__course_in_courses__expected_correct_string(self):
        course_name = 'Python'
        notes = ['note 2', 'note 3']
        add_course_notes = "z"
        student = Student(self.name, self.courses)
        student.enroll(course_name, notes, add_course_notes)
        expected = "Notes have been updated"
        actual = student.add_notes(course_name, notes)
        self.assertEqual(expected, actual)

    def test_student_add_notes__course_not_in_courses__expected_correct_string(self):
        course_name = 'C#'
        notes = ['Note']
        expected = "Cannot add notes. Course not found."
        with self.assertRaises(Exception) as error:
            self.student.add_notes(course_name, notes)
        self.assertEqual(expected, str(error.exception))

    def test_student_leave_course__course_in_courses__expected_correct_string(self):
        course_name = 'Python'
        self.student.courses = self.courses
        expected = "Course has been removed"
        actual = self.student.leave_course(course_name)
        self.assertEqual(expected, actual)

    def test_student_leave_course__course_not_in_courses__expected_correct_string(self):
        course_name = 'Java'
        expected = "Cannot remove course. Course not found."
        with self.assertRaises(Exception) as error:
            self.student.leave_course(course_name)
        self.assertEqual(expected, str(error.exception))


if __name__ == "__main__":
    main()
