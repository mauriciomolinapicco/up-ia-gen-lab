import sys
from pathlib import Path
import unittest


sys.path.insert(0, str(Path(__file__).resolve().parent))

from PasswordStrengthChecker import PasswordStrengthChecker


class TestPasswordStrengthChecker(unittest.TestCase):
    def setUp(self):
        self.checker = PasswordStrengthChecker()

    def test_constructor_raises_value_error_when_min_length_is_too_small(self):
        with self.assertRaises(ValueError) as context:
            PasswordStrengthChecker(min_length=3)

        self.assertEqual(
            str(context.exception),
            "La longitud mínima no puede ser menor a 4 caracteres.",
        )

    def test_check_strength_raises_type_error_for_non_string_values(self):
        invalid_values = [None, 123, 12.5, [], {}, True]

        for value in invalid_values:
            with self.subTest(value=value):
                with self.assertRaises(TypeError) as context:
                    self.checker.check_strength(value)

                self.assertEqual(
                    str(context.exception),
                    "La contraseña debe ser una cadena de texto (string).",
                )

    def test_check_strength_returns_very_weak_for_empty_or_whitespace_passwords(self):
        self.assertEqual(self.checker.check_strength(""), "MUY DÉBIL")
        self.assertEqual(self.checker.check_strength("   \t\n  "), "MUY DÉBIL")

    def test_check_strength_returns_very_weak_for_common_passwords_case_insensitive(self):
        common_passwords = ["password", "Password", "CONTRASEÑA", "Hola123"]

        for password in common_passwords:
            with self.subTest(password=password):
                self.assertEqual(self.checker.check_strength(password), "MUY DÉBIL")

    def test_check_strength_returns_weak_when_password_is_shorter_than_minimum(self):
        self.assertEqual(self.checker.check_strength("Ab1!xyz"), "DÉBIL")

    def test_check_strength_returns_weak_when_password_has_only_one_strength_criterion(self):
        self.assertEqual(self.checker.check_strength("abcdefgh"), "DÉBIL")

    def test_check_strength_returns_medium_for_two_strength_criteria(self):
        self.assertEqual(self.checker.check_strength("Abcdef12"), "MEDIANA")

    def test_check_strength_returns_strong_for_three_strength_criteria(self):
        self.assertEqual(self.checker.check_strength("Abcdef1!"), "FUERTE")

    def test_check_strength_returns_strong_for_long_passwords_with_extra_length_bonus(self):
        self.assertEqual(self.checker.check_strength("Abcdef12!XYZ"), "FUERTE")

    def test_check_strength_respects_custom_min_length(self):
        checker = PasswordStrengthChecker(min_length=12)

        self.assertEqual(checker.check_strength("Abcdef1!"), "DÉBIL")
        self.assertEqual(checker.check_strength("Abcdef12!XYZ"), "FUERTE")


if __name__ == "__main__":
    unittest.main()