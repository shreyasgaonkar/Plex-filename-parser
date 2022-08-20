import re
import string

BLACKLIST = {"1080p", "1080", "blu ray", "bluray", "blu-ray", "4k",
             "720p", "720", "480", "480p", "webdl" , "dvdrip", "dvd", "brrip", "h264", "h265", "mp4", "hdtv", "x264", "hdtvrip"}
ROMAN = {"i", "ii", "iii", "iv", "iiii", "v", "vi", "vii", "viii", "ix", "x"}


class BackgroundColors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def roman_char_fix(text: str) -> str:
    """Return file/dir name with Roman chars upper-cased"""
    if "." in text:
        words = text.split(".")
    else:
        words = text.split(" ")

    for index, word in enumerate(words):
        if word.lower() in ROMAN:
            words[index] = word.upper()
    return " ".join(words)


def blacklist_word_fix(text: str) -> str:
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


def remove_unwanted_chars(text: str) -> str:
    """Replace '.' & '%20' and any whitespaces"""
    text = text.replace(".", " ").replace("%20", " ").strip()
    text = re.sub(r"\s+", " ", text)
    return text


def capitalize_title(text: str) -> str:
    """Alternative to string.title() for apostrophes"""
    text = string.capwords(text.replace(".", " ")).strip()  # .title() replaces 's -> 'S
    return text


def remove_whitespaces(text: str) -> str:
    """ Remove extra whitespace and capitalize title """
    text = re.sub(r'\s+', ' ', text)
    text = capitalize_title(text)
    return text
