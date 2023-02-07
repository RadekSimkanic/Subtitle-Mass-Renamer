__author__ = "gulliver - Radek Simkanic"

import argparse
from argparse import RawDescriptionHelpFormatter
from core.renamer import Renamer


def parseArguments():
    parser = argparse.ArgumentParser(
        description="Rename multiple subtitles automatically",
        epilog=(
            "Examples:\n"
            "\tpython subtitle-renamer.py\n"
            "\tpython subtitle-renamer.py -t\n"
            "\tpython subtitle-renamer.py -m mkv\n"
            "\tpython subtitle-renamer.py -s ass\n"
            "\tpython subtitle-renamer.py -s txt -m avi\n"
            "\tpython subtitle-renamer.py -d ../../Video/\n"
            "\tpython subtitle-renamer.py -d ../../Video/ -l eng\n"
            "\tpython subtitle-renamer.py -s srt -m mp4 -d ../../Video/ -t"
        ),
        formatter_class=RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "-s",
        "--subtitle",
        help="Subtitle file extension, i.e. srt, txt, ass, etc. Default: srt",
        default="srt",
    )
    parser.add_argument(
        "-m",
        "--movie",
        help="Video file extension, i.e. avi, mkv, mp4, etc. Default: mp4",
        default="mp4",
    )
    parser.add_argument(
        "-d",
        "--directory",
        help="Directory containing files. Defaults to current directory.",
        default=".",
    )
    parser.add_argument("-t", "--test", action="store_true", help="Run in test mode")

    parser.add_argument(
        "-l",
        "--language",
        help="Language code to be added to\
                         the subtitles, e.g. en or eng. Default: en",
        default="en",
    )

    return parser.parse_args()


def main():
    args = parseArguments()

    r = Renamer(args.directory, args.subtitle, args.movie, args.language)

    if args.test:
        r.testMode()

    r.do()


if __name__ == "__main__":
    main()
