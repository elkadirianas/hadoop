#!/usr/bin/env python3
import sys

for line in sys.stdin:
    if line.startswith("movieId"):
        continue
    parts = line.strip().split(',')
    if len(parts) < 3:
        continue
    genres_field = ','.join(parts[2:])
    genres = genres_field.split('|')
    for genre in genres:
        print("{}\t1".format(genre))

