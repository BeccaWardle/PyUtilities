#!/usr/bin/env python3
from math import factorial

def wordformer(word, pointers):
    # newword = ""
    # for point in pointers:
    #     newword = newword + word[point]
    # return newword
    return "".join(str(pointers))

def anagramer(oldword):
    anagrams = list()
    pointers = list(range(0, len(oldword)))

    swapper, initial_comp, rearrange, asc_swapper = [0] * 4
    count = 2
    anagrams.append(wordformer(oldword, pointers))

    while count <= factorial(len(oldword)):
        initial_comp = len(oldword)-2

        while initial_comp >= 0:
            if pointers[initial_comp] < pointers[initial_comp+1]:
                break
            initial_comp -=1
        rearrange = initial_comp + 1
        asc_swapper = len(oldword) - 1

        while rearrange < asc_swapper:
            swapper = pointers[rearrange]
            pointers[rearrange] = pointers[asc_swapper]
            pointers[asc_swapper]= swapper
            rearrange  += 1
            asc_swapper -= 1

        rearrange = len(oldword) -1

        while pointers[rearrange] > pointers[initial_comp]:
            rearrange-=1
        rearrange += 1
        swapper = pointers[initial_comp]
        pointers[initial_comp] = pointers[rearrange]
        pointers[rearrange] = swapper

        returned = wordformer(oldword, pointers)
        anagrams.append(returned)
        count += 1
    return anagrams


###########################################
anagram = str(input("Anagram to solve: ")).lower()
#choice = str(input("True solution? ")).upper() 
wordlist = list()

with open("wordList.txt", "r") as file:
    for line in file:
        if (len(line) <= len(anagram)+1):
            line = line.replace("\n", "")
            wordlist.append(line.lower())

#if choice == "Y" or choice == "YES":
for word in wordlist:
    if len(word) != len(anagram):
        wordlist.remove(word)

anagrams = anagramer(anagram)

print ("Anagrams: ")
for word in wordlist:
    for anagram in anagrams:
        if word == anagram:
            print(anagram)

