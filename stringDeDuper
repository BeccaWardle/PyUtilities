#!/usr/bin/env python3
"""
Takes a file of strings and sorts them. Intented to be run with -u, which removes non-unique strings and -I which ignores the first n chars of the string when sorting and deleting the strings

Was written with mind to sort out files such as .zsh_history which have unique keys beginning each file but can then have many duplicate commands saved
"""

import argparse
from sys import argv

# command line arguments
parser = argparse.ArgumentParser(description="Takes a file of strings and sorts them and then prints or saves to a file")
parser.add_argument("-i", help="input file")
parser.add_argument("-o", help="output file")
parser.add_argument("--ignore", "-I", help="Ignore first N chars of each line in file", type=int)
parser.add_argument("--unique", "-u", help="Save only unique lines to source", action="store_true")
parser.add_argument("--verbose", "-v", help="Verbose mode", action="store_true")

# if no arguments print help
if len(argv) ==1:
    parser.print_help()
    exit()

args = parser.parse_args()

inFile = open(args.i, "r")
if args.o:
    outFile = open(args.o, "w")

ignore = 0
if args.ignore:
    ignore = args.ignore

# read file
lines = []
for line in inFile:
    lines.append(line.rstrip("\n"))

inFile.close()
size = len(lines)

# sort list
lines.sort(key=lambda x: x[ignore:])

# remove non-unique patterns
if args.unique:
    index = 0
    while index < len(lines) - 1:
        if lines[index][ignore:] == lines[index + 1][ignore:]:
            if lines[index] < lines[index + 1]:
                if args.verbose:
                    print("Removed:", lines[index + 1])
                del lines[index + 1]
            else:
                if args.verbose:
                    print("Removed:", lines[index])
                del lines[index]
        else:
            index += 1

diff = size - len(lines)

# output
if args.o:
    if args.verbose:
        print("Writing to:", args.o)
    for line in lines:
        outFile.write(line + "\n")
    outFile.close()
else:
    for line in lines:
        print(line)

if args.verbose:
    print("Removed:", diff, "lines")
