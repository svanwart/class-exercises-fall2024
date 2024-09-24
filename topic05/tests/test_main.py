import unittest
from unittest.mock import patch

from app.arithmetic import Arithmetic
from app.ui import UserInterface


class TestCourseFilter(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_add_nums_works_with_valid_inputs(self):
        self.assertEqual(Arithmetic.add_nums(1, 2), 3)
        self.assertEqual(Arithmetic.add_nums(-1, 2), 1)

    def test_add_nums_raises_exception_with_invalid_inputs(self):
        self.assertRaises(TypeError, Arithmetic.add_nums, None, 2)
        self.assertRaises(TypeError, Arithmetic.add_nums, 2, None)
        self.assertRaises(TypeError, Arithmetic.add_nums, None, None)

    # # Mock input
    @patch("builtins.input", return_value="2")
    def test_prompt_user_for_number_with_valid_inputs(self, mock_input):
        self.assertEqual(UserInterface.prompt_user_for_number(), 2)

    # Mock input + mock print
    @patch("builtins.print")
    @patch("builtins.input", return_value="4")
    def test_main_with_valid_inputs(self, mock_input, mock_print):
        UserInterface.add_nums_from_user_input()
        mock_print.assert_called_with("The sum of 4 + 4 is:", 8)
