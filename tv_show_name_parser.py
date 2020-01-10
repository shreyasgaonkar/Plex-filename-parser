#!/usr/bin/python3
import shutil
import os
import re

os.chdir('/Users/sggaonk/tmp')

blacklists = {'1080p', '1080', 'blu ray', "bluray", "blu-ray", "4k",
              "720p", "720", "dvdrip", "dvd", "brrip", "h264", "h265", "mp4"}
romans = {'i', 'ii', 'iii', 'iv', 'iiii', 'v', 'vi', 'vii', 'viii', 'ix', 'x'}


def clean_file(file):
    """ For a given filename, sanitize it as per Plex's standards """
    cleanfiles = []
    # Clean the file formats

    filename, file_extension = os.path.splitext(file)

    print(f"Origial file: {filename}")
    # Clean file names having excess spaces and periods
    filename = filename.strip()
    filename = filename.replace(".", " ")
    filename = filename.replace("%20", " ")

    try:
        # Get the show season from it's parent dir
        show_season = re.findall(r'([Ss]eason\ \d+)', filename)
        show_season = show_season[0].split(" ")[-1]
        print(f"Show season: {show_season}")

        filename = re.split(r'/', filename)
        filename = filename[-1]
        print(f"Filename: {filename}")

        # Check if a blacklisted word present, remove it.
        for blacklist in blacklists:
            if blacklist in filename.lower():
                temp_filename = file.lower().split(blacklist)
                temp_filename = temp_filename[0].title()

        print("~~")

        # Check for episode number
        episode_number = re.findall(r'\d+', temp_filename)
        print(f"Episode# {episode_number}")

        filename = temp_filename.strip() + file_extension
        print(f"Process file: {filename}")

    except Exception as e:
        print(e)


# Directory functions


def return_dir_name(path, match, season):
    """ Create directory name as required """
    return "".join(path) + '/' + match + " (" + "".join(season) + ")"


def change_dir_name(new_name, old_name):
    """ Renames the directory using shutil """
    try:
        if(new_name != old_name):
            shutil.move(old_name, new_name)
    # If the filename exists, skip
    except Exception as e:
        print(e)


def clean_directory(directory):
    """ Change dir name as per Plex standards. """

    org_directory = directory

    directory = directory.split("/")
    path = directory[:-1]
    directory = directory[-1]

    try:
        season = re.findall(r'[Ss]eason\ \d+', directory)
        if not season:
            return "Not a valid TV show directory"

        # Make sure we are not adding '(' to the filename on every run
        directory = directory.replace('(', '')
        match = re.split(r'[Ss]eason\ \d+', directory)
        match = match[0].strip()

        # Sanitize the output
        print(return_dir_name(path, match, season))
        change_dir_name(return_dir_name(path, match, season), org_directory)

    except Exception as e:
        print(e)
        return org_directory


# for i in directories_in_curdir:
#     cleanFile(i)
# Check all files and folder if we need to change any values
for root, dirs, files in os.walk(".", topdown=True):
    for name in dirs:
        clean_directory(os.path.join(root, name))
    for name in files:
        clean_file(os.path.join(root, name))
