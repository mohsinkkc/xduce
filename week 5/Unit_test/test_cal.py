import unittest
import calculation

class Unittest_cal(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculation.add(2,3),5)
        self.assertEqual(calculation.add(-1,3),2)
        self.assertEqual(calculation.add(-2,-3),-5)

    
    def test_sub(self):
        self.assertEqual(calculation.sub(2,3),-1)
        self.assertEqual(calculation.sub(-1,3),-4)
        self.assertEqual(calculation.sub(-2,-3),1)


    def test_multi(self):
        self.assertEqual(calculation.multi(2,3),6)
        self.assertEqual(calculation.multi(-1,3),-3)
        self.assertEqual(calculation.multi(-2,-3),6)


    def test_div(self):
        self.assertEqual(calculation.div(2,2),1)
        self.assertEqual(calculation.div(-6,3),-2)
        self.assertEqual(calculation.div(-12,-3),4)

if __name__=='__main__':
    unittest.main()
