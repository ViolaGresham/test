import unittest
from app.math_utils import add, div

class TestMathUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_div(self):
        self.assertEqual(div(10, 2), 5)

    def test_div_zero(self):
        with self.assertRaises(ValueError):
            div(1, 0)

if __name__ == '__main__':
    unittest.main()
