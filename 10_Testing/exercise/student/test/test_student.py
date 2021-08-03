from project.student import Student
from unittest import TestCase, main


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student('Ivan')

    def test_init_method_assertion(self):
        self.assertEqual('Ivan', self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_init_contain_course(self):
        self.student.courses = {'Python': ['n_1']}
        self.assertEqual('Ivan', self.student.name)
        self.assertEqual(self.student.courses, {'Python': ['n_1']})

    def test_init_contain_none_course(self):
        student = Student('Ivan', None)
        self.assertEqual('Ivan', student.name)
        self.assertEqual(student.courses, {})

    def test_enroll_duplicated_courses(self):
        self.student.courses = {'Python': ['note_1']}
        res = self.student.enroll('Python', ['note_2'])

        self.assertEqual("Course already added. Notes have been updated.", res)
        self.assertEqual(['note_1', 'note_2'], self.student.courses['Python'])

    def test_enroll_new_course_with_notes(self):
        res = self.student.enroll('Python', ['note_3'])
        self.assertEqual("Course and course notes have been added.", res)
        self.assertEqual(['note_3'], self.student.courses['Python'])

    def test_enroll_new_course_without_adding_notes(self):
        res = self.student.enroll('Python', ['note_3'], 'no')
        self.assertEqual("Course has been added.", res)
        self.assertEqual([], self.student.courses['Python'])

    def test_enroll_new_course_with_adding_notes(self):
        res = self.student.enroll('Python', ['note_1', 'note_2'], 'Y')
        self.assertEqual(self.student.courses['Python'], ['note_1', 'note_2'], res)

    def test_enroll_existing_course_and_adding_notes(self):
        self.student.enroll('Python', ['note_1', 'note_2'], 'Y')
        res = self.student.enroll('Python', ['note_3'], 'Y')
        self.assertEqual("Course already added. Notes have been updated.", res)
        self.assertEqual(['note_1', 'note_2', 'note_3'], self.student.courses['Python'])

    def test_add_notes(self):
        self.student.courses = {'Python': []}
        res = self.student.add_notes('Python', 'note_1')
        self.assertEqual("Notes have been updated", res)
        self.assertEqual(['note_1'], self.student.courses['Python'])

    def test_add_notes_when_course_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('JS', 'note_J')
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        self.assertEqual({}, self.student.courses)

    def test_leave_course(self):
        self.student.courses = {'Python': []}
        res = self.student.leave_course('Python')
        self.assertEqual("Course has been removed", res)

    def test_leave_non_existing_course(self):
        self.student.courses = {'Python': []}
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('Mushmuli')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()
