# Plex filename parser using Python [![CodeFactor](https://www.codefactor.io/repository/github/shreyasgaonkar/plex-filename-parser/badge)](https://www.codefactor.io/repository/github/shreyasgaonkar/plex-filename-parser) ![Tests](https://github.com/shreyasgaonkar/Plex-filename-parser/actions/workflows/tests.yml/badge.svg)

While trying to clean my Plex media database, I was tired of changing the naming schemes to match [Plex's standards](https://support.plex.tv/articles/naming-and-organizing-your-tv-show-files/). I wrote this simple script in Python to clean (most) of my databases which typically would take me hours of my weekend time to sit and manually update it. In few cases (duplicate file names), I still have to manually intervene once a while, but that is far less work as before.

### Installation:

0. Install Python3.x
1. Copy the python file, and update the directory where we want to process the filenames.
2. Edit file location: ```TARGET_DIR = '/path/to/<media>/directory'``` to parse the files.
3. Run - ```python movie_name_parser.py``` to clean Movie titles & ```python tv_show_name_parser.py``` for TV Shows

### Missing Info / Bugs

- :cold_sweat: Something broken? [Open an issue](https://github.com/shreyasgaonkar/Plex-filename-parser/issues) with a few sample inputs where it breaks. Screenshots help!

- For any addition feature request, [open a new issue](https://github.com/shreyasgaonkar/Plex-filename-parser/issues)

### Movie name parser

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

### TV-show name parser

Follows the requirements as per [Plex naming scheme](https://support.plex.tv/articles/200220687-naming-series-season-based-tv-shows/) -

```
/TV Shows
  /Grey's Anatomy
     /Season 02
         Grey's Anatomy - s02e01.avi
         Grey's Anatomy - s02e02.mkv
         Grey's Anatomy - s02e03.m4v
```

[movie_name_parser.py](movie_name_parser.py)

### Directory structure before:
```
$ tree .
.
├── avatar.2019
│   ├── VeNom\ [2018].mp4
│   ├── avatar-2019.mkv
│   └── avatar.2019.srt
├── harry\ potter\ and\ the\ half\ blood\ prince\ dvdrip\ 2006
│   └── harry\ potter\ and\ the\ half\ blood\ prince\ 2006.mkv
└── rise.of.the.planet.of.the.apes.iii.2015
    └── rise.of.the.planet.of.the.apes.iii.2015.mp4
```
### Directory structure after running the script:
```
$ tree .
.
├── Avatar\ (2019)
│   ├── Avatar\ (2019).mkv
│   ├── Avatar\ (2019).srt
│   └── Venom\ (2018).mp4
├── Harry\ Potter\ And\ The\ Half\ Blood\ Prince
│   └── Harry\ Potter\ And\ The\ Half\ Blood\ Prince\ (2006).mkv
└── Rise\ Of\ The\ Planet\ Of\ The\ Apes\ III\ (2015)
    └── Rise\ Of\ The\ Planet\ Of\ The\ Apes\ III\ (2015).mp4
```


### Output

```shell
[INFO] Starting script under /tmp/TV-Shows directory. If this isn't right, please replace the value of `TARGET_DIR` variable in this script.

Renamed directory: /tmp/TV-Shows/Grey's Anatomy (2001) 4k -> /tmp/TV-Shows/Grey's Anatomy (2001)

Renamed file: Grey'S Anatomy (2005) - s01e01 - Pt1.avi -> Grey's Anatomy (2005) - s01e01 - Pt1.avi
Renamed file: Grey'S Anatomy (2005) - s01e01 - Pt2.avi -> Grey's Anatomy (2005) - s01e01 - Pt2.avi
Renamed file: Grey'S Anatomy (2005) - s01e03.mp4 -> Grey's Anatomy (2005) - s01e03.mp4
Renamed file: Grey'S Anatomy (2005) - s01e02 - The First Cut Is The Deepest.avi -> Grey's Anatomy (2005) - s01e02 - The First Cut Is The Deepest.avi

[INFO] Finished execution
```

### Changelog

Check [Changelog.md](https://github.com/shreyasgaonkar/Plex-filename-parser/blob/master/CHANGELOG.md)
