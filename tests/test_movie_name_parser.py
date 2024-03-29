from plex.movie_name_parser import capitalize_title, remove_unwanted_chars, year_fix, remove_whitespaces, roman_char_fix

# Define the test string as the key, and value as another key-value with key being the method against the original string, and the value is the target result
test_dict = {
    "VeNom": {
        "capitalize_title": (capitalize_title, "Venom"),
        "year_fix": (year_fix, "VeNom"),
        "remove_unwanted_chars": (remove_unwanted_chars, "VeNom"),
        "roman_char_fix": (roman_char_fix, "VeNom"),
        "remove_whitespaces": (remove_whitespaces, "Venom")
    },
    "grey'S anatomy": {
        "capitalize_title": (capitalize_title, "Grey's Anatomy"),
        "year_fix": (year_fix, "grey'S anatomy"),
        "remove_unwanted_chars": (remove_unwanted_chars, "grey'S anatomy"),
        "roman_char_fix": (roman_char_fix, "grey'S anatomy"),
        "remove_whitespaces": (remove_whitespaces, "Grey's Anatomy")
    },
    "rise.of.the.planet.of.the.apes.iii.2015": {
        "capitalize_title": (capitalize_title, "Rise Of The Planet Of The Apes Iii 2015"),
        "year_fix": (year_fix, "rise of the planet of the apes iii (2015)"),
        "remove_unwanted_chars": (remove_unwanted_chars, "rise of the planet of the apes iii 2015"),
        "roman_char_fix": (roman_char_fix, "rise of the planet of the apes III 2015"),
        "remove_whitespaces": (remove_whitespaces, "Rise Of The Planet Of The Apes Iii 2015")
    },
    "harry potter and the half blood prince dvdrip 2006": {
        "capitalize_title": (capitalize_title, "Harry Potter And The Half Blood Prince Dvdrip 2006"),
        "year_fix": (year_fix, "harry potter and the half blood prince dvdrip (2006)"),
        "remove_unwanted_chars": (remove_unwanted_chars, "harry potter and the half blood prince dvdrip 2006"),
        "roman_char_fix": (roman_char_fix, "harry potter and the half blood prince dvdrip 2006"),
        "remove_whitespaces": (remove_whitespaces, "Harry Potter And The Half Blood Prince Dvdrip 2006")
    },
    "Batman%20Begins   (2005)": {
        "capitalize_title": (capitalize_title, "Batman%20begins (2005)"),
        "year_fix": (year_fix, "Batman Begins (2005)"),
        "remove_unwanted_chars": (remove_unwanted_chars, "Batman Begins (2005)"),
        "roman_char_fix": (roman_char_fix, "Batman%20Begins   (2005)"),
        "remove_whitespaces": (remove_whitespaces, "Batman%20begins (2005)")
    },
}


def generic_test_function(function_name: str) -> None:
    for key, value in test_dict.items():
        test_string = key
        method = value[function_name][0]
        target_string = value[function_name][1]
        assert method(test_string) == target_string


def test_all():
    """Run all test. Test names are the keys in the first (or any) key from test_dict"""
    # Get all testnames
    all_tests = test_dict[next(iter(test_dict))].keys()
    for test in all_tests:
        generic_test_function(f"{test}")
