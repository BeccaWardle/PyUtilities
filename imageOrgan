#!/usr/bin/env python3
import argparse
import os
from datetime import date, datetime
from filecmp import cmp
from shutil import copy2, disk_usage, move
from PIL import Image

# shutil import rmtree # unsure of original use

# checks there is enough space on the disk to duplicate all the images into a tree
dFree = disk_usage("/").free
dUsed = sum(d.stat().st_size for d in os.scandir() if d.is_file())
if dFree <= dUsed:
    raise OSError("Disk too full to perform this operation")

# parses arguments passed to program such as whether to copy or if a source and output file has been set
parser = argparse.ArgumentParser()
parser.add_argument("--copy", "-c", help="set the program to copy files instead of move", action="store_true")
parser.add_argument("--delete", "-d", help="delete files from source if they are found in the output folder", action="store_true")
parser.add_argument("--source", "-s", help="set the source directory")
parser.add_argument("--output", "-o", help="set the output directory")
parser.add_argument("--no-log", "-l", help="turn off the logging function", action="store_true")
args = parser.parse_args()

# if source is passed as arg sets that, uses current directo
if args.source:
    origin_path = args.source
    os.chdir(origin_path)
# else:
    # if os.name == "posix":
    #     origin_path = os.path.expanduser("~")+"/Pictures/dump"
    # elif os.name == "nt":
    #     origin_path = "D:/Pictures/SD_BackUp/Dump"


if args.output:
    dest_path = args.output
else:
    dest_path = "../Photos"

if not os.path.isdir(dest_path):
    os.mkdir(dest_path)
    # used to delete the pre-existing file structure with the sorted photos(?), now it should just add ones that don't alread exist
    # rmtree(dir_Name, True)


months = ["01-Jan", "02-Feb", "03-Mar", "04-Apr", "05-May", "06-Jun", "07-Jul",
          "08-Aug", "09-Sep", "10-Oct", "11-Nov", "12-Dec"]

log = ""

if os.path.isfile(dest_path + "/log.txt"):
    logger = open(dest_path + "/log.txt", "a+")
else:
    logger = open(dest_path + "/log.txt", "w+")
logger.write("Update: " + str(date.today()) + "\n")

# iterates over all files in the directory collecting datestamps and placing them into directories of those dates
for root, dirs, files in os.walk("."):
    for file_Name in files:
        if file_Name.lower().split(".")[-1] not in ["jpg", "cr2", "png", "gif", "tif"]:
            log += "Skipping over " + file_Name + "\n"
            continue

        source_path = os.path.join(root, file_Name)
        # try to get proper date taken via exif data
        try:
            take_date = Image.open(source_path).getexif()[36867].split(":")
            file_Year = take_date[0]
            file_Month = months[int(take_date[1])-1]
            file_Date = take_date[2].split()[0]
        # if failure rely on windows date created time
        except KeyError:
            file_Year = datetime.fromtimestamp(os.path.getmtime(source_path)).strftime('%Y')
            file_Month = months[int(datetime.fromtimestamp(os.path.getmtime(source_path)).strftime('%m'))-1]
            file_Date = datetime.fromtimestamp(os.path.getmtime(source_path)).strftime('%d')

        # checks if the file under that name exists, if it is not the same moves the file with an appendix, otherwise skips
        appendix = ""
        toCopy = True
        toDelete = False
        final_dest = file_Year + "/" + file_Month + "/" + file_Date
        while (os.path.isfile(dest_path + "/" + final_dest + "/" + file_Name + appendix)):
            # initial check of file size
            if os.path.getsize(source_path) == os.path.getsize(dest_path + "/" + final_dest + "/" + file_Name + appendix):
                # true comparison of file
                if cmp(source_path, dest_path + "/" + final_dest + "/" + file_Name + appendix, shallow=False):
                    toDelete = True
                    toCopy = False
                    break

            if appendix == "":
                appendix = "_1"
            elif appendix[1] == "9":
                log += "To many duplicates of: " + str(source_path) + "\n"
                toCopy = False
                break
            else:
                log += "File: " + str(source_path) + "had same name as " + str(dest_path) + "/"+str(file_Name) + "\n"
                appendix = "_" + str(int(appendix[1])+1)
                toDelete = False
                toCopy = True

        if args.delete and toDelete:
            log += "Duplicate: " + str(source_path) + " was deleted\n"
            os.remove(source_path)
            continue

        elif toDelete and not toCopy:
            log += "File: " + str(source_path) + "/" + str(file_Name) + " is a duplicate in " + dest_path + "/" + file_Month + "/" + file_Date + "/\n"
            continue

        elif not toCopy:
            log += "File: " + str(source_path) + " was a not moved/saved\n"
            continue

        # creates the year, month & date directories if they don't already exist
        if not os.path.isdir(dest_path + "/" + file_Year):
            os.mkdir(dest_path + "/" + file_Year)
        if not os.path.isdir(dest_path + "/" + file_Year + "/" + file_Month):
            os.mkdir(dest_path + "/" + file_Year + "/" + file_Month)
        if not os.path.isdir(dest_path + "/" + file_Year + "/" + file_Month + "/" + file_Date):
            os.mkdir(dest_path + "/" + file_Year + "/" + file_Month + "/" + file_Date)

        if args.copy:
            copy2(source_path, dest_path + "/" + final_dest + "/" + file_Name + appendix)
            log += "Copied " + str(source_path) + " as: " + dest_path + final_dest + file_Name + appendix + "\n"
        else:
            move(source_path, dest_path + "/" + final_dest + "/" + file_Name + appendix)
            log += "Moved " + str(source_path) + " to: " + str(dest_path) + str(final_dest) + str(file_Name) + str(appendix) + "\n"
        logger.write(log)
        log = ""

if os.path.isfile(dest_path + "/log.txt"):
    logger = open(dest_path + "/log.txt", "a+")
else:
    logger = open(dest_path + "/log.txt", "w+")

logger.write("\n\n")
logger.close()
