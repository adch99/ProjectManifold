#!/bin/python3

inputfile = open("/home/aditya/.config/gtk-3.0/bookmarks", "r")
bookmarks = inputfile.readlines()
inputfile.close()

outfilename = "/home/aditya/ProjectManifold/rofi/PlacesBookmarks/{0}.desktop"
contents = """
[Desktop Entry]
Name={1}
URL={0}
Type=Link
Comment=Opens the {1} Folder in File Manager
Icon=folder
NoDisplay=true
"""

for bookmark in bookmarks:
    # First we remove the ending \n
    bookmark = bookmark[:-1]
    name = bookmark.split("/")[-1].split(" ")[0]
    path = bookmark.split(" ")[0]
    print(f"Name: {name}")
    print(f"Path: {path}")
    print()
    outfile = open(outfilename.format(name), "w")
    outfile.write(contents.format(path, name))
    outfile.close()
