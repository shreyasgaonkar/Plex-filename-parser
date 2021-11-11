import unittest
import tv_show_name_parser


class TestTvShowNameParser(unittest.TestCase):

    def test_capitalize_title(self):
        self.assertEqual(
            tv_show_name_parser.capitalize_title("VeNom"), "Venom")
        self.assertEqual(tv_show_name_parser.capitalize_title(
            "grey'S anatomy"), "Grey's Anatomy")
        self.assertEqual(tv_show_name_parser.capitalize_title(
            "rise.of.the.planet.of.the.apes.iii.2015"), "Rise.of.the.planet.of.the.apes.iii.2015")
        self.assertEqual(tv_show_name_parser.capitalize_title(
            "harry potter and the half blood prince"), "Harry Potter And The Half Blood Prince")

    def test_remove_unwanted_chars(self):
        self.assertEqual(
            tv_show_name_parser.remove_unwanted_chars("     Venom     "), "Venom")
        self.assertEqual(tv_show_name_parser.remove_unwanted_chars(
            "grey'S.anatomy"), "grey'S anatomy")
        self.assertEqual(
            tv_show_name_parser.remove_unwanted_chars("rise.of.the.planet.of.the.apes.iii.2015"), "rise of the planet of the apes iii 2015")
        self.assertEqual(
            tv_show_name_parser.remove_unwanted_chars("Batman%20Begins   (2005)"), "Batman Begins (2005)")

    def test_roman_char_fix(self):
        self.assertEqual(
            tv_show_name_parser.roman_char_fix("VeNom"), "VeNom")
        self.assertEqual(
            tv_show_name_parser.roman_char_fix("grey'S anatomy"), "grey'S anatomy")
        self.assertEqual(
            tv_show_name_parser.roman_char_fix("rise of the planet of the apes iii 2015"), "rise of the planet of the apes III 2015")
        self.assertEqual(
            tv_show_name_parser.roman_char_fix("Harry Potter And The Half Blood Prince"), "Harry Potter And The Half Blood Prince")

    def test_blacklist_word_fix(self):
        self.assertEqual(
            tv_show_name_parser.blacklist_word_fix("harry potter and the half blood prince dvdrip 2006"), "harry potter and the half blood prince")
        self.assertEqual(
            tv_show_name_parser.blacklist_word_fix("rise of the planet of the apes iii 2015"), "rise of the planet of the apes iii 2015")


if __name__ == "__main__":
    unittest.main()
