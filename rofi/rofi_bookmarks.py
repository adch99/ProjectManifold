#!/bin/python3

import sys
import subprocess

def getBookmarks():
    inputfile = open("/home/aditya/.config/gtk-3.0/bookmarks", "r")
    inputdata = inputfile.readlines()
    inputfile.close()

    names = []
    paths = []

    for bookmark in inputdata:
        # First we remove the ending \n
        bookmark = bookmark[:-1]
        ending = bookmark.split("/")[-1].split(" ")
        if len(ending) == 1:
            name = ending[0]
        else:
            name = " ".join(ending[1:])

        path = bookmark.split(" ")[0]
        names.append(name)
        paths.append(path)
    bookmarks = dict(zip(names, paths))
    return bookmarks

def printProperties():
    print("\0prompt\x1f> ")

def printList(bookmarks):
    for name in bookmarks.keys():
        print(f"{name}\0icon\x1ffolder")

def main(argc, argv):
    bookmarks = getBookmarks()

    if argc == 1:
        printProperties()
        printList(bookmarks)
    else:
        try:
            path = bookmarks[argv[1]]
            subprocess.Popen(["exo-open", path])
        except KeyError:
            exit(0)

if __name__ == "__main__":
    argc = len(sys.argv)
    main(argc, sys.argv)
