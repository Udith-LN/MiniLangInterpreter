import unittest
from interpreter.tokenizer import tokenize
from interpreter.parser import Parser
from interpreter.interpreter import Interpreter

class TestInterpreter(unittest.TestCase):

    def setUp(self):
        """Setup before each test case"""
        self.interpreter = Interpreter()

    def execute_code(self, code):
        """Helper method to execute code"""
        tokens = tokenize(code)
        parser = Parser(tokens)
        ast = parser.parse()
        return self.interpreter.execute(ast)

    def test_basic_arithmetic(self):
        code = "x = 10; y = x + 5; print(y);"
        result = self.execute_code(code)
        self.assertEqual(result[-1], 15)  # Check print output

    def test_operator_precedence(self):
        code = "x = 10 + 5 * 2; print(x);"
        result = self.execute_code(code)
        self.assertEqual(result[-1], 20)  # Multiplication first

    def test_nested_parentheses(self):
        code = "x = ((10 + 2) * (5 - 3)) + (20 / (4 + 1)); print(x);"
        result = self.execute_code(code)
        self.assertEqual(result[-1], 26.0)  # Correct grouping and precedence

    def test_division_and_modulus(self):
        code = "a = 20 / 5; b = 23 % 5; print(a); print(b);"
        result = self.execute_code(code)
        self.assertEqual(result[-2], 4.0)  # Division
        self.assertEqual(result[-1], 3)    # Modulus

    def test_undefined_variable(self):
        code = "x = 10; print(y);"
        with self.assertRaises(NameError) as context:
            self.execute_code(code)
        self.assertIn("Undefined variable: y", str(context.exception))

    def test_division_by_zero(self):
        code = "x = 10 / 0; print(x);"
        with self.assertRaises(ZeroDivisionError) as context:
            self.execute_code(code)
        self.assertIn("Division by zero is not allowed", str(context.exception))

    def test_modulus_by_zero(self):
        code = "x = 10 % 0; print(x);"
        with self.assertRaises(ZeroDivisionError) as context:
            self.execute_code(code)
        self.assertIn("Modulus by zero is not allowed", str(context.exception))

    def test_invalid_character(self):
        code = "x = 10 @ 5;"
        with self.assertRaises(SyntaxError) as context:
            self.execute_code(code)
        self.assertIn("Unexpected character: @", str(context.exception))

    def test_incomplete_expression(self):
        code = "x = (10 + ;"
        with self.assertRaises(SyntaxError) as context:
            self.execute_code(code)
        self.assertIn("Missing closing parenthesis", str(context.exception))

    def test_unexpected_token(self):
        code = "x = 10 + ;"
        with self.assertRaises(SyntaxError) as context:
            self.execute_code(code)
        self.assertIn("Expected a term after operator +", str(context.exception))

    def test_complex_nested_operations(self):
        code = "x = (10 + (5 * 3)) - ((20 / 4) + 2); print(x);"
        result = self.execute_code(code)
        self.assertEqual(result[-1], 18.0)  # Correct precedence and grouping

if __name__ == "__main__":
    unittest.main()
