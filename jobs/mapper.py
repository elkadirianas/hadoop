#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    # Extract genres from the end
    try:
        last_comma = line.rindex(',')
        genre_part = line[last_comma + 1:]

        # Handle multiple genres
        genres = genre_part.split('|')
        for genre in genres:
            print("%s\t1" % genre)
    except Exception:
        continue

