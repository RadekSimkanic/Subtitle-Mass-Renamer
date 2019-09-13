__author__ = 'gulliver - Radek Simkanic'

import argparse
from core.renamer import Renamer


def parseArguments():
    parser = argparse.ArgumentParser(
        description="Rename multiple subtitles automatically")

    parser.add_argument('-s', '--subtitle', required=True,
                        help="Subtitle file extension")
    parser.add_argument('-m', '--movie', required=True,
                        help="Video file extension")
    parser.add_argument('-d', '--directory', help="Directory containing files",
                        default=".")
    parser.add_argument('-t', '--test', action='store_true',
                        help="Run in test mode")

    return parser.parse_args()


def main():
    args = parseArguments()

    r = Renamer(args.directory)
    r.setFirstSuffix(args.movie)
    r.setSecondSuffix(args.subtitle)
    if args.test:
        r.testMode()

    r.do()


if __name__ == "__main__":
    main()
