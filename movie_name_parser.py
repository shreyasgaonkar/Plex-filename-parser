import re
import os
import shutil
import string

# Change this to point to the directory containing movies
TARGET_DIR = '/path/to/movies/directory'


"""
1. Get All directories
2. Get individual files
3. Parse files and directory name
"""

BLACKLIST = ['1080p', '1080', 'blu ray', "bluray", "blu-ray", "4k",
             "720p", "720", "dvdrip", "dvd", "brrip", "h264", "h265", "mp4"]
ROMAN = ['i', 'ii', 'iii', 'iv', 'iiii', 'v', 'vi', 'vii', 'viii', 'ix', 'x']


def get_all_files(target_dir):
    """ Check all files and folders to verify the naming convention """
    for path, directories, files in os.walk(target_dir):
        for directory in directories:
            clean_directory(path, directory)
        for file in files:
            clean_file(path, file)


def clean_directory(path_name, dir_name):
    """
    Clean directory name as per Plex standards

    1. Remove any trailing spaces and replace %20 with whitespace
    2. Check if directory name contains year. Use if present
    3. Remove any blacklisted keywords after adding the year
    4. Remove extra whitespace and capitalize title
    5. Check for any Roman chars and uppercase them
    6. Rename the original directory
    """

    original_dir_name = dir_name
    dir_name = dir_name.strip()

    dir_name = capitalize_title(dir_name)
    dir_name = remove_unwanted_chars(dir_name)
    dir_name = year_fix(dir_name)
    dir_name = blacklist_word_fix(dir_name)
    dir_name = remove_whitespaces(dir_name)
    dir_name = roman_char_fix(dir_name)

    # Replace if any changes
    if dir_name != original_dir_name:
        print(f"Original dir name: {original_dir_name}")
        shutil.move(os.path.join(path_name, original_dir_name),
                    os.path.join(path_name, dir_name))
        print(f"Final dir name: {dir_name}")


def clean_file(path_name, file_name):
    """
    Clean file name as per Plex standards

    1. Ignore any dot files
    2. Check if directory name contains year. Use if present
    3. Remove any blacklisted keywords after adding the year
    4. Remove extra whitespace and capitalize title
    5. Check for any Roman chars and uppercase them
    6. Rename the original file
    """
    if file_name.startswith('.'):
        return

    original_file_name = file_name
    file_ext = os.path.splitext(file_name)[1][1:]

    file_name = capitalize_title(file_name)
    file_name = remove_unwanted_chars(file_name)
    file_name = year_fix(file_name)
    file_name = blacklist_word_fix(file_name)
    file_name = remove_whitespaces(file_name)
    file_name = roman_char_fix(file_name)
    file_name = f'{file_name}.{file_ext}'

    # Rename the files
    if file_name != original_file_name:
        print(f'Original filename: {original_file_name}')
        shutil.move(os.path.join(path_name, original_file_name),
                    os.path.join(path_name, file_name))
        print(f'Updated filename: {file_name}')


def roman_char_fix(text):
    """ Return file/dir name for Roman chars """
    temp = text.split(" ")
    for i, j in enumerate(temp):
        if j.lower() in ROMAN:
            temp[i] = j.upper()
    text = " ".join(temp)
    return text


def year_fix(text):
    """ Update year in the title if it exists """
    parsed_name = re.split(r'([12][90]\d{2})', text)

    if len(parsed_name) > 1:
        title, year, _ = parsed_name
        title = re.split(r'[\(\[\{\<]', title)
        title = ''.join(title)
        return f'{title}({year})'
    else:
        return parsed_name[0]


def blacklist_word_fix(text):
    """ Remove any blacklisted keywords after adding the year """
    for keyword in BLACKLIST:
        if keyword in text.lower():
            temp = re.split(keyword, text)
            text = temp[0]
    return text


def remove_whitespaces(text):
    """ Remove extra whitespace and capitalize title """
    text = re.sub(r'\s+', ' ', text)
    text = text.capitalize().title()
    return text


def remove_unwanted_chars(text):
    """ Replace '.' & '%20' and any whitespaces """
    text = text.replace(".", " ").replace("-", " ").replace("%20", " ")
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


def capitalize_title(text):
    """ Alternative to string.title() for apostrophes """
    text = string.capwords(text).strip()  # .title() replaces 's -> 'S
    return text


def main():
    """ Main function """
    get_all_files(TARGET_DIR)


if __name__ == '__main__':
    main()
