import pathlib
import sys
import unittest


CURRENT_DIR = pathlib.Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))


from PasswordStrengthChecker import PasswordStrengthChecker


class TestPasswordStrengthChecker(unittest.TestCase):
    def setUp(self):
        self.checker = PasswordStrengthChecker()

    def test_init_raises_value_error_when_min_length_is_too_small(self):
        with self.assertRaisesRegex(
            ValueError,
            r"La longitud mínima no puede ser menor a 4 caracteres.",
        ):
            PasswordStrengthChecker(min_length=3)

    def test_default_min_length_is_applied(self):
        self.assertEqual(self.checker.min_length, 8)

    def test_check_strength_raises_type_error_for_non_string_values(self):
        invalid_values = [None, 123, 12.5, ["Abc123!"], {"password": "Abc123!"}]

        for invalid_value in invalid_values:
            with self.subTest(invalid_value=invalid_value):
                with self.assertRaisesRegex(
                    TypeError,
                    r"La contraseña debe ser una cadena de texto \(string\).",
                ):
                    self.checker.check_strength(invalid_value)

    def test_check_strength_returns_very_weak_for_empty_or_whitespace_only_passwords(self):
        cases = ["", "   ", "\n\t "]

        for password in cases:
            with self.subTest(password=password):
                self.assertEqual(self.checker.check_strength(password), "MUY DÉBIL")

    def test_check_strength_returns_very_weak_for_common_passwords(self):
        cases = ["password", "Password", "123456", "CONTRASEÑA"]

        for password in cases:
            with self.subTest(password=password):
                self.assertEqual(self.checker.check_strength(password), "MUY DÉBIL")

    def test_check_strength_returns_weak_when_below_min_length(self):
        self.assertEqual(self.checker.check_strength("Ab1!"), "DÉBIL")

    def test_check_strength_returns_weak_when_score_is_low(self):
        self.assertEqual(self.checker.check_strength("abcdefgh"), "DÉBIL")

    def test_check_strength_returns_medium_for_two_criteria(self):
        self.assertEqual(self.checker.check_strength("Abc12345"), "MEDIANA")

    def test_check_strength_returns_strong_for_three_criteria(self):
        self.assertEqual(self.checker.check_strength("Abc123!X"), "FUERTE")

    def test_check_strength_returns_strong_for_long_password_with_multiple_criteria(self):
        self.assertEqual(self.checker.check_strength("SuperClave123!"), "FUERTE")


if __name__ == "__main__":
    unittest.main()
