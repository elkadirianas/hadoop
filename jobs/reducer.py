#!/usr/bin/env python3

import sys

current_genre = None
count = 0

for line in sys.stdin:
    genre = line.strip()
    if genre == current_genre:
        count += 1
    else:
        if current_genre:
            print("{0}\t{1}".format(current_genre, count))
        current_genre = genre
        count = 1

# Don't forget the last one
if current_genre:
    print("{0}\t{1}".format(current_genre, count))

