from project.student_report_card import StudentReportCard

from unittest import TestCase, main


class TestStudentReportCard(TestCase):
    STUDENT_NAME = 'Nikodim'
    SCHOOL_YEAR = 10
    NAME_NOT_VALID = "Student Name cannot be an empty string!"
    SCHOOL_YEAR_NOT_VALID = "School Year must be between 1 and 12!"
    MIN_SCHOOL_YEAR = 1
    MAX_SCHOOL_YEAR = 12

    def setUp(self) -> None:
        self.student_report_card = StudentReportCard(self.STUDENT_NAME, self.SCHOOL_YEAR)

    def test_init__expected_correct_object(self):
        self.assertEqual(self.STUDENT_NAME, self.student_report_card.student_name)
        self.assertEqual(self.SCHOOL_YEAR, self.student_report_card.school_year)
        self.assertDictEqual({}, dict(self.student_report_card.grades_by_subject))

    def test_init__invalid_name__expected_to_raise_value_error(self):
        with self.assertRaises(ValueError) as error:
            self.student_report_card.student_name = ''
        self.assertEqual(self.NAME_NOT_VALID, str(error.exception))

    def test_init__max_valid_year__expected_correct_object(self):
        self.student_report_card.school_year = 12
        self.assertEqual(self.STUDENT_NAME, self.student_report_card.student_name)
        self.assertEqual(self.MAX_SCHOOL_YEAR, self.student_report_card.school_year)
        self.assertDictEqual({}, dict(self.student_report_card.grades_by_subject))

    def test_init__min_valid_year__expected_correct_object(self):
        self.student_report_card.school_year = 1
        self.assertEqual(self.STUDENT_NAME, self.student_report_card.student_name)
        self.assertEqual(self.MIN_SCHOOL_YEAR, self.student_report_card.school_year)
        self.assertDictEqual({}, dict(self.student_report_card.grades_by_subject))

    def test_init__year_less_than_valid__expected_to_raise_value_error(self):
        with self.assertRaises(ValueError) as error:
            self.student_report_card.school_year = 0
        self.assertEqual(self.SCHOOL_YEAR_NOT_VALID, str(error.exception))

    def test_init__year_greater_than_valid__expected_to_raise_value_error(self):
        with self.assertRaises(ValueError) as error:
            self.student_report_card.school_year = 13
        self.assertEqual(self.SCHOOL_YEAR_NOT_VALID, str(error.exception))

    def test_add_grade__subject_not_in_subjects__expected_to_be_added(self):
        subject = 'Programming'
        grade = 6.00
        self.student_report_card.add_grade(subject, grade)
        self.assertDictEqual({subject: [grade]}, dict(self.student_report_card.grades_by_subject))

    def test_add_grade__subject_in_subjects__expected_grade_to_be_extended(self):
        subject = 'Programming'
        grade = 6.00
        grade2 = 5.80
        self.student_report_card.add_grade(subject, grade)
        self.student_report_card.add_grade(subject, grade2)
        self.assertDictEqual({subject: [grade, grade2]}, dict(self.student_report_card.grades_by_subject))

    def test_average_grade_by_subject_without_subjects__expected_empty_string(self):
        self.assertEqual('', self.student_report_card.average_grade_by_subject())

    def test_average_grade_by_subject_with_subject__expected_correct_string(self):
        subject = 'Programming'
        grade = 6.00
        grade2 = 5.80
        self.student_report_card.add_grade(subject, grade)
        self.student_report_card.add_grade(subject, grade2)
        expected_grade = (grade + grade2) / 2
        expected = f"{subject}: {expected_grade:.2f}\n"
        self.assertEqual(expected.strip(), self.student_report_card.average_grade_by_subject())

    def test_average_grade_by_subjects_with_subject__expected_correct_string(self):
        subject = 'Programming Advanced'
        grade = 6.00
        grade2 = 5.80
        self.student_report_card.add_grade(subject, grade)
        self.student_report_card.add_grade(subject, grade2)
        subject2 = 'Programming OOP'
        grade3 = 5.90
        grade4 = 5.80
        self.student_report_card.add_grade(subject2, grade3)
        self.student_report_card.add_grade(subject2, grade4)
        expected_grade = (grade + grade2) / 2
        expected_grade2 = (grade3 + grade4) / 2
        expected = f"{subject}: {expected_grade:.2f}" + "\n" + f"{subject2}: {expected_grade2:.2f}\n"
        self.assertEqual(expected.strip(), self.student_report_card.average_grade_by_subject())

    def test_average_grade_for_all_subjects_without_subjects__expected_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            self.student_report_card.average_grade_for_all_subjects()

    def test_average_grade_for_all_subjects_with_subject__expected_correct_string(self):
        subject = 'Programming'
        grade = 6.00
        grade2 = 5.80
        self.student_report_card.add_grade(subject, grade)
        self.student_report_card.add_grade(subject, grade2)
        expected_grade = (grade + grade2) / 2
        expected = f"Average Grade: {expected_grade:.2f}"
        self.assertEqual(expected.strip(), self.student_report_card.average_grade_for_all_subjects())

    def test_average_grade_for_all_subjects_with_subjects__expected_correct_string(self):
        subject = 'Programming Advanced'
        grade = 6.00
        grade2 = 5.80
        self.student_report_card.add_grade(subject, grade)
        self.student_report_card.add_grade(subject, grade2)
        subject2 = 'Programming OOP'
        grade3 = 5.90
        grade4 = 5.80
        self.student_report_card.add_grade(subject2, grade3)
        self.student_report_card.add_grade(subject2, grade4)
        expected_grade = (grade + grade2 + grade3 + grade4) / 4
        expected = f"Average Grade: {expected_grade:.2f}"
        self.assertEqual(expected.strip(), self.student_report_card.average_grade_for_all_subjects())

    def test_repr__without_students__expected_to_raise_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            repr(self.student_report_card)

    def test_repr__with_students__expected_correct_string(self):
        subject = 'Programming Advanced'
        grade = 6.00
        grade2 = 5.80
        self.student_report_card.add_grade(subject, grade)
        self.student_report_card.add_grade(subject, grade2)
        subject2 = 'Programming OOP'
        grade3 = 5.90
        grade4 = 5.80
        self.student_report_card.add_grade(subject2, grade3)
        self.student_report_card.add_grade(subject2, grade4)
        expected_grade1 = (grade + grade2) / 2
        expected_grade2 = (grade3 + grade4) / 2
        expected_grade3 = (grade + grade2 + grade3 + grade4) / 4
        expected = f"""Name: {self.STUDENT_NAME}
Year: {self.SCHOOL_YEAR}
----------
{subject}: {expected_grade1:.2f}
{subject2}: {expected_grade2:.2f}
----------
Average Grade: {expected_grade3:.2f}"""

        self.assertEqual(expected, repr(self.student_report_card))


if __name__ == "__main__":
    main()
