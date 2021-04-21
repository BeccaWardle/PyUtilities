#!/usr/bin/env python3
import datetime
from math import floor


def time(nowOrNot=True):
    if nowOrNot:
        currentDT = datetime.datetime.now()
        sHour = int(currentDT.hour)
        sMin = int(currentDT.minute)
    else:
        start = str(input("enter start time: "))
        sHour = int(start[:2])
        sMin = int(start[2:4])

    stop = str(input("enter end time: "))
    eHour = int(stop[:2])
    eMin = int(stop[2:4])
    time = 0

    if ((eHour < sHour) and (sMin == 0)):
        time = time + eHour*60 + (24 - sHour)*60
    elif ((eHour < sHour) and (sMin != 0)):
        time = time + eHour * 60 + (24 - sHour - 1) * 60
    else:
        # print("running else")
        time = (eHour - sHour)*60
    if sMin != 0:
        time = time + eMin + (60-sMin)
    else:
        time += eMin

    print("time = ", time, " minutes")
    print(floor(time/60), " hours and ", time % 60, " minutes")
    return time


choice = str(input("Is the start time now? ")).upper()
if choice == "Y" or choice == "YES":
    minTime = time(True)
else:
    minTime = time(False)

print("\n")
shutterSpeed = float(input("What shutter Speed will be used: "))
frames = (minTime*60)/shutterSpeed + 1
print("This will be: ", f'{round(frames):, }', " images")

if frames/25 > 60:
    print("Which will be: ", floor((frames/25)/60), " mins ", round((((frames/25)/60) % 1)*60), "secs")
else:
    print("Which will be: ", round(frames/25, 1), " seconds in length")
