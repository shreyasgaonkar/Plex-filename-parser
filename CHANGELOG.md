#### 1.2.2
* **Improvements:** Handle invalid file names and duplicate directories gracefully.

#### 1.2.1
* **Improvements:** Add python type hints.

#### 1.2
* **Improvements:** Add python unit tests, GitHub actions to automatically test new changes and refactor code.

#### 1.1.9
* **Improvements:** Minor code change.

#### 1.1.8
* **Improvements:** Clean tv_show_name_parser.py](tv_show_name_parser) functions and verify unit tests.

#### 1.1.7
* **Improvements:** Add test_movie_name_parser.py unit test and fix movie_name_parse filename bug for year_fix() function.

#### 1.1.6
* **Improvements:** Delete unwanted files, add unit tests and fix unhandled bugs caught in unit test. Add gitignore.

#### 1.1.5

* **Improvements:** Clean underlying code [tv_show_name_parser.py](tv_show_name_parser) to better handle files and directories for TV shows. This should run faster for large files using multithreading.

#### 1.1.4

* **Feature:** [movie_name_parser.py](/movie_name_parser.py) supports file and directory name cleanup. Fixes [#3](https://github.com/shreyasgaonkar/Plex-filename-parser/issues/3). Updated README for before and after output.

#### 1.1.3

* **Improvements:** Clean underlying code ```tv_show_name_parser``` to parse files. Code is now PEP8 complaint :tada:

#### 1.1.2

* **Feature:** TV show script checks for "." in the filename & checks for the SxxExx format to include in the cleaned file which was missing from the previous version.

#### 1.1.1

* **Feature:** TV show script now searches for the Episode name and adds to the filename as required by Plex naming convention.

#### 1.1.0

* **Features:** Add [tv_show_name_parser.py](tv_show_name_parser) to clean TV show files

#### 1.0.0

* **Features:**  Add [movie_name_parser.py](/movie_name_parser.py)
