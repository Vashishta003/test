import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(calculator.sub(5, 2), 3)

    def test_mul(self):
        self.assertEqual(calculator.mul(3, 4), 12)

    def test_div(self):
        self.assertAlmostEqual(calculator.div(7, 2), 3.5)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(1, 0)

    def test_pow(self):
        self.assertEqual(calculator.power(2, 5), 32)

    def test_safe_eval_simple(self):
        self.assertEqual(calculator.safe_eval("2+3*4"), 14)

    def test_safe_eval_unary(self):
        self.assertEqual(calculator.safe_eval("-5 + 2"), -3)

    def test_safe_eval_invalid(self):
        with self.assertRaises(ValueError):
            calculator.safe_eval("__import__('os').system('echo hi')")


if __name__ == "__main__":
    unittest.main()
