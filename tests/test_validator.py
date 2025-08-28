import unittest

from validate_postcode.validator import validate_post_code


class TestPostCodeValidation(unittest.TestCase):
    def test_basic_format(self):
        self.assertEqual(validate_post_code("CR2 6XH"), (True, "Valid post code."))
        self.assertEqual(validate_post_code("DN55 1PT"), (True, "Valid post code."))
        self.assertEqual(validate_post_code("CR222 6XH"), (False, "Does not match general postcode format."))
        self.assertEqual(validate_post_code("DN555 1PT"), (False, "Does not match general postcode format."))


    def test_invalid_start_chars(self):
        self.assertEqual(validate_post_code("QR2 6XH"), (False, "Invalid first letter."))
        self.assertEqual(validate_post_code("VR2 6XH"), (False, "Invalid first letter."))
        self.assertEqual(validate_post_code("XR2 6XH"), (False, "Invalid first letter."))


    def test_invalid_second_chars(self):
        self.assertEqual(validate_post_code("CI2 6XH"), (False, "Invalid second letter."))
        self.assertEqual(validate_post_code("CJ2 6XH"), (False, "Invalid second letter."))
        self.assertEqual(validate_post_code("CZ2 6XH"), (False, "Invalid second letter."))


    def test_invalid_final_chars(self):
        self.assertEqual(validate_post_code("CR2 6CH"), (False, "Invalid letters in the last two positions."))
        self.assertEqual(validate_post_code("CR2 6IH"), (False, "Invalid letters in the last two positions."))
        self.assertEqual(validate_post_code("CR2 6KH"), (False, "Invalid letters in the last two positions."))
        self.assertEqual(validate_post_code("CR2 6MH"), (False, "Invalid letters in the last two positions."))
        self.assertEqual(validate_post_code("CR2 6OH"), (False, "Invalid letters in the last two positions."))
        self.assertEqual(validate_post_code("CR2 6VH"), (False, "Invalid letters in the last two positions."))
        self.assertEqual(validate_post_code("CR2 6XC"), (False, "Invalid letters in the last two positions."))
        self.assertEqual(validate_post_code("CR2 6XI"), (False, "Invalid letters in the last two positions."))
        self.assertEqual(validate_post_code("CR2 6XK"), (False, "Invalid letters in the last two positions."))
        self.assertEqual(validate_post_code("CR2 6XM"), (False, "Invalid letters in the last two positions."))
        self.assertEqual(validate_post_code("CR2 6XO"), (False, "Invalid letters in the last two positions."))
        self.assertEqual(validate_post_code("CR2 6XV"), (False, "Invalid letters in the last two positions."))


    def test_central_london_districts(self):
        self.assertEqual(validate_post_code("W1A 0AX"), (True, "Valid post code."))
        self.assertEqual(validate_post_code("EC1A 1BB"), (True, "Valid post code."))
