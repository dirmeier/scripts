#!/usr/bin/python

from __future__ import print_function, absolute_import
import sys, re


def usage():
    s = """Cut a file at a specified delimiter where the delimiter is a regex.
        USAGE:
            ./rcut <pattern> <file>
                - <pattern> := pattern for cutting
                - <folder>  := file to be cut

        EXAMPLE:
            './rcut \\d+ ~'"""
    print(s)
    exit(-1)




def main(args):
    if len(args) != 2:
        usage()
    pattern, f = args[0], args[1]
    with open(f, "r") as infile:
        for line in infile:
            print( "\t".join(re.split(pattern, line.rstrip())) )
            

if __name__ == "__main__":
    main(sys.argv[1:])
