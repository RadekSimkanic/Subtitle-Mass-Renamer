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
usage: subtitle-renamer.py [-h] [-s SUBTITLE] [-m MOVIE] [-d DIRECTORY] [-t] [-l LANGUAGE]

Rename multiple subtitles automatically

options:
  -h, --help            show this help message and exit
  -s SUBTITLE, --subtitle SUBTITLE
                        Subtitle file extension, i.e. srt, txt, ass, etc. Default: srt
  -m MOVIE, --movie MOVIE
                        Video file extension, i.e. avi, mkv, mp4, etc. Default: mp4
  -d DIRECTORY, --directory DIRECTORY
                        Directory containing files. Defaults to current directory.
  -t, --test            Run in test mode
  -l LANGUAGE, --language LANGUAGE
                        Language code to be added to the subtitles, e.g. en or eng. Default: en

Examples:
        python subtitle-renamer.py
        python subtitle-renamer.py -t
        python subtitle-renamer.py -m mkv
        python subtitle-renamer.py -s ass
        python subtitle-renamer.py -s txt -m avi
        python subtitle-renamer.py -d ../../Video/
        python subtitle-renamer.py -d ../../Video/ -l eng
        python subtitle-renamer.py -s srt -m mp4 -d ../../Video/ -t
```
