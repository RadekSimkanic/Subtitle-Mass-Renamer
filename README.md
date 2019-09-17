# Subtitle Mass Renamer

## What is it?
Subtitle Mass Renamer is Python script for rename files (especially subtitles) with specific suffix to the same name files with another specific suffix.

## Prerequisites
- Python 3

## How to use
Download actual source code (unpacking):
```
git clone git@github.com:RadekSimkanic/Subtitle-Mass-Renamer.git
cd Subtitle-Mass-Renamer
```
Usage:
```
usage: main.py [-h] -s SUBTITLE -m MOVIE [-d DIRECTORY] [-t] [-l LANGUAGE]

Rename multiple subtitles automatically

optional arguments:
  -h, --help            show this help message and exit
  -s SUBTITLE, --subtitle SUBTITLE
                        Subtitle file extension, i.e. srt, txt, ass, etc.
  -m MOVIE, --movie MOVIE
                        Video file extension, i.e. avi, mkv, mp4, etc.
  -d DIRECTORY, --directory DIRECTORY
                        Directory containing files
  -t, --test            Run in test mode
  -l LANGUAGE, --language LANGUAGE
                        Language code to be added to the subtitles, e.g. en or
                        eng

Examples:
        python main.py -s txt -m avi .
        python main.py -s srt -m mp4 ../../Video/
        python main.py -s srt -m mp4 ../../Video/ -l eng
        python main.py -s my_serial_series_01_episode_01.txt -m my_serial_SE01E01.avi ../../Video/
        python main.py -s /home/user/Video/my_serial_series_01_episode_01.txt -m /home/user/Video/my_serial_SE01E01.avi /home/user/Video/
        python main.py -s srt -m mp4 ../../Video/ -t
```
