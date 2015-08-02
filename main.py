#!/usr/bin/python
#UTF-8
__author__ = 'gulliver - Radek Simkanic'

from core.application_arguments import *
from core.messages import *
from core.renamer import *



def main():
    # Applications arguments
    arg_movie = Argument("m", "movie", "First file suffix (suffix of movies)", True, True)
    arg_subtitle = Argument("s", "subtitle", "Second file suffix (suffix of subtitles)", True, True)
    arg_directory = Argument("d", "directory", "Source directory", True, False)

    # Arguments dependencies
    arg_movie.setDependencies([
        arg_subtitle
    ])

    arg_subtitle.setDependencies([
        arg_movie
    ])

    arg = Arguments()
    arg.setHeadInformation("Last params without commands is source directory with files of movies and subtitles.")\
    .addArgument(
        arg_movie
    )\
    .addArgument(
        arg_subtitle
    )\
    .addArgument(
        arg_directory, True
    )\
    .check()

    r = Renamer(arg_directory.getValue())
    r.setFirstSuffix(arg_movie.getValue())
    r.setSecondSuffix(arg_subtitle.getValue())
    r.do()

if __name__ == "__main__":
    main()