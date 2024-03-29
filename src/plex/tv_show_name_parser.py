#!/usr/bin/python3
# -*- coding: utf-8 -*-


import shutil
import os
import concurrent.futures  # for multithreading
import re
from typing import List, Union, Any

from plex.util import roman_char_fix, blacklist_word_fix, remove_unwanted_chars, capitalize_title

# Change this to point to the directory containing TV shows
TARGET_DIR = "/path/to/tvshows/directory"


def get_season_and_episode(file_name: str, file_path: str) -> List[Union[str, Any]]:
    # Check if file name contains SXXEXX format, if so rename as Plex requires
    season_and_episode = re.split(r'([S]\d{,2}[E]\d{,2})', file_name, re.IGNORECASE)
    season_and_episode = list(filter(None, season_and_episode))  # Remove empty vals

    # sXXeXX should be lowercase
    season_and_episode = [i.lower() if i.startswith("S") else capitalize_title(i)
                          for i in season_and_episode]

    season_and_episode = [i.replace("-", "").strip()
                          for i in season_and_episode]

    # Here sXXeXX can be either at 1st or 2nd position in the array.
    # If this is at first, get season from parent. If at second, don't change
    if re.findall(r'([S]\d{,2}[E]\d{,2})', season_and_episode[0], re.IGNORECASE):
        season_and_episode.insert(0, file_path.split("/")[-1])

    return season_and_episode


def clean_file(directory_path: str, file_name: str) -> None:
    """
    For a given filename, sanitize it as per Plex's standards

    1. Clean the name of the individual file. If no name present, grab name from the parent.
    2. Year of release is optional. If present add it under `()`
    """

    original_file_name = file_name

    file_name, file_extension = os.path.splitext(file_name)

    # Ignore dot files as they don't have extensions
    if file_extension:
        clean_file_name(directory_path, file_name,
                        file_extension, original_file_name)


def clean_file_name(file_path: str, file_name: str, file_extension: str, original_file_name: str) -> None:
    """
    Clean filename as per Plex standards:
    https://support.plex.tv/articles/naming-and-organizing-your-tv-show-files/

    1. Capitalize words as needed and remove unwanted whitespaces
    2. Extract `SXXEXX` from the filename
    3. Get show name from grandparent, rename with additional params and file extension.
    """

    # 1. Capitalize title & clean string
    file_name = capitalize_title(os.path.splitext(file_name)[0])
    file_name = remove_unwanted_chars(file_name)
    file_name = blacklist_word_fix(file_name)
    file_name = roman_char_fix(file_name)
    season_and_episode = get_season_and_episode(file_name, file_path)

    rename_file(season_and_episode, file_extension,
                original_file_name, file_path)


def rename_file(season_and_episode: Any, file_extension: str, original_file_name: str, file_path: str) -> None:
    """
    Rename files as per Plex's recommendations.
    Eg: Grey's Anatomy (2005) - s01e02 - The First Cut is the Deepest.avi
    """
    new_file_name = f"{' - '.join(season_and_episode)}{file_extension}"

    try:
        if original_file_name != new_file_name:
            shutil.move(os.path.join(file_path, original_file_name), os.path.join(
                file_path, new_file_name))
            print(f"Renamed file: {original_file_name} -> {new_file_name}")
    except Exception as exp:
        print(exp)


def change_dir_name(new_name: str, old_name: str) -> None:
    """ Rename the directory using shutil """
    try:
        if new_name != old_name:
            shutil.move(old_name, new_name)
            print(f"Renamed Directory: {old_name} -> {new_name}")
    # If the filename exists, skip
    except Exception as e:
        print(e)


def clean_directory(directory_path: str, directory_name: str) -> Any:
    """
    Function to rename directory name as per Plex standards.

    1. Capitalize title
    2. If the directory is a season, rename directory to Season XX
    3. Remove any year if present
    """

    original_dir_path = directory_path
    original_directory_name = directory_name

    # 1. Capitalize title & roman characters. Remove blacklisted words from title
    directory_name = capitalize_title(directory_name)
    directory_name = blacklist_word_fix(directory_name)
    directory_name = roman_char_fix(directory_name)

    # 2. If the directory is a season, rename directory to Season XX
    # 3. Remove any year present
    season = re.findall(r"([Ss]eason)\ ?(\d+)", directory_name)
    season_shorthand = re.findall(r"([Ss])\ ?(\d+)", directory_name)
    season = season or season_shorthand

    if not season:
        try:
            change_dir_name(os.path.join(original_dir_path, directory_name), os.path.join(
                original_dir_path, original_directory_name))
        except Exception as e:
            print(e)
            return original_directory_name

    directory_name = f"Season {season[0][-1]:0>2}"

    try:
        # Rename the directories
        change_dir_name(os.path.join(original_dir_path, directory_name),
                        os.path.join(original_dir_path, original_directory_name))

    except Exception as e:
        print(e)
        return original_directory_name


def main():
    """
    Main function to clean all directories and files recursively to be renamed as per Plex's standards
    """

    print(
        f"[INFO] Starting script under {TARGET_DIR} directory. If this isn't right, please replace the value of `TARGET_DIR` variable in this script.\n")

    for dir_paths, dir_names, files in os.walk(TARGET_DIR, topdown=True):

        # Multithreading
        with concurrent.futures.ThreadPoolExecutor() as executor:
            [executor.submit(
                clean_directory, dir_paths, dir_name) for dir_name in dir_names]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            [executor.submit(
                clean_file, dir_paths, file) for file in files]

    print("\n[INFO] Finished execution")


if __name__ == "__main__":
    main()
