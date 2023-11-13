import unittest
from math_quiz import random_integer, random_operator, math_problem

class TestMathGame(unittest.TestCase):
    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        result = random_operator()
        self.assertIn(result, ['+', '-', '*'])

    def test_math_problem(self):
        test_cases = [
            (3, 2, '+', '3 + 2', 5),
            (1, 5, '-', '1 - 5', -4),
            (10, 2, '*','10 * 2', 20),
            
        ]

        for number1, number2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = math_problem(number1, number2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()