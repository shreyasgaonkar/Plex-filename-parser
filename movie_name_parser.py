import os
import shutil

# Change current dir
os.chdir('/path/to/movies/directory')

# List all directories under current dir
directories_in_curdir = filter(os.path.isdir, os.listdir(os.curdir))

# Magic here!


def cleanFile(string):
    import re
    cleanfiles = []
    # Clean the file formats
    blacklist = ['1080p', '1080', 'blu ray', "bluray", "blu-ray", "4k",
                 "720p", "720", "dvdrip", "dvd", "brrip", "h264", "h265", "mp4"]
    roman = ['i', 'ii', 'iii', 'iv', 'iiii', 'v', 'vi', 'vii', 'viii', 'ix', 'x']

    # Clean the dots here
    def cleanDots(filename):
        return (filename.replace(".", " "))

    # Check for Movie year, if not then clean the dots if any
    cleanfiles = re.split(r'([12][90]\d{2})', string)

    # If no movie year, then skip formatting
    if(len(cleanfiles) < 2):
        cleanfiles = cleanDots(cleanfiles[0])

    # There's movie year, time to clean them!
    else:
        year = cleanfiles[1]
        temp = re.split(r'[\(\[\{\<]', cleanfiles[0])
        cleanfiles[0] = temp[0]
        cleanfiles = (cleanDots(cleanfiles[0]) + "("+year+")")

    # Check for any extra Chars that we might have missed earlier
    for i in blacklist:
        if i in cleanfiles.lower():
            temp = re.split(i, cleanfiles)
            cleanfiles = temp[0]

    # Check for any roman chars
    temp = (cleanfiles.split(" "))
    for i, s in enumerate(temp):
        if(s.lower() in roman):
            temp[i] = s.upper()
    cleanfiles = " ".join(temp)

    # Ensure it returns the cleaned value as needed
    return (cleanfiles.capitalize().title())


for i in directories_in_curdir:
    print("Original filename: {}".format(i))
    cleanFile(i)
    print("New filename: {}".format(cleanFile(i)))
    # If changes in filenames, rename
    try:
        if(i != cleanFile(i)):
            shutil.move(i, cleanFile(i))
    # If the filename exists, skip
    except:
        pass
    else:
        print("skipped")
        print("===")
