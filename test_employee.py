import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('Jason', 'Eisele', 5000)
        emp_2 = Employee('Elijah', 'Sawyers', 100000)

        self.assertEqual(emp_1.email, 'Jason.Eisele@email.com')
        self.assertEqual(emp_2.email, 'Elijah.Sawyers@email.com')

        emp_1.first = 'John'
        emp_2.first = 'Jane'
        self.assertEqual(emp_1.email, 'John.Eisele@email.com')
        self.assertEqual(emp_2.email, 'Jane.Sawyers@email.com')

    def test_fullName(self):
        emp_1 = Employee('Jason', 'Eisele', 50000)
        emp_2 = Employee('Elijah', 'Sawyers', 100000)
        self.assertEqual(emp_1.fullName, 'Jason Eisele')
        self.assertEqual(emp_2.fullName, 'Elijah Sawyers')

        emp_1.first = 'John'
        emp_2.first = 'Jane'
        self.assertEqual(emp_1.fullName, 'John Eisele')
        self.assertEqual(emp_2.fullName, 'Jane Sawyers')

    def test_apply_raise(self):
        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Jason', 'Eisele', 100000)
        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 105000)
