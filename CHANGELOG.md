#### 1.1.5

* **Improvements:** Cleaned underlying code [tv_show_name_parser.py](tv_show_name_parser) to better handle files and directories for TV shows. This should run faster for large files using multithreading.

#### 1.1.4

* **Feature:** [movie_name_parser.py](/movie_name_parser.py) supports file and directory name cleanup. Fixes [#3](https://github.com/shreyasgaonkar/Plex-filename-parser/issues/3). Updated README for before and after output.

#### 1.1.3

* **Improvements:** Cleaned underlying code ```tv_show_name_parser``` to parse files. Code is now PEP8 complaint :tada:

#### 1.1.2

* **Feature:** TV show script checks for "." in the filename & checks for the SxxExx format to include in the cleaned file which was missing from the previous version.

#### 1.1.1

* **Feature:** TV show script now searches for the Episode name and adds to the filename as required by Plex naming convention.

#### 1.1.0

##### Documentation Changes

* **New Features:** Add new script to clean TV show files

#### 1.0.0

* **New Features:**  Add movie parser file
