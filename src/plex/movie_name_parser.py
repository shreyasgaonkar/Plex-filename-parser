import re
import os
import shutil
import sys


from plex.util import BLACKLIST, roman_char_fix, capitalize_title, remove_unwanted_chars, remove_whitespaces

# Change this to point to the directory containing movies
TARGET_DIR = '/path/to/movies/directory'


"""
1. Get All directories
2. Get individual files
3. Parse files and directory name
"""


def get_all_files(target_dir: str) -> None:
    """ Check all files and folders to verify the naming convention """
    for path, directories, files in os.walk(target_dir):
        for directory in directories:
            clean_directory(path, directory)
        for file in files:
            clean_file(path, file)


def clean_directory(path_name: str, dir_name: str) -> None:
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
        try:
            shutil.move(os.path.join(path_name, original_dir_name), os.path.join(path_name, dir_name))
        except OSError as e:
            if "Destination path" and "already exists" in str(e):
                print("Dir already exists")
                handle_directory_exists_error(dir_name, original_dir_name, path_name)
                sys.exit(1)
        print(f"Final dir name: {dir_name}")


def handle_directory_exists_error(dir_name, original_dir_name, path_name):
    """List all files in the original dir and move the path to new dir"""

    old_dir_path = f'{path_name}/{original_dir_name}'

    for path, directories, files in os.walk(old_dir_path):
        # for directory in directories:
        #     print(f"directory is {directory}")
        #     print(f"Path is {path}")
        for file in files:
            print(f"Files are {file}")
            print(f"Current path is {path}")
            new_path = path.replace(original_dir_name, dir_name)

            if not os.path.exists(new_path):
                os.makedirs(new_path)

            shutil.move(os.path.join(path, file), os.path.join(new_path, file))
            print(f"Moved the file from {original_dir_name} to {dir_name}")

    print(f"Removing dir: {path_name}/{original_dir_name}")
    shutil.rmtree(f"{path_name}/{original_dir_name}")


def clean_file(path_name: str, file_name: str) -> None:
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

    remove_empty_files(path_name)
    file_name = capitalize_title(file_name)
    file_name = remove_unwanted_chars(file_name)
    file_name = year_fix(file_name)
    file_name = blacklist_word_fix(file_name)
    file_name = remove_whitespaces(file_name)
    file_name = roman_char_fix(file_name)
    file_name = remove_duplicate_file_ext(file_name, file_ext)
    file_name = f'{file_name}.{file_ext}'

    # Rename the files
    if file_name != original_file_name:
        print(f'Original filename: {original_file_name}')
        shutil.move(os.path.join(path_name, original_file_name),
                    os.path.join(path_name, file_name))
        print(f'Updated filename: {file_name}')


def remove_duplicate_file_ext(file_name: str, file_ext: str) -> str:
    file_name = file_name.replace(file_ext.capitalize(), '').strip()
    return file_name


def remove_empty_files(path_name):
    for root, _, files in os.walk(path_name):
        for f in files:
            fullpath = os.path.join(root, f)
            try:
                if os.path.getsize(fullpath) < 1:
                    print(fullpath)
                    os.remove(fullpath)
            except Exception:
                print("Error" + fullpath)


def year_fix(text: str) -> str:
    """ Update year in the title if it exists """
    text = remove_unwanted_chars(text)
    parsed_name = re.split(r'([12][90]\d{2})', text)

    if len(parsed_name) > 1:
        title, year, *_ = parsed_name
        title = re.split(r'[\(\[\{\<]', title)
        title = ''.join(title)
        return f'{title}({year})'
    return parsed_name[0]


def blacklist_word_fix(text: str) -> str:
    """ Remove any blacklisted keywords after adding the year """
    for keyword in BLACKLIST:
        if keyword in text.lower():
            temp = re.split(keyword, text)
            text = temp[0]
    return text


def main():
    """ Main function """
    get_all_files(TARGET_DIR)


if __name__ == '__main__':
    main()
