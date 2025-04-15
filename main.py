import unittest
from AES import mix_rows, mix_columns, convertToUnicode


class TestMixRows(unittest.TestCase):

    def test_columns_should_not_stay_the_same(self):
        initial_row = [[0,2,6,8,12,4,4]]
        self.assertNotEqual(mix_rows(initial_row), initial_row)
    
    def test_columns_should_not_stay_the_same_for_strings(self):
        initial_row = [["0", "2", "6", "8", "12", "4", "4"]]
        self.assertNotEqual(mix_rows(initial_row), initial_row)
    
    def test_first_row_is_moved_one_spot(self):
        initial_row = [[0,2,6,8,12,4,4]]
        expected_row = [[2,6,8,12,4,4,0]]
        self.assertEqual(mix_rows(initial_row), expected_row)

    def test_second_row_is_moved_two_spots(self):
        initial_row = [[0,2,6,8,12,4,4], 
                       [0,2,6,8,12,4,4]]
        
        expected_row = [[2,6,8,12,4,4,0],
                        [6,8,12,4,4,0,2]]
        self.assertEqual(mix_rows(initial_row), expected_row)


class TestMixColumns(unittest.TestCase):
    def test_first_column_get_mixed(self):
        initial_row = [[1], [5], [9],[13]]
        expected_row = [[39],[51], [63],[43]]

        self.assertEqual(mix_columns(initial_row), expected_row)
    
    def test_first_column_get_mixed_for_strings(self):
        initial_row = [convertToUnicode("j"), convertToUnicode("a"), convertToUnicode("b"),convertToUnicode("z")]
        expected_row =  [[723], [716], [765], [757]]

        self.assertEqual(mix_columns(initial_row), expected_row)

    def test_multiple_columns_get_mixed(self):
        initial_row = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
        expected_row = [[39,46,53,60],[51,58,65,72], [63,70,77,84],[43,50,57,64]]

        self.assertEqual(mix_columns(initial_row), expected_row)

    def test_single_change_causes_many_changes(self):
        initial_row = [[1,3,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
        expected_row = [[39, 48, 53, 60], [51, 59, 65, 72], [63, 71, 77, 84], [43, 53, 57, 64]]

        self.assertEqual(mix_columns(initial_row), expected_row)

class TestUnicodeConversion(unittest.TestCase):
    def test_simple_text_to_unicode_representation(self):
        input = "ChatGPT 💡"
        expected = [67, 104, 97, 116, 71, 80, 84, 32, 128161]
        
        self.assertEqual(convertToUnicode(input), expected)


if __name__ == "__main__":
    unittest.main()