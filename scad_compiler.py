#!/usr/bin/env python3

import argparse
import os
from shutil import SameFileError, copy
from subprocess import run

parser = argparse.ArgumentParser()
parser.add_argument(
    "--format", "-f", help="File format to compile to (stl, off, amf, dxf, svg, png)")
parser.add_argument(
    "--outDir", "-o", help="Store the files into a directory (will create if doensn't already exist")
parser.add_argument(
    "--tag", "-t", help="The tag string to search for, 'TOGGLE TAG' is used by default")
parser.add_argument(
    "--input", "-i", help="Input SCAD file to compile the components of")

args = parser.parse_args()

if args.outDir:
    path = str(args.outDir)
    if not os.path.isdir(args.outDir):
        os.mkdir(args.outDir)


tag = "TOGGLE TAG"
if args.tag:
    tag = args.tag


tmp_file = "tmp.scad"


with open(args.input, "r") as in_file:
    lines = in_file.read().split("\n")

    # find all tags in the file
    for i, line in enumerate(lines):
        if tag in line:
            line_tag = line.split(":")[1].replace(" ", "")
            print(f"Compiling {i} : {line_tag}")

            # open tmp file to write the components to
            with open("tmp.scad", "w") as tmp_file:
                for j in range(i):
                    tmp_file.write(lines[j] + "\n")

                tmp_file.write("!" + lines[i+1] + "\n")

                for j in range(i+1, len(lines)):
                    tmp_file.write(lines[j] + "\n")

            # create name of new compilation
            out_path = args.outDir + "/" + line_tag + "."
            if args.format:
                out_path += args.format
            else:
                out_path += "stl"

            print(f"Running openscad: {out_path}")
            scad_runner = run(
                ["openscad", "-o", out_path, "tmp.scad"], check=True)
            scad_runner.check_returncode()


os.remove("tmp.scad")
print("Done")
