#!/usr/bin/python

from __future__ import print_function, absolute_import
import os, sys


def usage():
    s = """Print the number of files in the lowest sub-folder level of a specified folder.
        USAGE:
            ./lssub <pattern> <folder>
                - <pattern> := pattern to match the searched files
                - <folder>  := folder where the search starts

        EXAMPLE:
            './lssub txt ~'"""
    print(s)
    exit(-1)




def main(args):
    if len(args) != 2:
        usage()
    pattern, folder = args[0].lower(), args[1]
    for d, s, f in os.walk(folder):
        if len(s):
            continue
        files = filter(lambda x: pattern in x.lower(), f)
        if len(files):
            print("Directory ", d, ": ", len(files))


if __name__ == "__main__":
    main(sys.argv[1:])

