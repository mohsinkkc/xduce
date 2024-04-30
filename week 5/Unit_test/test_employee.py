import unittest
from employee import Employee

class UnittestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp1=Employee('mohsin','kkc',50000)
        self.emp2=Employee('devanshu','chauhan',60000)

    def test_email(self):

        self.assertEqual(self.emp1.email(),'mohsin.kkc@gmail.com')
        self.assertEqual(self.emp2.email(),'devanshu.chauhan@gmail.com')

        self.emp1='mohmad'
        self.emp2='dev'

        self.assertEqual(self.emp1.email(),'mohmad.kkc@gmail.com')
        self.assertEqual(self.emp2.email(),'dev.chauhan@gmail.com')

    def test_fullname(self):

        self.assertEqual(self.emp1.fullname(),'mohsin kkc')
        self.assertEqual(self.emp2.fullname(),'devanshu chauhan')

        self.emp1='mohmad'
        self.emp2='dev'

        self.assertEqual(self.emp1.fullname(),'mohmad kkc')
        self.assertEqual(self.emp2.fullname(),'dev chauhan')

    def test_apply_raise(self):
        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay,52500)
        self.assertEqual(self.emp2.pay,63000)

if __name__=='__main__':
    unittest.main()

        