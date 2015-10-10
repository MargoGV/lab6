import unittest
import lib
import math
class LibTest(unittest.TestCase):
    def test_factorial_non_negative_arg(self):
        self.assertEqual(lib.factorial(3), 6)
        self.assertEqual(lib.factorial(8), 40320)
        self.assertEqual(lib.factorial(5), 120)
    def test_factorial_negative(self):
        self.assertEqual(lib.factorial(-1), 1)
    def test_even(self):
        self.assertEqual(lib.even(2), True)
        self.assertEqual(lib.even(0), True)
        self.assertEqual(lib.even(8), True)
        self.assertEqual(lib.even(16), True)
        self.assertEqual(lib.even(4032), True)
    def test_even_two(self):
        self.assertEqual(lib.even(-72), True)
    def test_non_even(self):
        self.assertEqual(lib.even(5), False)
        self.assertEqual(lib.even(7), False)
        self.assertEqual(lib.even(243), False)
        self.assertEqual(lib.even(-1), False)
    def test_palindrome(self):
        self.assertEqual(lib.palindrome('aqqa'), True)
        self.assertEqual(lib.palindrome('лепсспел'), True)
        self.assertEqual(lib.palindrome(''), True)
        self.assertEqual(lib.palindrome('ahaha'), True)
        self.assertEqual(lib.palindrome('123321'), True)
    def test_non_palindrome(self):
        self.assertEqual(lib.palindrome('qwqwdddd'), False)
        self.assertEqual(lib.palindrome('114332'), False)
        self.assertEqual(lib.palindrome('/'), False)
        self.assertEqual(lib.palindrome('3242q3t3'), False)
    def test_prime(self):
        self.assertEqual(lib.prime(11), True)
        self.assertEqual(lib.prime(3), True)
        self.assertEqual(lib.prime(3), True)
        self.assertEqual(lib.prime(17), True)
    def test_non_prime(self):
        self.assertEqual(lib.prime(12), False)
        self.assertEqual(lib.prime(0), False)
        self.assertEqual(lib.prime(156), False)
    def test_non_prime_two(self):
        self.assertEqual(lib.prime(-3), False)
    def test_sqrt(self):
        self.assertEqual(lib.sqrt(144), 12)
        self.assertEqual(lib.sqrt(0), 0)
        self.assertEqual(lib.sqrt(121), 11)
        self.assertEqual(lib.sqrt(25), 5)
    def test_sqrt_negativ(self):
        self.assertEqual(lib.sqrt(-12), 0)
        self.assertEqual(lib.sqrt(-3), 0)
        self.assertEqual(lib.sqrt(-4), 0)
    def test_sin(self):
        self.assertEqual(lib.sin(math.pi), 0)
        self.assertEqual(lib.sin(0), 0)
        self.assertEqual(lib.sin((math.pi)/2), 1)
        self.assertEqual(lib.sin((math.pi)/6), 0.5) 
unittest.main(verbosity=11)






