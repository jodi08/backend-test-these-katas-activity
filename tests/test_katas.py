import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        result = katas.add(3, 4)
        self.assertEqual(result, 7)

    def test_multiply(self):
        # checking the multiply function using the add function
        result = katas.multiply(5, 5)
        self.assertEqual(result, 25)

        result = katas.multiply(-2, 1)
        self.assertEqual(result, -2)

        result = katas.multiply(-2, -1)
        self.assertEqual(result, 2)

    def test_power(self):
        result = katas.power(2, 3)
        self.assertEqual(result, 8)

    def test_factorial(self):
        result = katas.factorial(5)
        self.assertEqual(result, 120)

    def test_fibonacci(self):
        result = katas.fibonacci(7)
        self.assertEqual(result, 8)


if __name__ == '__main__':
    unittest.main()
