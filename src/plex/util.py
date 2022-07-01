import re
import string

BLACKLIST = {"1080p", "1080", "blu ray", "bluray", "blu-ray", "4k",
             "720p", "720", "dvdrip", "dvd", "brrip", "h264", "h265", "mp4"}
ROMAN = {"i", "ii", "iii", "iv", "iiii", "v", "vi", "vii", "viii", "ix", "x"}


def roman_char_fix(text):
    """Return file/dir name with Roman chars upper-cased"""
    if "." in text:
        words = text.split(".")
    else:
        words = text.split(" ")

    for index, word in enumerate(words):
        if word.lower() in ROMAN:
            words[index] = word.upper()
    return " ".join(words)


def blacklist_word_fix(text):
    """Remove blacklisted keywords"""
    if "." in text:
        title = text.split(".")
    else:
        title = text.split(" ")
    new_title = ""

    for word in title:
        if not word.lower() in BLACKLIST:
            new_title += f"{word} "
    return new_title.strip()


def remove_unwanted_chars(text):
    """Replace '.' & '%20' and any whitespaces"""
    text = text.replace(".", " ").replace("-", " ").replace("%20", " ").strip()
    text = re.sub(r"\s+", " ", text)
    return text


def capitalize_title(text):
    """Alternative to string.title() for apostrophes"""
    text = string.capwords(text.replace(".", " ")).strip()  # .title() replaces 's -> 'S
    return text


def remove_whitespaces(text):
    """ Remove extra whitespace and capitalize title """
    text = re.sub(r'\s+', ' ', text)
    text = capitalize_title(text)
    return text