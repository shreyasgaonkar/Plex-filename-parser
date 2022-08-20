from plex.tv_show_name_parser import (
    capitalize_title,
    blacklist_word_fix,
    remove_unwanted_chars,
    roman_char_fix,
)

# Define the test string as the key, and value as another key-value with key being the method against the original string, and the value is the target result
test_dict = {
    "The.Secret.Circle.S01E19": {
        "capitalize_title": (capitalize_title, "The Secret Circle S01e19"),
        "blacklist_word_fix": (blacklist_word_fix, "The Secret Circle S01E19"),
        "remove_unwanted_chars": (remove_unwanted_chars, "The Secret Circle S01E19"),
        "roman_char_fix": (roman_char_fix, "The Secret Circle S01E19"),
    },
    "Fargo S01E07 HDTV x264 AAC E-Subs [GWC]": {
        "capitalize_title": (
            capitalize_title,
            "Fargo S01e07 Hdtv X264 Aac E-subs [gwc]",
        ),
        "blacklist_word_fix": (
            blacklist_word_fix,
            "Fargo S01E07 AAC E-Subs [GWC]",
        ),
        "remove_unwanted_chars": (
            remove_unwanted_chars,
            "Fargo S01E07 HDTV x264 AAC E-Subs [GWC]",
        ),
        "roman_char_fix": (roman_char_fix, "Fargo S01E07 HDTV x264 AAC E-Subs [GWC]"),
    },
    "Supernatural S1E08 - Bugs": {
        "capitalize_title": (capitalize_title, "Supernatural S1e08 - Bugs"),
        "blacklist_word_fix": (blacklist_word_fix, "Supernatural S1E08 - Bugs"),
        "remove_unwanted_chars": (remove_unwanted_chars, "Supernatural S1E08 - Bugs"),
        "roman_char_fix": (roman_char_fix, "Supernatural S1E08 - Bugs"),
    },
    "Silicon.Valley.S03E09.720p.HDTV.275MB.GoenWae": {
        "capitalize_title": (
            capitalize_title,
            "Silicon Valley S03e09 720p Hdtv 275mb Goenwae",
        ),
        "blacklist_word_fix": (
            blacklist_word_fix,
            "Silicon Valley S03E09 275MB GoenWae",
        ),
        "remove_unwanted_chars": (
            remove_unwanted_chars,
            "Silicon Valley S03E09 720p HDTV 275MB GoenWae",
        ),
        "roman_char_fix": (
            roman_char_fix,
            "Silicon Valley S03E09 720p HDTV 275MB GoenWae",
        ),
    },
}


def append_optional_params(input_string: str, optional_params: list) -> list:
    return [input_string] + optional_params


def generic_test_function(function_name: str) -> None:
    """

    Dict created with key as the input string to be tested,
    value as another dict with API name and the target string.

    Nested dict structure:
        - key (string): API method to be called
        - value (two valued tuple):
            - first: API name (again)
            - second: expected return string from the API
    """

    for key, value in test_dict.items():
        input_string = key
        method, target_string, *optional_params = value[function_name]

        # Certain function may have more than one params, append and assert
        if optional_params:
            params = append_optional_params(input_string, optional_params)
            assert method(*params) == target_string
        else:
            params = input_string
            assert method(params) == target_string


def test_all():
    """Run all test. Test names are the keys in the first (or any) key from test_dict"""
    # Get all testnames
    all_tests = test_dict[next(iter(test_dict))].keys()
    for test in all_tests:
        generic_test_function(test)
