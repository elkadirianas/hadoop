#!/usr/bin/env python3
import sys

current_genre = None
count = 0

for line in sys.stdin:
    genre, value = line.strip().split('\t')
    value = int(value)
    if genre == current_genre:
        count += value
    else:
        if current_genre:
            print(f"{current_genre}\t{count}")
        current_genre = genre
        count = value

# Output the last one
if current_genre:
    print(f"{current_genre}\t{count}")

