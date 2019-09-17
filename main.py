__author__ = 'gulliver - Radek Simkanic'

import argparse
from argparse import RawDescriptionHelpFormatter
from core.renamer import Renamer


def parseArguments():
    parser = argparse.ArgumentParser(
        description="Rename multiple subtitles automatically",
        epilog=(
            'Examples:\n'
            '\tpython main.py -s txt -m avi .\n'
            '\tpython main.py -s srt -m mp4 ../../Video/\n'
            '\tpython main.py -s my_serial_series_01_episode_01.txt -m my_serial_SE01E01.avi ../../Video/\n'
            '\tpython main.py -s /home/user/Video/my_serial_series_01_episode_01.txt -m /home/user/Video/my_serial_SE01E01.avi /home/user/Video/\n'
            '\tpython main.py -s srt -m mp4 ../../Video/ -t'
        ),
        formatter_class=RawDescriptionHelpFormatter
    )

    parser.add_argument('-s', '--subtitle', required=True,
                        help="Subtitle file extension, i.e. srt, txt, ass, etc.")
    parser.add_argument('-m', '--movie', required=True,
                        help="Video file extension, i.e. avi, mkv, mp4, etc.")
    parser.add_argument('-d', '--directory', help="Directory containing files",
                        default=".")
    parser.add_argument('-t', '--test', action='store_true',
                        help="Run in test mode")

    parser.add_argument('-l', '--language', help="Language code to be added to\
                         the subtitles, e.g. en or eng", default="")

    return parser.parse_args()


def main():
    args = parseArguments()

    r = Renamer(args.directory, args.subtitle, args.movie, args.language)

    if args.test:
        r.testMode()

    r.do()


if __name__ == "__main__":
    main()
