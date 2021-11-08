import unittest
from check import check

class Test(unittest.TestCase):

    def testone(self):
        self.assertEqual(check(1, 1, 1), 1)
    def testtwo(self):
        self.assertEqual(check('z', 11, -1), "Error")
    def testhree(self):
        self.assertEqual(check(11, 'a', 8), "Error")
    def testfour(self):
        self.assertEqual(check(0, 6, 15), 15)
    def testfive(self):
        self.assertEqual(check(-0.2, -9, 1.0), 1.0)
    def testsix(self):
        self.assertEqual(check(3, -2.7, 3), 3)
    def testseven(self):
        self.assertEqual(check(-10.2, 1.7, 1.7), 1.7)
    def testeight(self):
        self.assertEqual(check(3.0, "abc", 5), "Error")
    def testnine(self):
        self.assertEqual(check(-0.0009, -100000000, -1), -0.0009)
    def testten(self):
        self.assertEqual(check(-0.0009, -100000000, "xyz"), "Error")