# Plex filename parser using Python

While trying to clean my plex movie database, I was tired of changing the naming schemes to match Plex's. I wrote this simple script in Python to clean (most) of my databases which typically would take me hours of my weekend time to sit and manually update it. In few cases (duplicate file names), I still have to manually intervene once a while, but that is far less work as before.

Installation:

0. Install Python2.x
1. Copy the python file, and update the directory where we want to process the filenames.
2. Edit file location ```os.chdir('/path/to/movies/directory')``` to parse the files.
3. Run - ```python movie_name_parser.py``` to clean movie titles / ```python tv_show_name_parser.py``` for tv-shows

## Movie name parser

Follows the requirements as per [Plex naming scheme](https://support.plex.tv/articles/200381023-naming-movie-files/) -

```
/Movies
   /Avatar (2009)
      Avatar (2009).mkv
   /Batman Begins (2005)
      Batman Begins (2005).mp4
      Batman Begins (2005).eng.srt
      poster.jpg
```

## TV-show name parser

Follows the requirements as per [Plex naming scheme](https://support.plex.tv/articles/200220687-naming-series-season-based-tv-shows/) -

```
/TV Shows
  /Grey's Anatomy
     /Season 02
         Grey's Anatomy - s02e01.avi
         Grey's Anatomy - s02e02.mkv
         Grey's Anatomy - s02e03.m4v
```

## Changelog

Check [Changelog.md](https://github.com/shreyasgaonkar/Plex-filename-parser/blob/master/CHANGELOG.md)
