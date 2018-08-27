#!/usr/bin/python
import re
import os
import shutil
from os import walk
files = os.listdir(".")

for a in files:
    storedval = a
    blacklist = ['1080p', '1080', 'blu ray', "bluray", "blu-ray", "4k", "720p",
                 "720", "dvdrip", "dvd", "brrip", "h264", "h265", "HDTV", "hdtv"]

    # white spaces
    a = a.strip()

    if(a.count('.')) > 1:
        a = a.replace(".", " ")

    # Replace last space with .
    a = a[::-1].replace(" ", ".", 1)[::-1]
    print "Adjusted extension is ---> {}".format(a)

    for i in blacklist:
        if i in a:
            print i
            b = a.split(i)

            print b
            # white spaces after dropping the blacklisted values
            for j in range(0, len(b)):
                b[j] = b[j].strip()

            a = " ".join(b)

    print "cleaned filename with extension is --> {}".format(a)

    print a

    try:

        match = re.split(r'[([Ss]eason \d{2})]', a)
        seasonNumber = re.findall(r'\d+', match[1])
        seasonNumber = seasonNumber[0]

        episodeNumber = re.findall(r'\d+', match[2])
        episodeNumber = episodeNumber[0]

        try:
            extension = re.split(r' - ', match[-1])
            extension = " - " + extension[1]
            print extension

        except:
            extension = re.findall(r'\.\w+', match[-1])
            extension = extension[0]

            ans = (match[0] + '- s' + seasonNumber + 'e' + episodeNumber + extension)
            shutil.move(a, ans)

    except:
        # Check for SxxExx naming
        try:
            match = re.split(r'([sS]\d{2}[eE]\d{2})', a)

            # Clean whitespaces after split
            for j in range(0, len(match)):
                match[j] = match[j].strip()
            a = (" - ").join(match)
        except:
            print("skipped")

    # Clean any empty brackets
    try:
        a = re.split(r'[\[\{\(]\s?[\]\}\)]', a)
        a = "".join(a)
    except:
        pass

    # Replace the file names
    shutil.move(storedval, a)
