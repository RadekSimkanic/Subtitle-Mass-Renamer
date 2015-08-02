# Subtitle Mass Renamer

## What is it?
Subtitle Mass Renamer is Python script for rename files (especially subtitles) with specific suffix to the same name files with another specific suffix.

## Prerequisites
- Python interpreter version 2

## How to use
Download actual source code (unpacking) and run:
```
git clone git@github.com:RadekSimkanic/Subtitle-Mass-Renamer.git
cd Subtitle-Mass-Renamer
python main.py -s <suffix of subtitles> -m <suffix of movies> <location>
```

- <suffix of subtitles> - included suffix eg.: txt, .txt and also filename or filepath -> autodetection suffix (for simpler use - drag and drop)
- <suffix of movies> - see to <suffix of subtitles>
- <location> - location of directory contains subtitles and movies

Examples:
```
python main.py -s txt -m avi .
python main.py -s txt -m avi ../../Video/
python main.py -s my_serial_series_01_episode_01.txt -m my_serial_SE01E01.avi ../../Video/
python main.py -s /home/user/Video/my_serial_series_01_episode_01.txt -m /home/user/Video/my_serial_SE01E01.avi /home/user/Video/
```
