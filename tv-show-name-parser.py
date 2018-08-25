#!/usr/bin/python
import re
import os
import shutil

files = os.listdir("/path/to/tv-shows/directory")

for a in files:
  try:
    match = re.split(r'([Ss]eason \d{2})', a)

    seasonNumber = re.findall(r'\d+', match[1])
    seasonNumber = seasonNumber[0]

    episodeNumber = re.findall(r'\d+', match[2])
    episodeNumber = episodeNumber[0]
    
    # Check for name of the episode, if yes, add it to the filename
    try:
      extension = re.split(r'-', match[-1])
      extension = " -" + extension[1]
      print extension

    # No episode name, continue with the filename  
    except:
      extension = re.findall(r'\.\w+', match[-1])
      extension = extension[0]

    ans =  (match[0] + '- s' + seasonNumber + 'e' + episodeNumber + extension)
    shutil.move(a, ans)

  except:
    print("skipped")
